// Solution of: https://www.beecrowd.com.br/judge/problems/view/1004 Language: Go

package main

import "fmt"

func main() {

	var f1 int
	var f2 int
	var prod int

	fmt.Scanf("%d", &f1)
	fmt.Scanf("%d", &f2)

	prod = f1 * f2
	fmt.Printf("PROD = %d\n", prod)
}