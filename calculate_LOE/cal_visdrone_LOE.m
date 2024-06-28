% �����ļ���·��
folder1 = 'E:\������Ŀ\�޼ල�ĵ͹���ǿ\�Աȷ���ʵ����\Ours\Visdrone\Visdrone_Input\unlabeled_test\input'; % �滻Ϊ��һ���ļ��е�·��
folder2 = 'E:\������Ŀ\�޼ල�ĵ͹���ǿ\�Աȷ���ʵ����\Ours\Visdrone\semi-LLIE(Ours)\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0626'; % �滻Ϊ�ڶ����ļ��е�·��

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
