---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service EncryptionConfiguration
<a name="aws-properties-apprunner-service-encryptionconfiguration"></a>

Describes a custom encryption key that AWS App Runner uses to encrypt copies of the source repository and service logs.

## Syntax
<a name="aws-properties-apprunner-service-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKey](#cfn-apprunner-service-encryptionconfiguration-kmskey)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsKey](#cfn-apprunner-service-encryptionconfiguration-kmskey): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-encryptionconfiguration-properties"></a>

`KmsKey`  <a name="cfn-apprunner-service-encryptionconfiguration-kmskey"></a>
The ARN of the KMS key that's used for encryption.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws(-[\w]+)*:kms:[a-z\-]+-[0-9]{1}:[0-9]{12}:key\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
