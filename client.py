import grpc
import calculator_pb2,calculator_pb2_grpc



#step 1 : Create Channel

channel = grpc.insecure_channel('localhost:80')

#step 2 : Create Stub

stub = calculator_pb2_grpc.CalculatorStub(channel)

#step 3 : API call

number =calculator_pb2.Number(value=-1)
response = stub.SqureRoot(number)
print(response.value)





