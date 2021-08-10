clc,clear, close all

figure;
for i = 0:10:1000
    t = 0.1*i;
    cd POS;
    pos = dlmread(string(i)+ '.txt');
    cd ../VEL
    vel = dlmread(string(i)+ '.txt');
    cd ..
    p1 = [pos(1,1); pos(1,2)];
    p2 = [pos(2,1);pos(2,2)];
    
    v1 = [vel(1,1); vel(1,2)];
    v2 = [vel(2,1); vel(2,2)];

    subplot(2,1,1)
    plot(p1(1),p1(2),'ro')
    hold on
    plot(p2(1),p2(2),'bo')
    xlim([-1000 1000]), ylim([-1000 1000])
    
    subplot(2,1,2)
    hold on
    plot(t, sqrt(v1(1)^2+v1(2)^2), 'r.')
    
%     hold off
    
   
     pause(0.1)
end