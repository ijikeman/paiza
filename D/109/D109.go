package main

import (
	"os"
	"fmt"
	"bufio"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	input_array := strings.Split(strings.Replace(sc.Text(), " ", "", 1), "") // 1文字ずつ分割して配列に格納
	if len(array_uniq(input_array)) == 1 {
	    fmt.Println("Yes")
	} else {
	    fmt.Println("No")
	}
}

func array_uniq(args []string) []string {
    results := make([]string, 0, len(args))
    encountered := map[string]bool{}
    for i := 0; i < len(args); i++ {
        if !encountered[args[i]] {
            encountered[args[i]] = true
            results = append(results, args[i])
        }
    }
    return results
}