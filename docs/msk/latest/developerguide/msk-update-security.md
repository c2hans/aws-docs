---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-security.html
---

# Update security settings of a Amazon MSK cluster
<a name="msk-update-security"></a>

Use the [UpdateSecurity](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-security.html#UpdateSecurity) Amazon MSK operation to update the authentication and client-broker encryption settings of your MSK cluster. You can also update the Private Security Authority used to sign certificates for mutual TLS authentication. You can't change the in-cluster (broker-to-broker) encryption setting.

The cluster must be in the `ACTIVE` state for you to update its security settings.

If you turn on authentication using IAM, SASL, or TLS, you must also turn on encryption between clients and brokers. The following table shows the possible combinations.

| Authentication | Client-broker encryption options | Broker-broker encryption |
| --- | --- | --- |
| Unauthenticated | TLS, PLAINTEXT, TLS\_PLAINTEXT | Can be on or off. |
| mTLS | TLS, TLS\_PLAINTEXT | Must be on. |
| SASL/SCRAM | TLS | Must be on. |
| SASL/IAM | TLS | Must be on. |

When client-broker encryption is set to `TLS_PLAINTEXT` and client-authentication is set to `mTLS`, Amazon MSK creates two types of listeners for clients to connect to: one listener for clients to connect using mTLS authentication with TLS Encryption, and another for clients to connect without authentication or encryption (plaintext).

For more information about security settings, see [Security in Amazon MSK](security.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
