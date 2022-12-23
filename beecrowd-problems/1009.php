<!-- Solution of: https://www.beecrowd.com.br/judge/problems/view/1009 Language: PHP -->

<?php
    $name = readline();
    $salario = (float)readline();
    $vendas  = (float)readline();
    
    $total = $salario + $vendas * 15/100;

    echo "TOTAL = R$ " . number_format($total, 2,'.', '') . "\n";
?>