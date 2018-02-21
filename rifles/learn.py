from sklearn import tree
from type.gun import *

mg1 = (Gun(30,9,1000).get(),MACHINE_GUN)
mg2 = (Gun(300,10,2000).get(),MACHINE_GUN)
rifle1 = (Gun(1,4,20).get(),RIFLE)
rifle2 = (Gun(6,5,24).get(),RIFLE)
smg1=(Gun(40,2,300).get(),SMG)
at1=(Gun(1,12,1).get(),AT)
at2=(Gun(2,15,2).get(),AT)
at3=(Gun(1,7,1).get(),AT)
p1=(Gun(30,1,24).get(),PISTOL)
p2=(Gun(28,2,22).get(),PISTOL)

gun_arr=[mg1,mg2,rifle1,rifle2,smg1,at1,at2,at3,p1,p2]
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
            feature_names=['Fire rate(rpm)', 'Weight(kg)','Magazine capacity(rounds)'],
            class_names=['Machine gun','Rifle', 'SMG','Anti Tank','Pistol'])

