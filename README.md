# maintenance
This repository contains the scripts and instructions for cepdnaclk github organization maintainance.

User the following folder structure to organize the scripts and their outputs.

## Folder structure
```
scripts/
├── scrpit1/
│   ├── script1.sh
reports/
├── scrpit1/
|   ├── index.html
```

## Summary

|                       |Code                                     |Report             |
|-----------------------|-----------------------------------------|-------------------|
|Server storage usage   |[github](./scripts/server-storage-util/) |[url](https://cepdnaclk.github.io/maintenance/reports/server-storage-util/)|
|Server GPU usage       |[github](./scripts/server-gpu-util/)     |[url](https://cepdnaclk.github.io/maintenance/reports/server-gpu-util/plots/)|




## TO DO
1. Server storage usage
To do: Take storage allowances into account when generating the report. (e.g.: projects could be allowed to grow to X GB, but not more than that.)
To do: Integrate this into the Department API.

2. Server GPU Utilization
To do: Integrate this into the Department API.