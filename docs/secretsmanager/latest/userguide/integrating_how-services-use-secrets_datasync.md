---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_datasync.html
---

# How AWS DataSync uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_datasync"></a>

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates moving data between storage systems and services.

Some of the storage systems supported by DataSync require credentials to read and write data. DataSync uses Secrets Manager to store or access storage credentials. You can configure DataSync to create secrets on your behalf or you can provide a custom secret. Service-managed secrets begin with the prefix `aws-datasync`. You are charged only for the use of secrets that you create outside of DataSync. See [Providing credentials for storage locations](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html) in the *AWS DataSync User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
