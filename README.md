# Preprocess for new datasets: preGOC, postGOC, or paired data 

## How to guide
Have a new file? Upload it to the corresponding folder, and job done ✅

- **preGOC**: upload it [here](https://github.com/Gaelic-Algorithmic-Research-Group/DataPipeline_Gaelic_Text/upload/main/rowdata/preGOC)
- **postGOC**: upload it [here](https://github.com/Gaelic-Algorithmic-Research-Group/DataPipeline_Gaelic_Text/upload/main/rowdata/postGOC)
- **paired data**: make sure they have the same filenames
  - preGOC: [here](https://github.com/Gaelic-Algorithmic-Research-Group/DataPipeline_Gaelic_Text/upload/main/rowdata/paired/preGOC)
  - postGOC: [here](https://github.com/Gaelic-Algorithmic-Research-Group/DataPipeline_Gaelic_Text/upload/main/rowdata/paired/postGOC)

**Output folder: https://github.com/Gaelic-Algorithmic-Research-Group/DataPipeline_Gaelic_Text/tree/main/processed**

-------
[Folder structure](https://tree.nathanfriend.io/?s=(%27options!(%27fancy9~fullPath!false~trailingSlash9~rootDot9)~J(%27J%27Main%20repo6.github*workflows8actions.yml6rowdata*480*380*284_083_06processed*48B47*38B37*2845835%27)~version!%271%27)*6--%20%200unique_name72KData8HERE_YOU_LL_FIND_PAIRED_DATA.MD3postGOC4preGOC5_BK76%5Cn-7.txt8*-9!trueBall_Jsource!Kpaired%01KJB987654320-*)
```
.
└── Main repo/
    ├── .github/
    │   └── workflows/
    │       └── actions.yml
    ├── rowdata/
    │   ├── preGOC/
    │   │   └── unique_name.txt
    │   ├── postGOC/
    │   │   └── unique_name.txt
    │   └── pairedData/
    │       ├── HERE_YOU_LL_FIND_PAIRED_DATA.MD
    │       ├── preGOC_unique_name.txt
    │       └── postGOC_unique_name.txt
    └── processed/
        ├── preGOC/
        │   └── preGOC_all_single.txt
        ├── postGOC/
        │   └── postGOC_all_single.txt
        └── pairedData/
            ├── HERE_YOU_LL_FIND_PAIRED_DATA.MD
            ├── preGOC_all_paired.txt
            └── postGOC_all_paired.txt
```

## Notes

- Training Data Shuffling (👍 gradient friendly)
- TBC

```
mkdir -p processed/postGOC
mkdir processed/preGOC
mkdir processed/pairedData
mkdir -p rowdata/pairedData
mkdir rowdata/preGOC
mkdir rowdata/postGOC
```
