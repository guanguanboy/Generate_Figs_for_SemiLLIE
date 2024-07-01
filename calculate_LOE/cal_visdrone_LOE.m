% �����ļ���·��
folder1 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\Visdrone_Input\unlabeled_test\input'; % 替换为第一个文件夹的路径
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\semi-LLIE(Ours)\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0626'; % 替换为第二个文件夹的路径
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Retinexformer\LOL_v1_visdrone\LOL_v1\RetinexFormer_Visdrone_labeled\net_g_latest'; % 替换为第二个文件夹的路径
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\URentinexNet\visdrone_unlabeled_test_with_URetinexNet\visdrone_unlabeled_test'; % 替换为第二个文件夹的路径
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\EnlightenGAN\test_190\images_jpg';
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\NeRCo\NeRCo_visdrone_results\pretrained_models\LSRW\test_latest\images_jpg';
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\RUAS\result_RUAS\result';
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\RetinexNet\visdrone_unlabeld_test_RetinexNet\visdrone_unlabeld_test_jpg';
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\SNR-Net\formated_LOLv1_model_on_visdrone_unlabeled_test\formated_LOLv1_model\images\output';
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\MIRNetv2\Lol_visdrone_MIRNetv2\Lol_jpg';

%Restormer
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Restormer\visdrone_results_Restormer\visdrone';

%Semi-LLIE ablation
%folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\semi-LLIE(Ours)\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0628_01_ganloss';
folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\semi-LLIE(Ours)\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0628_10_ganloss_results\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0628_10_ganloss';


% ��ȡ�ļ����е�����ͼ���ļ�
images1 = dir(fullfile(folder1, '*.jpg')); % ����ͼ���ʽΪ PNG���ɸ�����Ҫ�޸�
images2 = dir(fullfile(folder2, '*.jpg'));

% ȷ�������ļ����е��ļ�������ͬ
if length(images1) ~= length(images2)
    error('�����ļ����е�ͼ��������ƥ�䡣');
end

% ��ʼ�� LOE ֵ����
LOE_values = zeros(length(images1), 1);

% ����ÿ��ͬ��ͼ�񲢼��� LOE ֵ
for i = 1:length(images1)
    % ��ȡͼ���ļ���
    imageName1 = images1(i).name;
    imageName2 = images2(i).name;
    
    % ȷ��ͼ���ļ�����ͬ
    if ~strcmp(imageName1, imageName2)
        error('ͼ���ļ�����ƥ��: %s �� %s', imageName1, imageName2);
    end
    
    % ��ȡͼ��
    epic = imread(fullfile(folder1, imageName1));
    ipic = imread(fullfile(folder2, imageName2));
    
    % ���� LOE_b �������� LOE ֵ
    LOE_values(i) = LOE_b(epic, ipic);
    % ʵʱ��ӡͼ�����ơ���źͼ������ LOE ֵ
    fprintf('ͼ������: %s, ���: %d, LOE ֵ: %f\n', imageName1, i, LOE_values(i));
end

% ���� LOE ֵ��ƽ��ֵ
average_LOE = mean(LOE_values);

% ������
fprintf('ƽ�� LOE ֵ: %f\n', average_LOE);
