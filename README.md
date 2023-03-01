# maintenance
This repository contains the scripts and instructions for cepdnaclk github organization maintainance.

User the following folder structure to organize the scripts and their outputs.

## Folder structure
```
scripts/z
├── scrpit1/
│   ├── script1.sh
reports/
├── scrpit1/
|   ├── index.html
```

## Maintenace scripts

1. Turing storage usage

This script will generate a [report](https://cepdnaclk.github.io/maintenance/reports/turing-storage-usage/) about the storage usage of the Turing server (for all folders that are larger than 10G).
To do: Take storage allowances into account when generating the report. (e.g.: projects could be allowed to grow to X GB, but not more than that.)