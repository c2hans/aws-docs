---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/read-s3-standard-storage-class.html
---

# Reading archived S3 objects with Standard storage class
<a name="read-s3-standard-storage-class"></a>

You can read S3 objects that are archived with the Amazon S3 storage class by using AWS Glue.

## Using AWS Glue
<a name="using-aws-glue.96b4be67-4561-5154-b84b-787a17431ad7"></a>

The data off-loaded from MySQL to Amazon S3 retains the same structural rigidity and consistency typical of a relational database management system (RDBMS).

[AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) crawls over S3 objects, infers the data types, and creates table metadata as an external table DDL. When you configure the crawler job, use Amazon S3 as the source, and specify the S3 prefix location where all the data-files are created. In the configuration, include the following:
+ Crawler run options
+ Optional table prefix preference
+ Target database for creating the table
+ IAM roles with required permissions

After you invoke the job, it will scan through the data to infer the schema and preserve it in [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) as [AWS Glue tables](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html). AWS Glue tables are essentially external tables that can be queried with SQL statements like a normal database table using analytical services such as [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html), and Apache Hive on [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html). For more information about the crawler, see the [AWS Glue documentation](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).

For .csv files with a column header specified, the resultant table column names will reflect the same field names. The data type is inferred based on the values in the data object.

For Parquet files, the schema is preserved within the data itself and the resultant table will reflect the same field names and data type.

Alternatively, you can run a DDL manually within Athena to create the table definition with the required column names and data type. This creates the table definition within Data Catalog. For more information about creating Athena tables, see the [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html).

**Note**
If the header row is missing from the CSV file, the crawler creates the field name as generic c\_0, c\_1,c\_2,...

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
