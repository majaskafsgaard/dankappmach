#!/usr/bin/env python
# coding: utf-8

# # AppliedML solution file reader
# 
# This notebook is used for reading solutions. Note: it will only print the first 5 error messages of each check.

# We start by defining the folder holding the solutions

# In[1]:


directory = 'solutions'


# Then we read all the files in the folder, which correspond to the format, and verify the prediction/variablelist pairs

# In[2]:


import os

def init_entry():
    tmp = {}
    tmp['Classification'] = {}
    tmp['Regression'] = {}
    tmp['Clustering'] = {}
    return tmp

def read_filenames(directory):
    tmp = {}
    for filename in os.listdir(directory):
        full_path = f'{directory}/{filename}'
        if not os.path.isfile(full_path) or not filename.endswith('.txt'):
            continue
        splitted = filename.split('_')
        
        project_part = splitted[0]
        student_name = splitted[1]
        is_varlist = splitted[-1].lower() == 'variablelist.txt'
        implementation = splitted[-2] if is_varlist else splitted[-1].split('.txt')[0]
        
        if student_name not in tmp:
            tmp[student_name] = init_entry()
        if implementation not in tmp[student_name][project_part]:
            tmp[student_name][project_part][implementation] = {}
        
        if is_varlist:
            tmp[student_name][project_part][implementation]['vars'] = full_path
        else:
            tmp[student_name][project_part][implementation]['preds'] = full_path
    return tmp

all_errors = 0
errors = 0
def write_error(msg, cap=5):
    global errors
    if errors < cap:
        print (msg)
    errors += 1

names = read_filenames(directory)


# Then we can print the structure:

# In[3]:


all_errors += errors
errors = 0

for name, parts in names.items():
    print (f'{name}:')
    for part, implementations in parts.items():
        print (f'    {part}:')
        if len(implementations) == 0:
            write_error(f'        {part} does not have any files')
        else:
            for implementation, files in implementations.items():
                if ('vars' not in files) and ('preds' not in files):
                    write_error(f'            {implementation} does not have a full prediction/variablelist set')
                else:
                    print (f'        {implementation}:')
                    print (f'            preds: {files["preds"]}')
                    print (f'            vars:  {files["vars"]}')

if errors == 0:
    print ('Files read succesfully')
else:
    print (f'Reading files gave {errors} errors')


# Then we verify the VariableList files

# In[4]:


