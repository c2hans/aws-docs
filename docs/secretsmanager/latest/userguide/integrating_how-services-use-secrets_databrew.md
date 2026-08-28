---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_databrew.html
---

# How AWS Glue DataBrew uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_databrew"></a>

AWS Glue DataBrew is a visual data preparation tool that you can use to clean and normalize data without writing any code. In DataBrew, a set of data transformation steps is called a recipe. AWS Glue DataBrew provides the [`DETERMINISTIC_DECRYPT`](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_DECRYPT.html), [`DETERMINISTIC_ENCRYPT`](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_ENCRYPT.html), and [`CRYPTOGRAPHIC_HASH`](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.CRYPTOGRAPHIC_HASH.html) recipe steps to perform transformations on personally identifiable information (PII) in a dataset, which use an encryption key stored in a Secrets Manager secret. If you use the DataBrew *default secret* to store the encryption key, DataBrew creates a [managed secret](service-linked-secrets.md) with the prefix `databrew`. The cost of storing the secret is included with the charge for using DataBrew. If you create a new secret to store the encryption key, DataBrew creates a secret with the prefix `AwsGlueDataBrew`. You are charged for that secret.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
