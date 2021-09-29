# _*_ coding:utf-8 _*_
# @author:Jiajie Lin
# @file: train_ratio.py
# @time: 2020/05/13
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,5), dpi=120)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
x = (
     np.array([0.8360498579841501, 0.8818895234085107, 0.7174118766627045, 0.7366296519629887, 0.7986186827061038,
                    0.7654119404650785, 0.7558440245972031, 0.7527648484278491, 0.7487164298180005, 0.8449695002518328,
                    0.8623506867499545, 0.8536882411067194, 0.8709350203179484, 0.8140411624545103, 0.6734130016414784,
                    0.8372194377933796, 0.8249695002518328, 0.8303008600183613, 0.6482993937077484, 0.8549695002518328,
                    0.8008202545450938, ]),
     np.array([0.8360498579841501, 0.8318895234085107, 0.7174118766627045, 0.7366296519629887, 0.7986186827061038,
               0.7654119404650785, 0.7558440245972031, 0.7527648484278491, 0.7487164298180005,
               0.8623506867499545, 0.8536882411067194, 0.8709350203179484, 0.8140411624545103, 0.7838887283082292,
               0.8372194377933796, 0.8249695002518328, 0.8203008600183613, 0.6682993937077484,
               0.8008202545450938, ]),
     np.array([0.8160498579841501, 0.8018895234085107,0.7174118766627045, 0.7366296519629887, 0.7986186827061038, 0.7654119404650785, 0.7558440245972031,0.7366296519629887,0.7487164298180005,
                    0.8623506867499545, 0.8536882411067194, 0.8309350203179484, 0.8140411624545103, 0.7838887283082292, 0.8172194377933796, 0.8049695002518328,0.8203008600183613,
               0.8008202545450938,]),
     np.array([0.846427149290814, 0.8292768586794487,0.8460398145623125, 0.7940734333388412, 0.746860753757288, 0.760590073402294, 0.8377322061630761, 0.7347540625618036,
               0.8391476220901413, 0.8307452419090327, 0.8377322061630761, 0.7811180535812202, 0.7253174333428026, 0.7615220087584534, 0.7623186272957421, 0.7460466246951019]),
     np.array([0.8624234833156694, 0.8403779644268775, 0.8233363821696275, 0.8026591858445167, 0.7932764877798118, 0.8233275671983009, 0.800450500867424,
               0.8623506867499545, 0.8536882411067194, 0.8309350203179484, 0.8140411624545103, 0.7838887283082292, 0.8172194377933796, 0.8049695002518328]),
     np.array([0.8744180021624862, 0.8530160797700324, 0.8382342089728453, 0.8288267338158961, 0.8429662459453383, 0.8615244071533893, 0.803085417949148,
                    0.8321721164211283, 0.8379323999203756, 0.8177226415192571, 0.8332286347432315, 0.8225731444904776, 0.8558552903020711, 0.8432154382823138]),
     )
labels = ["10%","20%","30%","40%","50%","60%"]
plt.boxplot(x, notch=False, labels=labels, meanline=True, showmeans=True)
plt.title("数据集训练率对模型的影响箱线图")
plt.xlabel("Train Ratio", verticalalignment="top")
plt.ylabel("AUC", rotation=0, horizontalalignment="right")
# plt.savefig("./生产总值箱线图.png")
plt.show()