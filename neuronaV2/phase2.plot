set term png
set output "phase2.png"
m2 = 0.846904364067
b2 = 0.752050923756
m1 = 1.54706789217
b1 = -1.87590287756
condition(x) = m1*x+b1
weights(x) = m2*x+b2
plot '00.txt' u 1:2 w points pt 5 lt 2, '01.txt' u 1:2 w point pt 5 lt 4, '10.txt' u 1:2 w points pt 7 lt 3, '11.txt' u 1:2 w point pt 7 lt 1
