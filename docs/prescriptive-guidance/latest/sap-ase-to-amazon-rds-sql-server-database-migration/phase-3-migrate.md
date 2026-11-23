---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sap-ase-to-amazon-rds-sql-server-database-migration/phase-3-migrate.html
---

# Phase 3: Migrate

A primary task of database migrations is to complete the migration with minimal downtime. Because both databases should use the same programming language and communication protocols, you may need to convert the code and schema for similar query syntaxes, procedures, and functions. When converting a schema, consider the following aspects:
+ Modify the database connection as appropriate for the new engine.
+ Fix any warnings and errors from the code conversion.
+ Modify table mappings and code as appropriate for the converted schema.
+ Identify and refactor any vendor-specific functionality that your application uses.

You can use any third-party migration tool for schema code conversion, such as SAP ASE database and Amazon RDS for SQL Server. You may need to convert some code manually because non-ANSI SQL is not supported in SQL Server.

After you convert the code, convert your application code or Dynamic SQL application, and then perform unit and functional testing. For more information, see [Testing Migrated Database Objects (SybaseToSQL)](https://learn.microsoft.com/en-us/sql/ssma/sybase/testing-migrated-database-objects-sybasetosql?view=sql-server-ver15).

## Converting the data
<a name="converting-the-data.08113c62-7c5a-5df1-abcf-462e3e9209f4"></a>

Transform raw data to make it more useful by cleaning, standardizing, verifying, and sorting it. In database migrations, extract, transform, and load (ETL) processes are used in the following ways:
+ Inside the database
+ With external scripts
+ Using third-party tools

Examples of ETL tools include AWS Glue, Informatica, and Talend. For migrations from SAP ASE to SQL Server, some free tools can convert stored procedures and functions automatically.

## Validating database objects
<a name="validating-database-objects.bedb4955-648f-5ab8-9a49-d970e49d4fe0"></a>

Validating your database helps prevent problems in subsequent migration stages. After code conversion, validate your database schema by comparing the following elements between SAP ASE and RDS SQL Server:
+ Schemas
+ Tables
+ Views
+ Functions
+ Stored procedure indexes
+ Triggers
+ Constraints (for example, primary keys, foreign keys, checks, and defaults)

Check that each object migrated correctly. If you find differences, identify the reason for the failure. You may need to manually create missing objects in the target database or convert Transact-SQL code. For more information, see [Validate database objects after migrating from SAP ASE to Amazon RDS for SQL Server or Microsoft SQL Server](https://aws.amazon.com/blogs/database/validate-database-objects-after-migrating-from-sap-ase-to-amazon-rds-for-sql-server-or-microsoft-sql-server/).

## Migrating data using AWS DMS
<a name="migrating-data-using-9999999999999999dms-.b00b80bb-7556-53a8-b07f-b7d4e065e2c6"></a>

If you have multiple database users, your application may need to be migrated according to a schedule. Depending on the database size and migration window, such data migrations require knowledge of full loads and incremental loads. For this reason, AWS DMS can connect source and target databases to replicate database contents according to the following processes:
+ Create a replication server.
+ Create source and target endpoints that describe data store connections.
+ Create one or more migration tasks to migrate data between source and target data stores.
+ Ongoing replication from SAP ASE to SQL Server
+ (Optional) Complete data migration from SAP ASE to SQL Server with change data capture

You may need to optimize AWS DMS for handling certain data types. For more information, see [Using an SAP ASE database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html).

## Migrating offline data
<a name="migrating-offline-data.c30b339b-01da-554a-af9e-96de65ebc764"></a>

You can use AWS Storage Gateway to integrate your SAP ASE database with Amazon Simple Storage Service (Amazon S3), which provides cost-effective, scalable, and secure storage for on-premises SAP ASE database backups. For more information, see [Integrate an SAP ASE database to Amazon S3 using AWS Storage Gateway](https://aws.amazon.com/blogs/storage/integrate-an-sap-ase-database-to-amazon-s3-using-aws-storage-gateway/).

## Using third-party tools
<a name="using-third-party-tools.ed9e4cc9-d3dc-53ab-96c3-f169e905a0e8"></a>

Some applications serve as a single point of contact (SPOC) that interfaces with other applications. When migrating to an SQL Server database platform, these interconnections may be affected, and database monitoring might require native or third-party tools that use server-specific communication protocols. It's important to assess whether these dependent applications and tools already support SQL Server or if they need modifications to function properly.

For packaged applications, consult vendors to determine if they support Amazon RDS for SQL Server. For custom applications, you may need to modify the code to ensure compatibility with the migrated database.

## Monitoring the database
<a name="monitoring-the-database.c3866831-759e-538c-ba49-bf453e5a30d8"></a>

Regardless of your chosen migration path, Amazon CloudWatch plays a role in collecting metrics, such as CPU type, memory, and I/O functions. It's also capable of setting metrics thresholds and initiating actions when thresholds are triggered.

For example, you can create alarms for Amazon RDS cluster metrics, notifications, and actions to detect and shut down unused or underutilized reader instances. Setting alarms on metrics and events can help minimize downtime and business impacts. AWS services like Amazon S3, [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/), Amazon CloudWatch, and AWS CloudTrail are already integrated with the RDS database platform, and we recommend them to monitor performance.

## Validating the data
<a name="validating-the-data.db424118-081f-5d5d-8394-35c8419fc5ed"></a>

After the data migration from SAP ASE to Amazon RDS for SQL Server is complete, validate the data to ensure accuracy and consistency. Use the following SQL queries to generate metadata statements for each table in your database.

### Step 1: Generate metadata statements and column lists
<a name="step-1--generate-metadata-statements-and-column-lists.91680588-ecd0-51c4-9430-3703110eed04"></a>

```
SELECT dt.schema_name, dt.table_name,
    STRING_AGG(dt.column_name, ',') AS column_name,
    STRING_AGG(dt.cname, ',') AS column_order
FROM (
    SELECT
        object_name(a.id) AS table_name,
        a.name colname,
        c.name col_type,
        a.isnullable,
        a.name AS cname,
        schema_name(b.uid) AS schema_name,
        CASE
            WHEN a.isnullable = 1 THEN
                CASE
                    WHEN c.name LIKE '%char%'
                        THEN 'coalesce(ltrim(rtrim('+a.name+')),''X'') as '+a.name
                    WHEN (c.name LIKE '%int%' OR c.name = 'numeric')
                        THEN 'coalesce('+a.name+',0) as '+a.name
                    WHEN c.name IN ('decimal','float','money')
                        THEN 'coalesce('+a.name+',0.0) as '+a.name
                    WHEN c.name LIKE 'datetime%'
                        THEN 'coalesce(convert(nvarchar(30),'+a.name+',112),''99991231'') as '+a.name
                    ELSE a.name
                END
            WHEN c.name LIKE 'datetime%'
                THEN 'coalesce(convert(nvarchar(30),'+a.name+',112),''99991231'') as '+a.name
            WHEN c.name LIKE '%char%'
                THEN 'coalesce(ltrim(rtrim('+a.name+')),''X'') as '+a.name
            ELSE a.name
        END AS column_name
    FROM syscolumns a
    INNER JOIN sysobjects b
        ON a.id = b.id
        AND b.type = 'U'
    INNER JOIN systypes c
        ON a.usertype = c.usertype
        AND a.xusertype = c.xusertype
        AND c.name != 'varbinary'
    INNER JOIN (
        SELECT
            OBJECT_NAME(ic.OBJECT_ID) AS table_name,
            COL_NAME(ic.OBJECT_ID, ic.column_id) AS column_name
        FROM sys.indexes AS i
        INNER JOIN sys.index_columns AS ic
            ON i.OBJECT_ID = ic.OBJECT_ID
            AND i.index_id = ic.index_id
            AND i.is_primary_key = 1
    ) pk
        ON pk.table_name = object_name(a.id)
        AND pk.column_name = a.name
) dt
GROUP BY dt.schema_name, dt.table_name;
```

The following table lists examples of outputs:

|
|
| Schema name | Table name | Column name | Column order |
| --- |--- |--- |--- |
| Person | Address | AddressID | AddressID |
| Person | AddressType | AddressTypeID | AddressTypeID |
| Person | BusinessEntity | BusinessEntityID | BusinessEntityID |
| Person | BusinessEntityAddress | BusinessEntityID, AddressID, AddressTypeID | BusinessEntityID, AddressID, AddressTypeID |

### Step 2: Generate comparison queries using the metadata results and create SELECT statements
<a name="step-2--generate-comparison-queries-using-the-metadata-results-and-create-select-statements.3bddef85-9d37-52f9-9891-7ffeb8a18284"></a>

```
SELECT <column_name>
FROM [schema_name].[table_name]
ORDER BY <column_order>;
```

The following is an example of a generated query:

```
SELECT BusinessEntityID, AddressID, AddressTypeID
FROM [Person].[BusinessEntityAddress]
ORDER BY BusinessEntityID, AddressID, AddressTypeID;
```

### Step 3: Validation
<a name="step-3--validation.cdd20b51-79c4-53ec-9644-94d3315f2066"></a>

1. Run the metadata query in both databases.

1. Generate and run `SELECT` statements for each table.

1. Compare the results between source and target databases:
   + Row counts should match.
   + Data values should be identical.
   + Check for data-type conversion issues.

### Step 4: Validate row count
<a name="step-4--validate-row-count.3c9e0313-164c-5a56-ac38-d4514a27f659"></a>

```
SELECT COUNT(1) AS total_rows
FROM [schema_name].[table_name];
```

### Step 5: Update your application's configuration to point to the new database
<a name="step-5--update-your-application-s-configuration-to-point-to-the-new-database.624179d8-8a54-5781-8994-eddd9b4045f8"></a>

1. Update the security group.

1. Modify the DNS connection string as needed to connect to the target database.

## Testing the migration
<a name="testing-the-migration.f08797b2-2978-57de-b957-36761dee3923"></a>

The testing process can help you identify overlooked issues during development, such as incorrectly converted queries or missing indexes. And it may reveal the need for database engine tuning or query modifications based on workload performance.

Functional testing, which includes unit tests for application workflows, helps to ensure seamless integration with your new database. Performance testing helps to optimize your database by verifying acceptable response times and identifying bottlenecks.

While both manual and automated testing methods exist, we recommend an automated method because it's more efficient, especially for additional testing cycles.
