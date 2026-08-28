---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/security-encryption.html
---

# Encryption in Amazon Simple Workflow Service
<a name="security-encryption"></a>

## Encryption at rest
<a name="security-encryption-at-rest"></a>

Amazon SWF always encrypts your data at rest. Data in Amazon Simple Workflow Service is encrypted at rest using transparent server-side encryption. This helps reduce the operational burden and complexity involved in protecting sensitive data. With encryption at rest, you can build security-sensitive applications that meet encryption compliance and regulatory requirements

## Encryption in transit
<a name="security-encryption-in-transit"></a>

All data that passes between Amazon SWF and other services is encrypted using Transport Layer Security (TLS).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
