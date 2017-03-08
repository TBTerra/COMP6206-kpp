function [ dir1, dir2, dir3, dir4 ] = AllGLD( image, d )
    dir1 = GLD(image, [1 1], d);
    dir2 = GLD(image, [1 -1], d);
    dir3 = GLD(image, [1 0], d);
    dir4 = GLD(image, [0 1], d);
end
