#  1.代码结构

首先，代码分为三个部分：

1. 模型部分HDTR-NET，包含[原模型](https://github.com/yylgoodlucky/HDTR-Net)的所有代码
2. 测试第一部分test1，包含指标fid,niqe,psnr,ssim
3. 测试第二部分test2，包含指标lse-c,lse-d。这个指标是用[额外的网络](https://github.com/Rudrabha/Wav2Lip/tree/master/evaluation)实现的，因此单独分装。

其中，HDTR-NET为原模型，里面装有Dockerfile文件，可以方便的构建镜像。
test_file为test1的代码，包含这部分测试指标的实现，同样有Dockerfile文件。
syncnetpython为test2的代码，包含lse测试指标的实现，包含Dockerfile文件。
```
实验报告
code/              
  ├── HDTR-NET/    
  ├── test_file/     
  ├── syncnetpython/   
README
```
# 2.运行模型

首先，到[这里](https://drive.google.com/drive/folders/1IGJpQVC2fbJJASoS7bbPdt722vSvMtHr?hl=zh-cn)下载checkponit，将其放入你的本地文件夹下。在主目录里使用docker build得到镜像。之后，运行如下命令：

```
docker run --rm \
    -v /your_input:/app/input_video \
    -v /your_checkpoint:/app/checkpoint \
    -v /your_result:/app/test_result \ # 用于存放生成结果
    hdtr-net3:latest \
    python inference.py \
    --input_video ./input_video/your_video.mp4 \
    --temp_dir ./test_result \
    --model_path ./checkpoint/lip-clarity-model.pth \
    --mask_channel 6 \
    --ref_channel 3 \
    --mouth_size 96 \
    --test_batch_size 8 \
    --test_workers 4
```
模型结果将写入你本地挂载的文件夹下

# 3.运行test1

进入test_file根目录，使用docker build，生成镜像
test1需要输入模型生成的**文件夹**，运行如下命令：


```
docker run --rm \
   -v /your_test_video:/app/video \ #注意每个测试文件应该是是整个文件夹，是模型的输出结果
   test1:latest \
   python test.py \
   --path ./video/your_filefolder
```

# 4.运行test2

进入syncnetpython根目录，使用docker build生成镜像
test2需要输入*一个视频*，该视频必须是放在**一个文件夹里且该文件夹只能有该视频**
运行如下命令：

```
docker run --rm \
   -v /your_test_video:/app/testdata \
   -v /your_path/all_scores.txt:/app/all_scores.txt \ #结果将写入你本地挂载的txt
   test2:latest \
   sh -c "pip install --upgrade scenedetect && sh calculate_scores_real_videos.sh /app/testdata"
```
# 5.补充说明

- 镜像文件太大了，百度网盘传不上去（
- 如果无法构建，可以联系[我](mailto:3557458017@qq.com)发给你镜像文件
