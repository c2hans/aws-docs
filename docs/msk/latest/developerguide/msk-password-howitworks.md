---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-password-howitworks.html
---

# How sign-in credentials authentication works
<a name="msk-password-howitworks"></a>

Sign-in credentials authentication for Amazon MSK uses SASL/SCRAM (Simple Authentication and Security Layer/ Salted Challenge Response Mechanism) authentication. To set up sign-in credentials authentication for a cluster, you create a Secret resource in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/?id=docs_gateway), and associate sign-in credentials with that secret.

SASL/SCRAM is defined in [RFC 5802](https://tools.ietf.org/html/rfc5802). SCRAM uses secured hashing algorithms, and does not transmit plaintext sign-in credentials between client and server.

**Note**
When you set up SASL/SCRAM authentication for your cluster, Amazon MSK turns on TLS encryption for all traffic between clients and brokers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
