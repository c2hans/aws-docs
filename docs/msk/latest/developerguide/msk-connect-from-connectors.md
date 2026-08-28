---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-from-connectors.html
---

# Connecting from connectors
<a name="msk-connect-from-connectors"></a>

The following best practices can improve the performance of your connectivity to Amazon MSK Connect.

## Do not overlap IPs for Amazon VPC peering or Transit Gateway
<a name="CIDR-ip-ranges"></a>

If you are using Amazon VPC peering or Transit Gateway with Amazon MSK Connect, do not configure your connector for reaching the peered VPC resources with IPs in the CIDR ranges:
+ "10.99.0.0/16"
+ "192.168.0.0/16"
+ "172.21.0.0/16"

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
