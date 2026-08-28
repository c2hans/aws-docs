---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/encryption-in-transit.html
---

# Encryption in transit
<a name="encryption-in-transit"></a>

AWS provides Secure Sockets Layer (SSL) encryption for data in flight.

DataBrew support for JDBC data sources comes through AWS Glue. When connecting to JDBC data sources, DataBrew uses the settings on your AWS Glue connection, including the **Require SSL connection** option. For more information, see [AWS Glue Connection Properties - AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html) in the *AWS Glue Developer Guide*.

AWS KMS provides both "bring your own key" encryption and server-side encryption for DataBrew extract, transform, load (ETL) processing and for the AWS Glue Data Catalog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
