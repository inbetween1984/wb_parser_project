@echo off
echo Generating Protobuf code for Go and Python...

echo Generating Go code...
protoc --go_out=parser --go-grpc_out=parser proto/wb_parser.proto
if %ERRORLEVEL% NEQ 0 (
    echo Failed to generate Go code
    exit /b %ERRORLEVEL%
)

echo Generating Python code...
python -m grpc_tools.protoc -Iproto --python_out=api --grpc_python_out=api proto/wb_parser.proto
if %ERRORLEVEL% NEQ 0 (
    echo Failed to generate Python code
    exit /b %ERRORLEVEL%
)

echo Protobuf code generated successfully!