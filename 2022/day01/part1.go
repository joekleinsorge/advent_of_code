package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// var highest int
	// var sum int

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan(){
		fmt.Println(scanner.Text())
		// num, _ := strconv.Atoi(line)
		// sum += num
		// if sum > highest {
		// 	highest = sum
		// }
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
}
