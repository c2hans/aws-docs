---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/port-info.html
---

# Port information
<a name="port-info"></a>

Use the following port numbers so that Amazon MSK can communicate with client machines:
+ To communicate with brokers in plaintext, use port 9092.
+ To communicate with brokers with TLS encryption, use port 9094 for access from within AWS and port 9194 for public access.
+ To communicate with brokers with SASL/SCRAM, use port 9096 for access from within AWS and port 9196 for public access.
+ To communicate with brokers in a cluster that is set up to use [IAM access control](iam-access-control.md), use port 9098 for access from within AWS and port 9198 for public access.
+ To communicate with brokers using IPv6 network type in plaintext, use port 20092
+ To communicate with brokers in a cluster that is set up to use IAM access control using IPv6, use port 20098.
+ To communicate with brokers with SASL/SCRAM using IPv6, use port 20096.
+ To communicate with brokers with TLS encryption using IPv6, use port 20094.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
