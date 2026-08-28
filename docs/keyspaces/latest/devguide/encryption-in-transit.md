---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/encryption-in-transit.html
---

# Encryption in transit in Amazon Keyspaces
<a name="encryption-in-transit"></a>

Amazon Keyspaces only accepts secure connections using Transport Layer Security (TLS). Encryption in transit provides an additional layer of data protection by encrypting your data as it travels to and from Amazon Keyspaces. Organizational policies, industry or government regulations, and compliance requirements often require the use of encryption in transit to increase the data security of your applications when they transmit data over the network.

To learn how to encrypt `cqlsh` connections to Amazon Keyspaces using TLS, see [How to manually configure `cqlsh` connections for TLS](programmatic.cqlsh.md#encrypt_using_tls). To learn how to use TLS encryption with client drivers, see [Using a Cassandra client driver to access Amazon Keyspaces programmatically](programmatic.drivers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
