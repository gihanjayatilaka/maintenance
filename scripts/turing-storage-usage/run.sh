ssh -tJ e14158@tesla.ce.pdn.ac.lk,localturinggihan@turing.ce.pdn.ac.lk,turingadmin@turing.ce.pdn.ac.lk "sudo su; ls"


"sudo su; (du -hs --threshold=10G /localhome/*; du -hs --threshold=10G /storage/scratch/*; du -hs --threshold=10G /storage/projects1/*; du -hs --threshold=10G /storage/projects2/*;) | sort -hr"

( sudo du -hs --threshold=10G /localhome/* ; sudo du -hs --threshold=10G /storage/scratch/*; sudo du -hs --threshold=10G /storage/projects1/*; sudo du -hs --threshold=10G /storage/projects2/*; ) | sort -hr



( sudo du -hs --threshold=10G /localhome/* /storage/scratch/* /storage/projects1/* /storage/projects2/*) | sort -hr

#   > temp.txt
# python gen-report.py -i temp.txt -o ../../reports/turing-storage-usage/index.html
# rm temp.txt
# echo "Done"( sudo du -hs --threshold=10G /localhome/*; sudo du -hs --threshold=10G /storage/scratch/*; sudo du -hs --threshold=10G /storage/projects1/*; sudo du -hs --threshold=10G /storage/projects2/*; ) | sort -hr