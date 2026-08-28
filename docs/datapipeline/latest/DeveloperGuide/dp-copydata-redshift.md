---
source_url: https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-copydata-redshift.html
---

AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/)

# Copy Data to Amazon Redshift Using AWS Data Pipeline
<a name="dp-copydata-redshift"></a>

This tutorial walks you through the process of creating a pipeline that periodically moves data from Amazon S3 to Amazon Redshift using either the **Copy to Redshift** template in the AWS Data Pipeline console, or a pipeline definition file with the AWS Data Pipeline CLI.

Amazon S3 is a web service that enables you to store data in the cloud. For more information, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

Amazon Redshift is a data warehouse service in the cloud. For more information, see the [Amazon Redshift Management Guide](https://docs.aws.amazon.com/redshift/latest/mgmt/).

This tutorial has several prerequisites. After completing the following steps, you can continue the tutorial using either the console or the CLI.

**Topics**
+ [Before You Begin: Configure COPY Options and Load Data](dp-learn-copy-redshift.md)
+ [Set up Pipeline, Create a Security Group, and Create an Amazon Redshift Cluster](dp-copydata-redshift-prereq.md)
+ [Copy Data to Amazon Redshift Using the Command Line](dp-copydata-redshift-cli.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
