---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-quotas.html
---

# Service quotas for managed knowledge bases
<a name="kb-managed-quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for managed Amazon Bedrock knowledge bases. To view service quotas for Amazon Bedrock, do one of the following:
+ Follow the steps at [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html) and select **Amazon Bedrock** as the service.
+ Refer to [Amazon Bedrock service quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock) in the AWS General Reference.

The following quotas apply specifically to managed knowledge bases:

**Managed knowledge base quotas**

| Quota | Default value | Adjustable |
| --- | --- | --- |
| Maximum managed knowledge bases per account, per Region | 10,000 | Yes |
| Maximum data sources per knowledge base | 200 | No |
| Maximum concurrent ingestion jobs per knowledge base | 50 | No |
| Maximum raw data storage per knowledge base | 10 TB | No |
| Maximum query input characters per Retrieve or AgenticRetrieveStream request (English text) | 10,000 | No |
| Maximum Retrieve requests per minute (RPM), per knowledge base | 600 (supports burst of 25 requests per second (RPS)) | Yes |
| Maximum AgenticRetrieveStream requests per minute, per account | 300 | Yes |

To request adjustable quota increases, follow the steps at [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html), or contact your AWS account team.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
