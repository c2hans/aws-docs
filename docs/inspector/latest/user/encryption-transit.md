---
source_url: https://docs.aws.amazon.com/inspector/latest/user/encryption-transit.html
---

# Encryption in transit
<a name="encryption-transit"></a>

 AWS encrypts all data in transit between AWS internal systems and other AWS services. AWS Systems Manager gathers telemetry data from customer-owned EC2 instances it sends to AWS over a Transport Layer Security (TLS)-protected channel for assessment. Amazon ECR and AWS Lambda function scan findings that are sent to Security Hub CSPM are encrypted using a TLS-protected channel. For more information, see [Data Protection in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/data-protection.html) to understand how SSM encrypts data in transit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
