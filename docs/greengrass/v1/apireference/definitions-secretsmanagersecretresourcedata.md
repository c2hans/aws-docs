---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-secretsmanagersecretresourcedata.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# SecretsManagerSecretResourceData
<a name="definitions-secretsmanagersecretresourcedata"></a>

```
{
"ARN": "string",
"AdditionalStagingLabelsToDownload": [
  "string"
]
}
```

SecretsManagerSecretResourceData
Attributes that define a secret resource, which references a secret from AWS Secrets Manager. AWS IoT Greengrass stores a local, encrypted copy of the secret on the Greengrass core, where it can be securely accessed by connectors and Lambda functions.
type: object

ARN
The ARN of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the `AWSCURRENT` staging label) is included by default.
type: string

AdditionalStagingLabelsToDownload
Optional. The staging labels in addition to `AWSCURRENT` whose values you want to make available on the core.
type: array
