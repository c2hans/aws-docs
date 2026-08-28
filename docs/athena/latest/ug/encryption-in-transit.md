---
source_url: https://docs.aws.amazon.com/athena/latest/ug/encryption-in-transit.html
---

# Encryption in transit
<a name="encryption-in-transit"></a>

In addition to encrypting data at rest in Amazon S3, Amazon Athena uses Transport Layer Security (TLS) encryption for data in-transit between Athena and Amazon S3, and between Athena and customer applications accessing it.

You should allow only encrypted connections over HTTPS (TLS) using the [`aws:SecureTransport condition`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html#Conditions_Boolean) on Amazon S3 bucket IAM policies.

Query results that stream to JDBC or ODBC clients are encrypted using TLS. For information about the latest versions of the JDBC and ODBC drivers and their documentation, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md) and [Connect to Amazon Athena with ODBC](connect-with-odbc.md).

For Athena federated data source connectors, support for encryption in transit using TLS depends on the individual connector. For information, see the documentation for the individual [data source connectors](connectors-available.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
