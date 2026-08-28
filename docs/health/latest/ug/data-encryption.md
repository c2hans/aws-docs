---
source_url: https://docs.aws.amazon.com/health/latest/ug/data-encryption.html
---

# Data encryption
<a name="data-encryption"></a>

See the following information about how AWS Health encrypts data.

Data encryption refers to protecting data while in-transit (as it travels from the service to your AWS account), and at rest (while it is stored in AWS services). You can protect data in transit using Transport Layer Security (TLS) or at rest using client-side encryption.

AWS Health doesn't record personal identifying information (PII) such as email addresses or customer names in events.

## Encryption at rest
<a name="encryption-at-rest"></a>

All data stored by AWS Health is encrypted at rest.

## Encryption in transit
<a name="encryption-in-transit"></a>

All data sent to and from AWS Health is encrypted in transit.

## Key management
<a name="key-management"></a>

AWS Health doesn't support customer-managed encryption keys for data encrypted in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
