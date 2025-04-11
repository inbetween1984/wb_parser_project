package fetcher

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	pb "wb_parser_project/parser/wbparser"
)

type PriceResponse struct {
	Data struct {
		Products []struct {
			Name  string `json:"name"`
			Sizes []struct {
				Price struct {
					Product int `json:"product"`
				} `json:"price"`
			} `json:"sizes"`
		} `json:"products"`
	} `json:"data"`
}

func FetchPrice(nmID int32) *pb.ProductResponse {
	url := fmt.Sprintf("https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-4039474&spp=30&nm=%d", nmID)
	client := &http.Client{}
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return &pb.ProductResponse{NmId: nmID, Error: err.Error()}
	}

	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")

	resp, err := client.Do(req)
	if err != nil {
		return &pb.ProductResponse{NmId: nmID, Error: err.Error()}
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return &pb.ProductResponse{NmId: nmID, Error: err.Error()}
	}

	var priceResp PriceResponse
	if err := json.Unmarshal(body, &priceResp); err != nil {
		return &pb.ProductResponse{NmId: nmID, Error: err.Error()}
	}

	if len(priceResp.Data.Products) == 0 {
		return &pb.ProductResponse{NmId: nmID, Error: "product not found"}
	}

	product := priceResp.Data.Products[0]
	price := float32(product.Sizes[0].Price.Product) / 100

	return &pb.ProductResponse{
		NmId:  nmID,
		Price: price,
		Name:  product.Name,
	}
}
