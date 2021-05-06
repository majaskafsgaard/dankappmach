#!/usr/bin/env python
# coding: utf-8

# # Reading the small project data into Python
#
# This file will show how to read the data from the files `train.h5` and
# `test.h5` into Python, for training.
#
# The files are available at:
# https://www.nbi.dk/~petersen/Teaching/ML2020/SmallProject/train.h5
# https://www.nbi.dk/~petersen/Teaching/ML2020/SmallProject/test.h5

# We start by opening the files and loading them into a pandas DataFrame
import h5py
import pandas

def load_data(name):
    with h5py.File(f'{name}.h5', 'r') as f:
        return pandas.DataFrame(f[name][:])

train = load_data('train')
test  = load_data('test')

# Then we can verify the shape
print(f'Shape of training data set: {train.shape}')
print(f'Shape of test data set: {test.shape}')

# As expected, the test set contains 2 columns less: `Truth` and `p_truth_E`.
#
# Then we copy the variable list from the course website
# https://www.nbi.dk/~petersen/Teaching/ML2020/SmallProject/VariableList.html>

all_variables = [
        'actualInteractionsPerCrossing', 'averageInteractionsPerCrossing',
        'correctedActualMu', 'correctedAverageMu', 'correctedScaledActualMu',
        'correctedScaledAverageMu', 'NvtxReco', 'p_nTracks', 'p_pt_track',
        'p_eta', 'p_phi', 'p_charge', 'p_qOverP', 'p_z0', 'p_d0', 'p_sigmad0',
        'p_d0Sig', 'p_EptRatio', 'p_dPOverP', 'p_z0theta', 'p_etaCluster',
        'p_phiCluster', 'p_eCluster', 'p_rawEtaCluster', 'p_rawPhiCluster',
        'p_rawECluster', 'p_eClusterLr0', 'p_eClusterLr1', 'p_eClusterLr2',
        'p_eClusterLr3', 'p_etaClusterLr1', 'p_etaClusterLr2',
        'p_phiClusterLr2', 'p_eAccCluster', 'p_f0Cluster', 'p_etaCalo',
        'p_phiCalo', 'p_eTileGap3Cluster', 'p_cellIndexCluster',
        'p_phiModCalo', 'p_etaModCalo', 'p_dPhiTH3', 'p_R12', 'p_fTG3',
        'p_weta2', 'p_Reta', 'p_Rphi', 'p_Eratio', 'p_f1', 'p_f3', 'p_Rhad',
        'p_Rhad1', 'p_deltaEta1', 'p_deltaPhiRescaled2', 'p_TRTPID',
        'p_TRTTrackOccupancy', 'p_numberOfInnermostPixelHits',
        'p_numberOfPixelHits', 'p_numberOfSCTHits', 'p_numberOfTRTHits',
        'p_numberOfTRTXenonHits', 'p_chi2', 'p_ndof', 'p_SharedMuonTrack',
        'p_E7x7_Lr2', 'p_E7x7_Lr3', 'p_E_Lr0_HiG', 'p_E_Lr0_LowG',
        'p_E_Lr0_MedG', 'p_E_Lr1_HiG', 'p_E_Lr1_LowG', 'p_E_Lr1_MedG',
        'p_E_Lr2_HiG', 'p_E_Lr2_LowG', 'p_E_Lr2_MedG', 'p_E_Lr3_HiG',
        'p_E_Lr3_LowG', 'p_E_Lr3_MedG', 'p_ambiguityType', 'p_asy1',
        'p_author', 'p_barys1', 'p_core57cellsEnergyCorrection', 'p_deltaEta0',
        'p_deltaEta2', 'p_deltaEta3', 'p_deltaPhi0', 'p_deltaPhi1',
        'p_deltaPhi2', 'p_deltaPhi3', 'p_deltaPhiFromLastMeasurement',
        'p_deltaPhiRescaled0', 'p_deltaPhiRescaled1', 'p_deltaPhiRescaled3',
        'p_e1152', 'p_e132', 'p_e235', 'p_e255', 'p_e2ts1', 'p_ecore',
        'p_emins1', 'p_etconeCorrBitset', 'p_ethad', 'p_ethad1', 'p_f1core',
        'p_f3core', 'p_maxEcell_energy', 'p_maxEcell_gain', 'p_maxEcell_time',
        'p_maxEcell_x', 'p_maxEcell_y', 'p_maxEcell_z', 'p_nCells_Lr0_HiG',
        'p_nCells_Lr0_LowG', 'p_nCells_Lr0_MedG', 'p_nCells_Lr1_HiG',
        'p_nCells_Lr1_LowG', 'p_nCells_Lr1_MedG', 'p_nCells_Lr2_HiG',
        'p_nCells_Lr2_LowG', 'p_nCells_Lr2_MedG', 'p_nCells_Lr3_HiG',
        'p_nCells_Lr3_LowG', 'p_nCells_Lr3_MedG', 'p_pos', 'p_pos7',
        'p_poscs1', 'p_poscs2', 'p_ptconeCorrBitset',
        'p_ptconecoreTrackPtrCorrection', 'p_r33over37allcalo',
        'p_topoetconeCorrBitset', 'p_topoetconecoreConeEnergyCorrection',
        'p_topoetconecoreConeSCEnergyCorrection', 'p_weta1', 'p_widths1',
        'p_widths2', 'p_wtots1', 'p_e233', 'p_e237', 'p_e277', 'p_e2tsts1',
        'p_ehad1', 'p_emaxs1', 'p_fracs1', 'p_DeltaE', 'p_E3x5_Lr0',
        'p_E3x5_Lr1', 'p_E3x5_Lr2', 'p_E3x5_Lr3', 'p_E5x7_Lr0', 'p_E5x7_Lr1',
        'p_E5x7_Lr2', 'p_E5x7_Lr3', 'p_E7x11_Lr0', 'p_E7x11_Lr1',
        'p_E7x11_Lr2', 'p_E7x11_Lr3', 'p_E7x7_Lr0', 'p_E7x7_Lr1'
    ]

# Finally, we divide the training data into data (`X`) and labels (`y`)
X = train[all_variables]
y = train['Truth']

print (f'Shape of X: {X.shape}')
print (f'Shape of y: {y.shape}')