function [ diff ] = GLD( image, vector, d )
    min1 = abs(min(vector, vector*0) * d) + 1;
    max1 = abs(max(vector, vector*0) * d) + 1;
    min2 = size(image) - max1;
    max2 = size(image) - min1;
    
    image1 = image(min1(1):min2(1), min1(2):min2(2));
    image2 = image(max1(1):max2(1), max1(2):max2(2));
    
    diff = abs(image2 - image1);
end

