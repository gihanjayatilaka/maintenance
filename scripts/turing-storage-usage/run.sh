rm temp.txt
(sudo du -hs --threshold=10G /localhome/*;\
sudo du -hs --threshold=10G /storage/scratch/*;\
sudo du -hs --threshold=10G /storage/projects1/*;\
sudo du -hs --threshold=10G /storage/projects2/*;\
) | sort -hr > temp.txt
python gen-report.py -i temp.txt -o ../../reports/turing-storage-usage/index.html
rm temp.txt
echo "Done"


