package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, err := os.Open("in.txt")
	if err != nil {
		log.Fatal(err)
	}

	sum := 0
	
	scanner := bufio.NewReader(f)
	


}
