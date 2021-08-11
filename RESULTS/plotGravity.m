clc,clear, close all
cd POS;
pos = dlmread(string(0)+ '.txt');
cd ..
n_planet = length(pos);

figure;
for i = 0:10:3900
    t = 0.1*i;
    cd POS;
    pos = dlmread(string(i)+ '.txt');
    cd ../VEL
    vel = dlmread(string(i)+ '.txt');
    cd ..
    for j = 1:n_planet
        p(:,j) = [pos(j,1); pos(j,2)];
    end
  
    
    v1 = [vel(1,1); vel(1,2)];
    v2 = [vel(2,1); vel(2,2)];
    
%     subplot(2,1,1)
    for j = 1:n_planet
        plot(p(1,j),p(2,j),'o')
        hold on
    end
    axis equal
    hold off

    xlim([-2200 2200]), ylim([-2200 2200])
    
%     subplot(2,1,2)
%     hold on
%     plot(t, sqrt(v1(1)^2+v1(2)^2), 'r.')
    
    
    
   
     pause(0.1)
end