rm ../../reports/server-gpu-util/logs/*.jpeg;
./download-logs.sh
python generate-graphs.py