from mainCNN import cnn
from mainDataAugmentation import dataAugmentation
from mainTransfertLearning import transfertLearning
from mainPreTrained import preTrained

cnnAccu = cnn()
dataAugmentationAccu = dataAugmentation()
transfertLearningAccu = transfertLearning()
preTrainedAccu = preTrained()

print("accu : \n\tcnn: {}\n\tdataAugmentation: {}\n\ttransfertLearning: {}\n\tpreTrained: {}", 
      cnnAccu, dataAugmentationAccu, transfertLearningAccu, preTrainedAccu)