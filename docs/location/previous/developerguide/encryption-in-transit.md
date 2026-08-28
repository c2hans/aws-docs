---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/encryption-in-transit.html
---

# Data in transit encryption for Amazon Location Service
<a name="encryption-in-transit"></a>

Amazon Location protects data in transit, as it travels to and from the service, by automatically encrypting all inter-network data using the Transport Layer Security (TLS) 1.2 encryption protocol. Direct HTTPS requests sent to the Amazon Location Service APIs are signed by using the [AWS Signature Version 4 Algorithm](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html) to establish a secure connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
