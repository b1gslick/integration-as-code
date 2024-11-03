package main

import (
	"crypto/sha256"
	"encoding/hex"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	// Define routes
	router.POST("/hash", requestCalculate)

	host := os.Getenv("host")
	port := os.Getenv("port")

	log.Println("Starting server")
	// Start the server
	log.Fatal(router.Run(host + ":" + port))
}

type Income struct {
	Data string `json:"data"`
}

func requestCalculate(c *gin.Context) {
	var income Income
	if err := c.BindJSON(&income); err != nil {
		return
	}
	value := calculate(income.Data)

	c.IndentedJSON(http.StatusCreated, value)
}

func calculate(t string) string {
	h := sha256.New()

	h.Write([]byte(t))

	bs := h.Sum(nil)

	return hex.EncodeToString(bs)
}
