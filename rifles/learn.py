from sklearn import tree
from type.gun import *

mg1 = (Gun(30,100).get(),MACHINE_GUN)
mg2 = (Gun(300,120).get(),MACHINE_GUN)
rifle1 = (Gun(1,80).get(),RIFLE)
smg1=(Gun(40,30).get(),SMG)

gun_arr=[mg1,mg2,rifle1,smg1]
features=[]
labels=[]
for gun,gun_type in gun_arr:
  features.append(gun)
  labels.append(gun_type)

classifier = tree.DecisionTreeClassifier() 
classifier.fit(features, labels)

gun=get_input()
gun.print()
i_am(classifier.predict(gun.get()))


with open('dogs.dot', 'w') as dotfile:
    tree.export_graphviz(
            classifier,
            dotfile,
            feature_names=['Fire rate(rpm)', 'Weight(kg)'],
            class_names=['Machine_gun','Rifle', 'SMG'])

