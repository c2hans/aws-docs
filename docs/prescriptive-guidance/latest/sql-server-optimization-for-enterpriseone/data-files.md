---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/data-files.html
---

# Add and balance data files
<a name="data-files"></a>

The SQL Server databases provided with EnterpriseOne can often benefit from additional files. Additional files enable optimal balancing across storage and processor cores. Balancing the files is a multi-step process. Many of these steps require exclusive access to the database objects, so you would have to take EnterpriseOne and other systems accessing the database offline.

1. Complete file sizing calculations.

1. Create new files.

1. Temporarily empty the MDF file.

1. Resize the MDF file.

1. Clean up.

1. Validate the results.

## Complete file sizing calcuations
<a name="file-size"></a>

To find the appropriate size of the database files, start by examining the size of the current ROW data by using the following query.

```
USE JDE_PRIST920
SELECT SUM(CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0) AS SpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS'
```

Then complete the following calculations and fill out the *Your value* column:

|
|
| Line | Name | Example | Your value | Description |
| --- |--- |--- |--- |--- |
| **1** | Current size of the row | 1 TB |  | The results from the previous query. |
| **2** | Planned growth | 20% |  | Expected growth over the next number of months, including a safety margin. |
| **3** | Required size | 1.2 TB |  | Line 1 multiplied by line 2. |
| **4** | Number of files | 8 |  | The number of files targeted. |
| **5** | Size per file | 150 GB |  | Line 3 divided by line 4. |
| **6** | Autogrowth percentage | 10% |  | The size for automatic growth. For minimum fragmentation, 10% is a good target. |
| **7** | Autogrowth size | 15 GB |  | Line 5 multiplied by line 6. |

## Create new files
<a name="new-files"></a>

Use the following script as a template to add files to the database. Modify the following parameters:
+ Change `JDE-PRIST920` to the name of the database you want to add files to.
+ For `NAME`, specify the logical name of each file you want to add.
+ For `FILENAME`, specify the physical name of each file you want to add.
+ For `FILEGROWTH`, use the value you calculated in row 7 of the previous table.
+ For `SIZE`, specify the value from row 5 of the previous table.

```
USE master;
GO

ALTER DATABASE JDE_PRIST920
MODIFY FILE (NAME = JDE_PRIST920_Data, FILEGROWTH = 15GB);
GO

ALTER DATABASE JDE_PRIST920
ADD FILE
(NAME = JDE_PRIST920_Data2, FILENAME = 'M:\DATA\PRIST920_Data2.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data3, FILENAME = 'M:\DATA\PRIST920_Data3.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data4, FILENAME = 'M:\DATA\PRIST920_Data4.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data5, FILENAME = 'M:\DATA\PRIST920_Data5.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data6, FILENAME = 'M:\DATA\PRIST920_Data6.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data7, FILENAME = 'M:\DATA\PRIST920_Data7.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_Data8, FILENAME = 'M:\DATA\PRIST920_Data8.ndf', SIZE=150GB, FILEGROWTH = 15GB),
(NAME = JDE_PRIST920_TEMP, FILENAME = 'M:\DATA\PRIST920_TEMP.ndf', SIZE=150GB, FILEGROWTH = 15GB)
GO
```

## Temporarily empty the MDF file
<a name="empty-mdf"></a>

When the files have been created, migrate the data from the MDF to the NDF files by running the following command for each file. Adjust the file names to reflect the file names in your database.

```
USE JDE_PRIST920
DBCC SHRINKFILE (JDE_PRIST920_Data, EMPTYFILE)
```

The `EMPTYFILE `command generates an error because some content can't be moved to an NDF file. You can ignore this error message.

![Error message when emptying the MDF file](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/images/guide-img/1ded277e-59b3-4f6d-bcef-fa7d04f06c63/images/1e9a4313-7b87-4902-8a15-0cc341db2e6e.png)

## Resize the MDF file
<a name="resize-mdf"></a>

To reduce the size of the MDF file to the target size, run the following command. Adjust the file size to reflect the value from line 5 of the calculation in the table.

```
JDE_PRIST920
DBCC SHRINKFILE (JDE_PRIST920_Data, 150000);
```

Occasionally, the `SHRINKFILE` command will fail because of the placement of content that couldn't be moved to an NDF file. In this case, you might need to run the `DBCC DBREINDEX` command, rerun the process to empty the file, and try the `SHRINKFILE` operation again.

## Clean up
<a name="cleanup"></a>

When the target files have been created and the MDF file is correctly sized, use the following command to migrate the data from the TEMP file back to the MDF file. Adjust the file names to reflect the file names in your database.

```
DBCC SHRINKFILE (JDE_PRIST920_TEMP, EMPTYFILE)
```

When the file is empty, you can remove it by using the following command:

```
ALTER DATABASE JDE_PRIST920;
REMOVE FILE JDE_PRIST920_TEMP;
```

## Validate results
<a name="validate"></a>

To check the current disk space utilization of the database after balancing, run the following scripts.

```
USE JDE_PRIST920
SELECT DB_NAME() AS DbName,
    type_desc,
    CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS SpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS';

SELECT SUM(CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0) AS TotalSpaceUsedMB
FROM sys.database_files
WHERE type IN (0,1)
AND type_desc = 'ROWS'
```

The output should be similar to the following. The files will seldom be perfectly balanced, because some content can exist only in the MDF file.

![Validating disk space utilization after balancing](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/images/guide-img/1ded277e-59b3-4f6d-bcef-fa7d04f06c63/images/175af9bb-4a1f-4779-871b-e695e291cec0.png)
