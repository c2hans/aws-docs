---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html
---

# Mutual TLS client authentication for Amazon MSK
<a name="msk-authentication"></a>

You can enable client authentication with TLS for connections from your applications to your Amazon MSK brokers. To use client authentication, you need an AWS Private CA. The AWS Private CA can be either in the same AWS account as your cluster, or in a different account. For information about AWS Private CAs, see [Creating and Managing a AWS Private CA](https://docs.aws.amazon.com/acm-pca/latest/userguide/create-CA.html).

Amazon MSK doesn't support certificate revocation lists (CRLs). To control access to your cluster topics or block compromised certificates, use Apache Kafka ACLs and AWS security groups. For information about using Apache Kafka ACLs, see [Apache Kafka ACLs](msk-acls.md).

**Topics**
+ [Create a Amazon MSK cluster that supports client authentication](msk-authentication-cluster.md)
+ [Set up a client to use authentication](msk-authentication-client.md)
+ [Produce and consume messages using authentication](msk-authentication-messages.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
