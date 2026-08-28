---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ApplicationEncryptionConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration"></a>

Specifies the configuration to manage encryption at rest.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration-syntax.json"></a>

```
{
  "[KeyId](#cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keyid)" : {{String}},
  "[KeyType](#cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration-syntax.yaml"></a>

```
  [KeyId](#cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keyid): {{String}}
  [KeyType](#cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keytype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-applicationencryptionconfiguration-properties"></a>

`KeyId`  <a name="cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keyid"></a>
The key ARN, key ID, alias ARN, or alias name of the KMS key used for encryption at rest.
*Required*: No
*Type*: String
*Pattern*: `^(?:arn:.*:kms:.*:.*:(?:key\/.*|alias\/.*)|alias\/.*|(?i)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyType`  <a name="cfn-kinesisanalyticsv2-application-applicationencryptionconfiguration-keytype"></a>
Specifies the type of key used for encryption at rest.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
