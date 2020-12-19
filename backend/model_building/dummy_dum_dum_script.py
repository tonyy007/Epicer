import matplotlib.pyplot as plt

data = "- 42s - loss: 13.9206 - accuracy: 0.7955 - val_loss: 0.4410 - val_accuracy: 0.9478 \n\
       Epoch 2/30 - 41s - loss: 1.0656 - accuracy: 0.8092 - val_loss: 0.1706 - val_accuracy: 0.9809\n\
Epoch 3/30 - 41s - loss: 0.4555 - accuracy: 0.8831 - val_loss: 0.0646 - val_accuracy: 0.9896\n\
Epoch 4/30 - 43s - loss: 0.4303 - accuracy: 0.9160 - val_loss: 0.7240 - val_accuracy: 0.9541\n\
Epoch 5/30 - 42s - loss: 0.6047 - accuracy: 0.9253 - val_loss: 1.1173e-04 - val_accuracy: 0.9974\n\
Epoch 6/30 - 41s - loss: 0.2671 - accuracy: 0.9497 - val_loss: 0.0047 - val_accuracy: 0.9834\n\
Epoch 7/30 - 41s - loss: 0.4149 - accuracy: 0.9626 - val_loss: 0.0352 - val_accuracy: 0.9870\n\
Epoch 8/30 - 41s - loss: 0.1698 - accuracy: 0.9701 - val_loss: 2.8491e-05 - val_accuracy: 0.9885\n\
Epoch 9/30 - 42s - loss: 0.2699 - accuracy: 0.9787 - val_loss: 0.2060 - val_accuracy: 0.9831\n\
Epoch 10/30 - 41s - loss: 0.4146 - accuracy: 0.9512 - val_loss: 8.9341e-04 - val_accuracy: 0.9873\n\
Epoch 11/30 - 42s - loss: 0.3335 - accuracy: 0.9636 - val_loss: 0.0078 - val_accuracy: 0.9987\n\
Epoch 12/30 - 41s - loss: 0.2259 - accuracy: 0.9675 - val_loss: 1.2640e-09 - val_accuracy: 0.9580\n\
Epoch 13/30 - 41s - loss: 0.2727 - accuracy: 0.9732 - val_loss: 0.0045 - val_accuracy: 0.9584\n\
Epoch 14/30 - 43s - loss: 0.8807 - accuracy: 0.9614 - val_loss: 0.5680 - val_accuracy: 0.9847\n\
Epoch 15/30 - 41s - loss: 0.1883 - accuracy: 0.9827 - val_loss: 2.0133e-09 - val_accuracy: 0.9870\n\
Epoch 16/30 - 40s - loss: 0.7497 - accuracy: 0.9717 - val_loss: 0.1548 - val_accuracy: 0.9605\n\
Epoch 17/30 - 41s - loss: 0.2474 - accuracy: 0.9782 - val_loss: 0.0000e+00 - val_accuracy: 0.9857\n\
Epoch 18/30 - 41s - loss: 0.3474 - accuracy: 0.9706 - val_loss: 2.1563 - val_accuracy: 0.9389\n\
Epoch 19/30 - 41s - loss: 0.4036 - accuracy: 0.9792 - val_loss: 0.0566 - val_accuracy: 0.9338\n\
Epoch 20/30 - 41s - loss: 0.2988 - accuracy: 0.9747 - val_loss: 0.0135 - val_accuracy: 0.9805\n\
Epoch 21/30 - 40s - loss: 0.8856 - accuracy: 0.9853 - val_loss: 0.1906 - val_accuracy: 0.9834\n\
Epoch 22/30 - 41s - loss: 0.4154 - accuracy: 0.9681 - val_loss: 4.5574e-05 - val_accuracy: 0.9844\n\
Epoch 23/30 - 40s - loss: 0.3869 - accuracy: 0.9756 - val_loss: 0.0193 - val_accuracy: 0.9363\n\
Epoch 24/30 - 40s - loss: 0.2967 - accuracy: 0.9736 - val_loss: 0.4558 - val_accuracy: 0.9831\n\
Epoch 25/30 - 40s - loss: 1.9739 - accuracy: 0.9762 - val_loss: 5.8395e-11 - val_accuracy: 0.9873\n\
Epoch 26/30 - 40s - loss: 0.2524 - accuracy: 0.9842 - val_loss: 0.1369 - val_accuracy: 0.9351\n\
Epoch 27/30 - 42s - loss: 3.4847 - accuracy: 0.9782 - val_loss: 1.4859e-05 - val_accuracy: 0.9325\n\
Epoch 28/30 - 42s - loss: 0.8974 - accuracy: 0.9746 - val_loss: 1.7249 - val_accuracy: 0.9753\n\
Epoch 29/30 - 41s - loss: 0.1464 - accuracy: 0.9787 - val_loss: 0.0044 - val_accuracy: 0.9796\n\
Epoch 30/30 - 41s - loss: 0.4697 - accuracy: 0.9696 - val_loss: 0.0043 - val_accuracy: 0.9494"

train_reports = [float(report.split('loss: ')[1].split(' - accuracy')[0]) for report in data.split('\n')]
test_reports = [float(report.split('val_loss: ')[1].split(' - val_accuracy')[0]) for report in data.split('\n')]

plt.plot(train_reports, label='Train')
plt.plot(test_reports, label='Validation')

plt.legend()
plt.xlabel('Epochs')
plt.ylabel('loss function')

plt.show()