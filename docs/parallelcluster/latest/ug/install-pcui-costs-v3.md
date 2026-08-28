---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/install-pcui-costs-v3.html
---

# PCUI costs
<a name="install-pcui-costs-v3"></a>

The PCUI is built on a serverless architecture and you can use it within the AWS Free Tier category for most cases. The following table lists the AWS services that the PCUI depends on and their free-tier limits. Typical usage is estimated to cost less than one dollar each month.

| Service | AWS Free Tier |
| --- | --- |
| Amazon Cognito | 50,000 monthly active users |
| Amazon API Gateway | 1 million rest API calls |
| AWS Lambda | 1 million free requests each month and 400,000 GB-seconds of compute time each month |
| EC2 Image Builder | No cost, except EC2 |
| Amazon Elastic Compute Cloud | 15-minute one-time container image build |
| CloudFormation | 5 GB data (ingestion, archive storage, and data scanned by Logs Insights queries) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
