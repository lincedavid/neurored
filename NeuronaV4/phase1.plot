set term png
set output "phase1.png"
plot 'ones.txt' u 1:2 w points pt 5 lt 1, 'zeros.txt' u 1:2 w point pt 7 lt 2, ((3.0106484177635808 - 3.5380880259871601*(x)) / (-2.5610224499454608)) with lines lw 1 lt 3 title "Condicion"

