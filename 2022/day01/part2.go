package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	var cal int = 0
	var calMax int = 0
	var calSecondMax int = 0
	var calThirdMax int = 0

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			if cal > calMax {
				calThirdMax = calSecondMax
				calSecondMax = calMax
				calMax = cal
			} else if cal > calSecondMax {
				calThirdMax = calSecondMax
				calSecondMax = cal
			} else if cal > calThirdMax {
				calThirdMax = cal
			}
			cal = 0
		}
		cal += x
	}
	fmt.Println(calMax, calSecondMax, calThirdMax)
}
