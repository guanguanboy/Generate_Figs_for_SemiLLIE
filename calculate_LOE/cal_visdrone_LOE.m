% 设置文件夹路径
folder1 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\Visdrone_Input\unlabeled_test\input'; % 替换为第一个文件夹的路径
folder2 = 'E:\科研项目\无监督的低光增强\对比方法实验结果\Ours\Visdrone\semi-LLIE(Ours)\Visdrone_ckpt_mambalowlight_rampeceptual_weight_01_0626'; % 替换为第二个文件夹的路径

% 获取文件夹中的所有图像文件
images1 = dir(fullfile(folder1, '*.jpg')); % 假设图像格式为 PNG，可根据需要修改
images2 = dir(fullfile(folder2, '*.jpg'));

% 确保两个文件夹中的文件数量相同
if length(images1) ~= length(images2)
    error('两个文件夹中的图像数量不匹配。');
end

% 初始化 LOE 值数组
LOE_values = zeros(length(images1), 1);

% 遍历每对同名图像并计算 LOE 值
for i = 1:length(images1)
    % 获取图像文件名
    imageName1 = images1(i).name;
    imageName2 = images2(i).name;
    
    % 确保图像文件名相同
    if ~strcmp(imageName1, imageName2)
        error('图像文件名不匹配: %s 和 %s', imageName1, imageName2);
    end
    
    % 读取图像
    epic = imread(fullfile(folder1, imageName1));
    ipic = imread(fullfile(folder2, imageName2));
    
    % 调用 LOE_b 函数计算 LOE 值
    LOE_values(i) = LOE_b(epic, ipic);
    % 实时打印图像名称、序号和计算出的 LOE 值
    fprintf('图像名称: %s, 序号: %d, LOE 值: %f\n', imageName1, i, LOE_values(i));
end

% 计算 LOE 值的平均值
average_LOE = mean(LOE_values);

% 输出结果
fprintf('平均 LOE 值: %f\n', average_LOE);
