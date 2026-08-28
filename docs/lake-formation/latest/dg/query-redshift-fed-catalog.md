---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/query-redshift-fed-catalog.html
---

# Querying federated catalogs
<a name="query-redshift-fed-catalog"></a>

After you grant permissions to other principals, they can sign in and start querying the tables in the federated catalogs by logging into the SQL tools using Amazon Redshift, Amazon EMR, Amazon Athena, and AWS Glue ETL.

 For more information on connecting to the AWS Glue Data Catalog using Apache Iceberg Rest extension endpoint or standalone Spark application, see [Accessing the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/access_catalog.html) section in the AWS Glue Developer Guide.

You can use the data definition language (DDL) queries to create and manage tables in the database using Apache Spark on Amazon EMR. To create and delete tables in the Amazon Redshift database, the principal must have Lake Formation `Create table`, `Drop` permissions.

 For more information on granting Data Catalog permissions, see [Granting permissions on Data Catalog resources](granting-catalog-permissions.md).

For more information on querying the catalog resources from Amazon Athena, see [Querying AWS Glue Data Catalog from Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/gdc-register.html) in Amazon Athena User Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
