set term png
set output "phase2.png"
plot '00.txt' u 1:2 w points pt 5 lt 2, '01.txt' u 1:2 w point pt 5 lt 4, '10.txt' u 1:2 w points pt 7 lt 3, '11.txt' u 1:2 w point pt 7 lt 1
