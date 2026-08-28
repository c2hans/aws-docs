---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html
---

# Querying Cost and Usage Reports using Amazon Athena
<a name="cur-query-athena"></a>

Amazon Athena is a serverless query service that you can use to analyze the data from your AWS Cost and Usage Reports (AWS CUR) in Amazon Simple Storage Service (Amazon S3) using standard SQL. This helps you avoid having to create your own data warehouse solutions to query AWS CUR data.

We strongly recommend that you create both a new Amazon S3 bucket and a new AWS CUR report to use with Athena. AWS CUR supports only the Apache Parquet compression format for Athena and automatically overwrites previous reports that are stored in your S3 bucket.

This section outlines how to use Athena with Cost and Usage Reports. For a full description of the Athena service, see the [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/latest/ug/).

**Topics**
+ [Setting up Athena using CloudFormation templates](use-athena-cf.md)
+ [Setting up Athena manually](cur-ate-manual.md)
+ [Running Amazon Athena queries](cur-ate-run.md)
+ [Loading report data to other resources](cur-query-other.md)

For a demonstration of querying reports using Athena, see the following video.

[![AWS Videos](http://img.youtube.com/vi/KEeJEZTYE8E/0.jpg)](http://www.youtube.com/watch?v=KEeJEZTYE8E)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
