#coding:utf-8
import pydicom
import matplotlib.pyplot as plt
import pandas as pd
import os

# path = os.listdir('data')
path = os.listdir('data')
print(path)
file_name = []
def traverse(f):
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            # print('file: %s' % tmp_path)
            pass
        else:
            file_name.append(tmp_path)
            traverse(tmp_path)
    return file_name


pd_image = pd.read_csv('csv/nlst_sct_ct_image_info_20180720.csv', low_memory=False)

label_index = []
series_uid = []
for ii in range(len(path)):
    label = pd_image[pd_image.pid.isin([path[ii]])]
    label = label[label.numberimages > 100]
    label_index.append(label.index)
    for ij in range(len(label)):
        series_uid.append(pd_image.seriesinstanceuids[label_index[ii][ij]][-5:])




dir_name = []
for pathi in range(len(path)):
    fd = traverse('data/' + str(path[pathi]))

for uj in range(len(fd)):
    for uk in range(len(series_uid)):
        try:
            if fd[uj][38] != "1" and series_uid[uk] in fd[uj]:
                dir_name.append(fd[uj])
        except IndexError as e:
            continue


ct_data = pd.read_csv('csv/nlst_sct_ct_ab_20180720.csv', low_memory=False)

num = []
for ci in range(len(path)):
    ct_label = ct_data[ct_data.pid.isin([path[ci]])]
    ct_label = ct_label[~ct_label.sct_slice_num.isin(['NaN'])]
    ct_label = ct_label.sct_slice_num[ct_label.index]
    for cj in range(len(ct_label)):
        num.append(str("%06d" %int(ct_label.values[cj])) + '.dcm')


f_name = []
for ii in range(len(dir_name)):
    for ij in range(len(num)):
        f_name.append(dir_name[ii] + '/' + num[ij])


pd_alcohol = pd.read_csv('csv/AlcoholHistory.csv', low_memory=False)
pd_family = pd.read_csv('csv/FamilyLungCancerHistory .csv', low_memory=False)
pd_work = pd.read_csv('csv/WorkHistory.csv', low_memory=False)
pd_medical = pd.read_csv('csv/MedicalHistory.csv', low_memory=False)
pd_smoke = pd.read_csv('csv/SmokingHistory.csv', low_memory=False)

for ai in range(len(path)):
    pi_smoke = pd_smoke[pd_smoke.pid.isin([path[ai]])]
    pi_alcohol = pd_alcohol[pd_alcohol.pid.isin([path[ai]])]
    pi_family = pd_family[pd_family.pid.isin([path[ai]])]
    pi_medical = pd_medical[pd_medical.pid.isin([path[ai]])]
    pi_work = pd_work[pd_work.pid.isin([path[ai]])]
    # print pd_smoke.code.values[0]
    name = str(pd_smoke.code.values[0]) + '_' + \
           str(pd_alcohol.code.values[0]) + '_' +\
           str(pd_family.code.values[0]) + '_' + \
           str(pd_medical.code.values[0]) + '_' + \
           str(pd_work.code.values[0]) + '_'


for readi in f_name:
    # dcm = pydicom.read_file(readi)
    # plt.set_cmap(plt.gray())
    # plt.imsave('pic/' + name + readi[5:11] + '_' + readi[-16:-11],
    #            dcm.pixel_array)
    # print(readi)
    try:
        dcm = pydicom.read_file(readi)
        plt.set_cmap(plt.gray())
        plt.imsave('pic/' + name + readi[5:11] + '_' + readi[-16:-11],
                   dcm.pixel_array)
        del dcm
    except IOError as e:
        # print(readi[5:11])
        continue
