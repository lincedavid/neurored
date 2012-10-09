set key off
set term png
set output "phase1.png"
plot 'ones.txt' u 1:2 w points pt 5 lt 1, 'zeros.txt' u 1:2 w point pt 7 lt 2

