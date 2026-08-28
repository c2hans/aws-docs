---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_appflow.html
---

# How Amazon AppFlow uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_appflow"></a>

Amazon AppFlow is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and AWS services, such as Amazon Simple Storage Service (Amazon S3) and Amazon Redshift.

In Amazon AppFlow, when you configure an SaaS application as a source or destination, you create a connection. This includes information required for connecting to the SaaS applications, such as authentication tokens, user names, and passwords. Amazon AppFlow stores your connection data in a Secrets Manager [managed secret](service-linked-secrets.md) with the prefix `appflow`. The cost of storing the secret is included with the charge for Amazon AppFlow. For more information, see [Data protection in Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/data-protection.html#encryption-rest) in the *Amazon AppFlow User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