all_variables = ['actualInteractionsPerCrossing', 'averageInteractionsPerCrossing', 'correctedActualMu', 'correctedAverageMu', 'correctedScaledActualMu', 'correctedScaledAverageMu', 'NvtxReco', 'p_nTracks', 'p_pt_track', 'p_eta', 'p_phi', 'p_charge', 'p_qOverP', 'p_z0', 'p_d0', 'p_sigmad0', 'p_d0Sig', 'p_EptRatio', 'p_dPOverP', 'p_z0theta', 'p_etaCluster', 'p_phiCluster', 'p_eCluster', 'p_rawEtaCluster', 'p_rawPhiCluster', 'p_rawECluster', 'p_eClusterLr0', 'p_eClusterLr1', 'p_eClusterLr2', 'p_eClusterLr3', 'p_etaClusterLr1', 'p_etaClusterLr2', 'p_phiClusterLr2', 'p_eAccCluster', 'p_f0Cluster', 'p_etaCalo', 'p_phiCalo', 'p_eTileGap3Cluster', 'p_cellIndexCluster', 'p_phiModCalo', 'p_etaModCalo', 'p_dPhiTH3', 'p_R12', 'p_fTG3', 'p_weta2', 'p_Reta', 'p_Rphi', 'p_Eratio', 'p_f1', 'p_f3', 'p_Rhad', 'p_Rhad1', 'p_deltaEta1', 'p_deltaPhiRescaled2', 'p_TRTPID', 'p_TRTTrackOccupancy', 'p_numberOfInnermostPixelHits', 'p_numberOfPixelHits', 'p_numberOfSCTHits', 'p_numberOfTRTHits', 'p_numberOfTRTXenonHits', 'p_chi2', 'p_ndof', 'p_SharedMuonTrack', 'p_E7x7_Lr2', 'p_E7x7_Lr3', 'p_E_Lr0_HiG', 'p_E_Lr0_LowG', 'p_E_Lr0_MedG', 'p_E_Lr1_HiG', 'p_E_Lr1_LowG', 'p_E_Lr1_MedG', 'p_E_Lr2_HiG', 'p_E_Lr2_LowG', 'p_E_Lr2_MedG', 'p_E_Lr3_HiG', 'p_E_Lr3_LowG', 'p_E_Lr3_MedG', 'p_ambiguityType', 'p_asy1', 'p_author', 'p_barys1', 'p_core57cellsEnergyCorrection', 'p_deltaEta0', 'p_deltaEta2', 'p_deltaEta3', 'p_deltaPhi0', 'p_deltaPhi1', 'p_deltaPhi2', 'p_deltaPhi3', 'p_deltaPhiFromLastMeasurement', 'p_deltaPhiRescaled0', 'p_deltaPhiRescaled1', 'p_deltaPhiRescaled3', 'p_e1152', 'p_e132', 'p_e235', 'p_e255', 'p_e2ts1', 'p_ecore', 'p_emins1', 'p_etconeCorrBitset', 'p_ethad', 'p_ethad1', 'p_f1core', 'p_f3core', 'p_maxEcell_energy', 'p_maxEcell_gain', 'p_maxEcell_time', 'p_maxEcell_x', 'p_maxEcell_y', 'p_maxEcell_z', 'p_nCells_Lr0_HiG', 'p_nCells_Lr0_LowG', 'p_nCells_Lr0_MedG', 'p_nCells_Lr1_HiG', 'p_nCells_Lr1_LowG', 'p_nCells_Lr1_MedG', 'p_nCells_Lr2_HiG', 'p_nCells_Lr2_LowG', 'p_nCells_Lr2_MedG', 'p_nCells_Lr3_HiG', 'p_nCells_Lr3_LowG', 'p_nCells_Lr3_MedG', 'p_pos', 'p_pos7', 'p_poscs1', 'p_poscs2', 'p_ptconeCorrBitset', 'p_ptconecoreTrackPtrCorrection', 'p_r33over37allcalo', 'p_topoetconeCorrBitset', 'p_topoetconecoreConeEnergyCorrection', 'p_topoetconecoreConeSCEnergyCorrection', 'p_weta1', 'p_widths1', 'p_widths2', 'p_wtots1', 'p_e233', 'p_e237', 'p_e277', 'p_e2tsts1', 'p_ehad1', 'p_emaxs1', 'p_fracs1', 'p_DeltaE', 'p_E3x5_Lr0', 'p_E3x5_Lr1', 'p_E3x5_Lr2', 'p_E3x5_Lr3', 'p_E5x7_Lr0', 'p_E5x7_Lr1', 'p_E5x7_Lr2', 'p_E5x7_Lr3', 'p_E7x11_Lr0', 'p_E7x11_Lr1', 'p_E7x11_Lr2', 'p_E7x11_Lr3', 'p_E7x7_Lr0', 'p_E7x7_Lr1' ]
max_variables = {
    'Classification': 15,
    'Regression': 10,
    'Clustering': 25,
}

all_errors += errors
errors = 0
for student_name, parts in names.items():
    for part, implementations in parts.items():
        for implementation, files in implementations.items():
            file = files['vars']
            count = 0
            with open(file, 'r') as f:
                for line in f:
                    var_name = line.rstrip()
                    if var_name not in all_variables:
                        write_error(f'Variable {var_name} not in the given variable list {file}')
                    else:
                        count += 1
            if count > max_variables[part]:
                write_error(f'Used too many variables ({count}/{max_variables[part]}) for {part}: {file}')
                    
if errors == 0:
    print ('Variables parsed without error')
else:
    print (f'Variables had {errors} errors')


# Then we can verify than the solution files

# In[5]:


test_entries = 160651
prediction_range = {
    'Classification': (0.0, 1.0),
    'Regression': (-float('inf'), float('inf')),
    'Clustering': (-float('inf'), float('inf')),
}

all_errors += errors
errors = 0
for student_name, parts in names.items():
    for part, implementations in parts.items():
        for implementation, files in implementations.items():
            file = files['preds']
            with open(file, 'r') as f:
                lines = [line for line in f]
            for i in range(len(lines)):
                if ',' in lines[i]:
                    index, value = lines[i].lstrip().rstrip().split(',')
                    try:
                        if int(index) != i:
                            write_error(f'Index at line {i+1} does not have correct index: {index}')
                    except ValueError:
                        write_error(f'Unable to cast the index to an integer: {index} in {file}')
                else:
                    value = lines[i].lstrip().rstrip()
                value = float(value)
                if part == 'Clustering':
                    if value.is_integer():
                        value = int(value)
                    else:
                        write_error(f'Clustering value at {i} is not an integer: {value} in {file}')
                        continue
                mi, ma = prediction_range[part]
                if not (value >= mi and value <= ma):
                    write_error(f'Value at {i} is not in the permitted range of ({mi},{ma}): {value} in {file}')
            if len(lines) != test_entries:
                write_error(f'Not enough predictions. Got {len(lines)}, expected {test_entries}')
                
if errors == 0:
    print ('Solutions parsed without error')
else:
    print (f'Solutions had {errors} errors')


# Finally, we check if all of the steps completed without error:

# In[6]:


if all_errors == 0:
    print ('All of parts of this submission had no errors')
else:
    print (f'This submission had {all_errors} errors')

