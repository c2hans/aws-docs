---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-redshift.html
---

# Accessing Amazon S3 tables with Amazon Redshift
<a name="s3-tables-integrating-redshift"></a>

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools. Redshift Serverless lets you access and analyze data without all of the configurations of a provisioned data warehouse. For more information, see [Get started with serverless data warehouses](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html) in the *Amazon Redshift Getting Started Guide*.

## Query Amazon S3 tables with Amazon Redshift
<a name="rs-query-table"></a>

**Prerequisites**
+ [Integrate your table buckets with AWS analytics services](s3-tables-integrating-aws.md).
  + [Create a namespace](s3-tables-namespace-create.md).
  + [Create a table](s3-tables-create.md).
+ [Managing access to a table or database with Lake Formation](grant-permissions-tables.md).

After you complete the prerequisites, you can begin using Amazon Redshift to query tables in one of the following ways:
+ [Using the Amazon Redshift query editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)
+ [Connecting to an Amazon Redshift data warehouse using SQL client tools](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-to-cluster.html)
+ [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
