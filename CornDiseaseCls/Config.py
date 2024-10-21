#coding:utf-8


# 使用的模型路径
model_path = 'models/best.pt'

names = {0: 'common rust', 1: 'gray leaf spot', 2: 'healthy', 3: 'northern leaf blight'}

CH_names = ['锈病','灰叶斑病','健康','枯叶病']

method_infos = {'锈病':'在玉米锈病的发病初期用药防治。25%三唑酮可湿性粉剂1500—2000倍液后、50%多菌灵可湿性粉剂500—1000倍液、20%萎锈灵乳油400倍液、40%福星乳剂9000倍液、50%胶体硫200倍液喷雾。7-10天一次，连续防治2-3次。',
                '灰叶斑病':'2',
                  '健康':'无',
                '枯叶病':'1',}