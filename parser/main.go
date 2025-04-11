package main

import (
	"context"
	"log"
	"net"
	"sync"

	"google.golang.org/grpc"
	"wb_parser_project/parser/internal/fetcher"
	pb "wb_parser_project/parser/wbparser"
)

type server struct {
	pb.UnimplementedWBParserServer
}

func (s *server) GetPrice(ctx context.Context, req *pb.BatchRequest) (*pb.BatchResponse, error) {
	results := make([]*pb.ProductResponse, len(req.NmIds))
	var wg sync.WaitGroup

	for i, nmID := range req.NmIds {
		wg.Add(1)
		go func(i int, nmID int32) {
			defer wg.Done()
			results[i] = fetcher.FetchPrice(nmID)
		}(i, nmID)
	}
	wg.Wait()

	return &pb.BatchResponse{Results: results}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterWBParserServer(s, &server{})
	log.Printf("gRPC server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
