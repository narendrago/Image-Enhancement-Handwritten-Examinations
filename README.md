# Image-Enhancement-Handwritten-Examinations

- Due to the onset of pandemic in 2019, all of us are now engaged in work/education **remotely**. Remote examination softwares are in the trend with features like automated submission, noise and object detection, proctoring etc.
- Students in such systems, are generally expected to upload **images** of their answer scripts, for each of the questions. Due to exam coercion and uploading device limitations (like RAM, camera quality etc.), the answer script images recieved at the evaluator's end may be blurred/shaken. This makes the evaluation process difficult and students may therefore lose deserving marks.
- The proposed system aims at developing model(s) for enhancing such images.

# KOHTD: Kazakh Offline Handwritten Text Dataset

Although digitalisation is in the trend, handwritten examinations are comfortable. There is always a need for handwritten text recognition (HTR) models to automate evaluations. It is also challenging because of the virtually infinite number of ways a letter/word can be written by the very same person. The dataset used in the study is **Kazakh offline Handwritten Text Recognition (KOHTR)** dataset, which comprises of:
- 3000 handwritten exam scripts
- &gt;140335 image segments
- ~ 922010 symbols

Paper Link: https://arxiv.org/abs/2110.04075

Dataset Link: https://github.com/abdoelsayed2016/KOHTD

# Architecture

Since not all images are blurred or have some distortion in them, we add Gaussian Blur manually. We have used Super Resolution Convolutional Neural Networks (SRCNN) to produce high resolution deblurred image from single low-resolution blurred image. The architecture is depicted below:

![srcnn_arch1](https://user-images.githubusercontent.com/60711014/166106401-1fce7e8e-1caa-43be-aec6-fabcaac7321c.png)
![srcnn_arch2](https://user-images.githubusercontent.com/60711014/166106403-46d21773-566c-432c-bfa9-2d7371a39c1f.png)

The SRCNN architecture has a total of three convolutional layers. First convolution operation has weight matrix of shape c x f1 x f1 x n1 where f1 and c refer to the number of kernels and neurons respectively. Second convolution operation has a weight matrix of shape n1  x 1 x 1 x n2. Here the kernel size is 1 x 1. Final convolution operation has a weight matrix of shape n2  x f3 x f3 x c. Among all those three convolution operations, ReLU (Rectified Linear Units) activations are applied to the first two convolution operations.

# Results Produced 

<img width="503" alt="Screenshot 2022-04-30 at 6 27 27 PM" src="https://user-images.githubusercontent.com/60711014/166106536-b4efe756-9002-4d2d-b940-80a5af13911b.png">

<img width="510" alt="Screenshot 2022-04-30 at 6 27 39 PM" src="https://user-images.githubusercontent.com/60711014/166106543-9d0be1d0-b192-4704-a2a7-3e450687c6ac.png">

<img width="520" alt="Screenshot 2022-04-30 at 6 27 49 PM" src="https://user-images.githubusercontent.com/60711014/166106552-71064864-3665-41e2-be1a-90f3e3b59841.png">
