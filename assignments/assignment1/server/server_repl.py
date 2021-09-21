import grpc
import sys
# setting path
sys.path.append('..')
from assignments.assignment1 import replicate_pb2
from assignments.assignment1 import replicate_pb2_grpc
from concurrent import  futures
from assignments.assignment1 import  mongo

class ReplicatePostgresToMongodbService(replicate_pb2_grpc.ReplicatePostgresToMongodbServicer):
    def __init__(self, *args, **kwargs):
        pass

    def StreamToServer(self, request, context):
        message = request.message
        print(message)
        # Call mongo class method here
        result = mongo.generateJson(message)
        response = {'messageResponse': result, 'completed': True}
        return replicate_pb2.Response(**response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    replicate_pb2_grpc.add_ReplicatePostgresToMongodbServicer_to_server(ReplicatePostgresToMongodbService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()