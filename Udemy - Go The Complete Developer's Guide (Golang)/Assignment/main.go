package main

import "fmt"

func main() {
	sliceOfInts := make([]int, 10)

	for i := 1; i < 11; i++ {
		sliceOfInts[i-1] = i
		fmt.Println(sliceOfInts[i-1])
	}

	//print(sliceOfInts[0:10])
	for _, elem := range sliceOfInts {
		if elem%2 == 0 {
			fmt.Println(elem, "is even.")
		} else {
			fmt.Println(elem, "is odd.")
		}
	}
}
