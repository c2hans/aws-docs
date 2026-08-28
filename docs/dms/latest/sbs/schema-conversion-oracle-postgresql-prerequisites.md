---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-prerequisites.html
---

# Prerequisites for migrating Oracle databases to Amazon Aurora PostgreSQL with DMS schema conversion
<a name="schema-conversion-oracle-postgresql-prerequisites"></a>

The following prerequisites are also required to complete this walkthrough:
+ Familiarity with the AWS Management Console, AWS Database Migration Service, and SQL.
+ A user with AWS Identity and Access Management (IAM) credentials. Make sure that you can use these credentials to create an Amazon S3 bucket in your AWS Region.
+ Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups.
+ An understanding of the supported features and limitations of DMS Schema Conversion. For more information, see [Schema conversion limitations](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html#schema-conversion-limitations).

We recommend that you don’t use your production workloads for the migration in this walkthrough. After you get familiar with migration tools and AWS services, you can migrate your production workloads.

Make sure that you create all your AWS and DMS Schema Conversion resources in the AWS Regions that support DMS Schema Conversion. For more information, see the [list of supported Regions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html#schema-conversion-supported-regions). In other Regions, you can use the AWS Schema Conversion Tool. For an example of migration from Oracle to PostgreSQL with AWS SCT, see [Use Schema Conversion Tool to Convert the Oracle Schema to PostgreSQL](chap-rdsoracle2postgresql.steps.convertschema.md).

For more information about DMS Schema Conversion, see the [user guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
