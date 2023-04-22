scp -J e14158@tesla.ce.pdn.ac.lk localturinggihan@turing.ce.pdn.ac.lk:/storage/scratch/e14-4yp-low-light-images/logging/turing/* ../../reports/server-gpu-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk gihan@kepler.ce.pdn.ac.lk:~/logging/kepler/* ../../reports/server-gpu-util/logs/;
scp -J e14158@tesla.ce.pdn.ac.lk gihan@ai4covid.ee.pdn.ac.lk:~/logging/ai4covid/* ../../reports/server-gpu-util/logs/;
# scp -J e14158@tesla.ce.pdn.ac.lk servermonitoring@ai4covid.ee.pdn.ac.lk:~/logging/ai4covid/* ../../reports/server-gpu-util/logs/;
find ../../reports/server-gpu-util/logs/ -type f -exec sed -i 's/index/gpuid/g' {} \;
