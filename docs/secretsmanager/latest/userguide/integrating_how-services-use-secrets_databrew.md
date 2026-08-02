---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_databrew.html
---

# How AWS Glue DataBrew uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_databrew"></a>

AWS Glue DataBrew is a visual data preparation tool that you can use to clean and normalize data without writing any code. In DataBrew, a set of data transformation steps is called a recipe. AWS Glue DataBrew provides the [https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_DECRYPT.html](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_DECRYPT.html), [https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_ENCRYPT.html](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.DETERMINISTIC_ENCRYPT.html), and [https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.CRYPTOGRAPHIC_HASH.html](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.CRYPTOGRAPHIC_HASH.html) recipe steps to perform transformations on personally identifiable information (PII) in a dataset, which use an encryption key stored in a Secrets Manager secret. If you use the DataBrew *default secret* to store the encryption key, DataBrew creates a [managed secret](service-linked-secrets.md) with the prefix `databrew`. The cost of storing the secret is included with the charge for using DataBrew. If you create a new secret to store the encryption key, DataBrew creates a secret with the prefix `AwsGlueDataBrew`. You are charged for that secret.
