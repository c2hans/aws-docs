---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/custom-data-sources.html
---

# Custom sources
<a name="custom-data-sources"></a>

For custom application logs, you can define your own data source categorization using one of the following methods:
+ **Log group tags** – Add tags to your log groups using the keys `cw:datasource:name` and `cw:datasource:type` to specify the data source name and type for all logs ingested in the log group.
+ **Pipeline configuration** – Configure data source information through log processing pipelines when ingesting your application logs.

**Note**
Custom data source names cannot start with "aws" or "amazon" to avoid conflicts with AWS service logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
