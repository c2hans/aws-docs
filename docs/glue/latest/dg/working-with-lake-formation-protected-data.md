---
source_url: https://docs.aws.amazon.com/glue/latest/dg/working-with-lake-formation-protected-data.html
---

# Working with AWS Lake Formation-protected data
<a name="working-with-lake-formation-protected-data"></a>

## Full Table Access
<a name="full-table-access"></a>

AWS Glue supports Full Table Access (FTA) for AWS Lake Formation-protected tables. This allows your ETL jobs to read and write data with full table permissions.

### Prerequisites
<a name="full-table-access-prerequisites"></a>
+ Appropriate IAM roles and permissions
+ AWS Lake Formation configured for your data catalog
+ Compatible table types (Hive or Iceberg)

### Key considerations
<a name="full-table-access-key-considerations"></a>

#### Required permissions
<a name="full-table-access-required-permissions"></a>
+ `lakeformation:GetDataAccess` IAM permission
+ AWS Lake Formation table permissions
+ Amazon S3 bucket access permissions

#### Supported table types
<a name="full-table-access-supported-table-types"></a>
+ Hive tables
+ Iceberg tables

#### Limitations
<a name="full-table-access-limitations"></a>
+ Not compatible with Spark Streaming
+ Cannot be used simultaneously with fine-grained access control
+ Does not support Delta or Hudi tables

### Best Practices
<a name="full-table-access-best-practices"></a>

1. Ensure IAM roles are properly configured before job execution

1. Test access permissions in a development environment

1. Monitor job execution logs for permission-related issues

1. Maintain clear documentation of access patterns

### Troubleshooting
<a name="full-table-access-troubleshooting"></a>

Common issues include:
+ Missing IAM permissions
+ Incorrect AWS Lake Formation configuration
+ Table type compatibility problems

For complete setup instructions and configuration details, see [ Using AWS Lake Formation with full table access](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/lake-formation-unfiltered-access.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
