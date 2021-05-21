package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Book struct {
	Id       string `json:"id"`
	Title    string `json:"title"`
	Category string `json:"category"`
	Author   string `json:"author"`
}

var Books []Book

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcomey human")
	fmt.Println("EOP")
}

func returnAllBooks(w http.ResponseWriter, r *http.Request) {
	fmt.Println("return all articles method")
	json.NewEncoder(w).Encode(Books)
}

func handleRequest() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/books", returnAllBooks)
	log.Fatal(http.ListenAndServe(":2000", nil))
}

func main() {
	Books = []Book{
		{Title: "Ponniyin selvan", Category: "Historical fiction", Author: "Kalki"},
		{Title: "Secret", Category: "Self Help", Author: "Rhonda bryne"},
	}
	handleRequest()
}
