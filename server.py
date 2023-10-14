try:
    import grpc
    from concurrent import futures
    import time
    import calculator
    import calculator_pb2,calculator_pb2_grpc
except Exception as e:
    print("error while loading modules")
    
    
class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def SqureRoot(self,request,context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response
_ONE_DAY_IN_SECONDS = 300000
def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    print('starting server. Listeing on Port 80.')
    server.add_insecure_port('[::]:80')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()