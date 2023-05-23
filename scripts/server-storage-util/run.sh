#rm temp.txt
#(sudo du -hs --threshold=10G /localhome/*;\
#sudo du -hs --threshold=10G /storage/scratch/*;\
#sudo du -hs --threshold=10G /storage/projects1/*;\
#sudo du -hs --threshold=10G /storage/projects2/*;\
#) | sort -hr > temp.txt
./download-logs.sh
python gen-report.py -o ../../reports/server-storage-util/index.html
echo "Done"


