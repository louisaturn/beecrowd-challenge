(* Solution of: https://www.beecrowd.com.br/judge/problems/view/1007 Language: OCaml*)

Scanf.scanf "%i %i %i %i" (fun A B C D ->
    Printf.printf "DIFERENCA = %d\n" (A*B - C*D)
    )
