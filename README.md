
# Tumor growth prediction via Conditional Recurrent Variantional Auto-Encoder(CRVAE).  

The prediction of lung tumor growth is the key to early treatment of lung cancer. However, the lack of intuitive and clear judgments about the future development of the tumor often leads patients to miss the best treatment opportunities. Combining the characteristics of variational autoencoder and recurrent neural networks, this paper propose a tumor growth prediction via Conditional Recurrent Variational Autoencoder. The proposed model uses variational autoencoder to reconstruct tumor images at different times. Meanwhile, the recurrent units are proposed to infer the relationship between tumor images according to chronological order. The different tumor development varies in different patients, patients’ condition is adopted to achieve personalized prediction. 
![Figure1](https://user-images.githubusercontent.com/30771950/127951579-14640adf-4402-4d7d-89d9-152d53547b3d.jpg)
## Prepare

``tensorflow,
numpy,
matplotlib``

## Implementation 
1. cd to main directory. 

2. ``jupyter notebook``

3. run  ``CRVAE.ipynb``


## Appendix


You can obtain your custom data by modifying the file ``creatMnist.py ``.

The source sees  https://github.com/LukeZhuang/IVRAE.

# Results
![Figure6](https://user-images.githubusercontent.com/30771950/127951637-c5f2de95-c872-46df-affc-9e68eebd5731.jpg)


