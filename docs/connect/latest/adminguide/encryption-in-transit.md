---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/encryption-in-transit.html
---

# Encryption in transit in Connect Customer
<a name="encryption-in-transit"></a>

All data exchanged with Connect Customer is protected in transit between the user’s web browser and Connect Customer using industry-standard TLS encryption. [Which version of TLS?](infrastructure-security.md#supported-version-tls)

External data is additionally encrypted while being processed by AWS KMS.

When Connect Customer integrates with AWS services, such as AWS Lambda, Amazon Kinesis, or Amazon Polly, data is always encrypted in transit using TLS.

When event data is forwarded from external applications to Connect Customer it is always encrypted in transit using TLS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
