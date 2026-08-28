---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/assess-environment.html
---

# Assessing your environment
<a name="assess-environment"></a>

To assess your SQL Server environment and find out whether your Enterprise SQL Server instance is using Enterprise feature, you can take one of the following approaches:
+ Using a T-SQL script
+ Using the AWS SCT tool

## Using a T-SQL script  to assess a SQL Server database
<a name="using-a-t-sql-script--to-assess-a-sql-server-database.672e88e7-12ce-567c-bf58-028ce6ebc965"></a>

To determine whether your Microsoft SQL Server database uses Enterprise edition-specific features, you can run the following T-SQL statement in SQL Server  Management Studio (SSMS).

```
IF (SELECT SERVERPROPERTY('EngineEdition')) = 2
    SELECT 'This is already a Standard SQL Server Edition instance!' AS Status
ELSE
    BEGIN
        --Checking Enterprise features
        CREATE TABLE ##EntFeatures ( dbid int, db_name SYSNAME, feature_name VARCHAR(100))
        EXEC sp_msforeachdb
        N' USE [?]
        IF (SELECT COUNT(*) FROM sys.dm_db_persisted_sku_features) >0
        BEGIN
           INSERT INTO ##EntFeatures
            SELECT db_id(),dbname=DB_NAME(),feature_name FROM sys.dm_db_persisted_sku_features
        END '
        IF (SELECT COUNT(1) FROM ##EntFeatures WHERE dbid>4) >0
            SELECT db_name,feature_name FROM   ##EntFeatures;
        ELSE
            SELECT CONCAT('Ready to move! You are running a(n) ', CONVERT(VARCHAR,SERVERPROPERTY('Edition')),' and are not using any Enterprise features') AS Status
    END

IF OBJECT_ID('tempdb.dbo.##EntFeatures') IS NOT NULL
DROP TABLE ##EntFeatures
```

If the script returns a single row with the message **Ready to move\! You are running a(n) <your SQL Sever edition>**, as shown in the following screen illustration, your SQL Server database can be a candidate for downgrading from Enterprise edition to Standard edition.

![Status message indicating that there are no dependencies.](http://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/images/guide-img/4f72b44a-289d-4c64-8325-b36e4aec7488/images/766828e8-e2d2-41c9-b188-903268a0effe.png)

If the script returns a list of databases and Enterprise edition features, you must evaluate the possible consequences of removing Enterprise features from those databases.

![Script results listing databases that have dependencies on Enterprise edition.](http://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/images/guide-img/4f72b44a-289d-4c64-8325-b36e4aec7488/images/637eea90-9c4a-48a4-90d4-550cf7bf55f5.png)

## Using AWS SCT to assess a SQL Server database
<a name="using-aws-sct-to-assess-a-sql-server-database.ae323d93-77c1-5643-9544-c1e20eeb0c92"></a>

When you create a database migration assessment report in AWS SCT, the **License Evaluation and Cloud Support** section of the report lists the SQL Server features that your source database is using. You can use this list to make an informed decision while migrating to Amazon RDS for SQL Server.

![List of dependencies that need to be removed before downgrading and features that cannot be supported after downgrading.](http://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/images/guide-img/4f72b44a-289d-4c64-8325-b36e4aec7488/images/164750ba-6d2f-4eeb-ba6c-12324ff68c76.png)

## Scaling the SQL Server assessment
<a name="scaling-the-sql-server-assessment.ecfeacc5-c323-51dc-b9f3-04ca9fbe5892"></a>

AWS SCT now supports batch assessment using the [multiserver assessor](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html#CHAP_AssessmentReport.Multiserver.Agreggated) to evaluate multiple servers based on input that you provide for each schema definition that you want to assess. Your schema definition contains database server connection parameters and the full name of each schema. After assessing each schema, the assessor produces a summary aggregated report that shows the estimated complexity for each possible migration target. It also produces a server-level report that includes the License Evaluation and Cloud Support section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
