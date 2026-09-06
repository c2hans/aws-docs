---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DatabaseSourceAuthenticationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration"></a>

 The structure to configure the authentication methods for Firehose to connect to source database endpoint.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-syntax.json"></a>

```
{
  "[SecretsManagerConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-secretsmanagerconfiguration)" : {{SecretsManagerConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-syntax.yaml"></a>

```
  [SecretsManagerConfiguration](#cfn-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-secretsmanagerconfiguration): {{
    SecretsManagerConfiguration}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-properties"></a>

`SecretsManagerConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-secretsmanagerconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretsManagerConfiguration](aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
