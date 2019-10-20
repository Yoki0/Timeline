x=[0:1:11];
y=[28133,27014,23593,29963,29410,19731,22811,24853,21189,24970,29254,20959];
plot(x,y,'-r*');
xlabel('month')
ylabel('how many years detected this month contains')
xlim([0, 12]);
set(gca,'XTick',[0:1:11]);