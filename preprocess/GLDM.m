function [ feature ] = GLDM( image, d )
    [diff1, diff2, diff3, diff4] = AllGLD(image, d);
    
    feature = mean([
        Properties(diff1)';
        Properties(diff2)';
        Properties(diff3)';
        Properties(diff4)']);
end

function [ properties ] = Properties( diff )
    P = histcounts(reshape(diff.', 1, numel(diff))) * 1.0;
    P = P / sum(P);
    I = 0:(length(P) - 1);
    
    logN = P .* log(P);
    logN(isnan(logN)) = 0;
    
    properties = [
        mean(P .* I); % Mean
        sum(P .* I .* I); % Contrast
        sum(P .* P); % ASM
        -sum(logN); % Entropy
        sum(P ./ ((I .* I) + 1)); % IDM
        var(P .* I) % Variance
        ]; 
end
