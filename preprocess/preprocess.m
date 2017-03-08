rng(10);
close all;
clear all;
files = dir('dataset');
features = [];
for i = 3 : length(files)
    image = imread(strcat('dataset/', files(i).name));
    features = [features; GLDM(image,7)];
end

features = zscore(features); 