package main

import "fmt"

const globalConstant = 2.72
const ExportedGlobalConstant = 3.14

func main() {
  var first string
  first = "This is first string"
  
  var second = "This is second string"
  
  third := "This is third string"
  
  fmt.Println(first, second, third)
}