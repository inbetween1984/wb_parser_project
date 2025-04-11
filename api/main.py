import grpc
from fastapi import FastAPI
from typing import List, Union, Dict

import wb_parser_pb2
import wb_parser_pb2_grpc
from models.schemas import BatchRequest, ProductResponse

import time

app = FastAPI()

@app.post("/api/track/batch")
async def track_batch(request: BatchRequest) -> List[Union[ProductResponse, Dict]]:
    with grpc.insecure_channel('parser:50051') as channel:
        stub = wb_parser_pb2_grpc.WBParserStub(channel)
        try:
            start_time = time.time()
            response = stub.GetPrice(wb_parser_pb2.BatchRequest(nm_ids=request.nm_ids))
            results = []
            for item in response.results:
                if item.error:
                    results.append({"nm_id": item.nm_id, "error": item.error})
                else:
                    results.append(ProductResponse(nm_id=item.nm_id, price=item.price, name=item.name))
            print(time.time() - start_time)
            return results
        except Exception as e:
            print(time.time() - start_time)
            return [{"nm_id": nm_id, "error": str(e)} for nm_id in request.nm_ids]