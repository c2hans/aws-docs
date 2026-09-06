---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SecretsManagerConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration"></a>

The structure that defines how Firehose accesses the secret.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-enabled)" : {{Boolean}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-rolearn)" : {{String}},
  "[SecretARN](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-enabled): {{Boolean}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-rolearn): {{String}}
  [SecretARN](#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-enabled"></a>
Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When it's set to `False` Firehose falls back to the credentials in the destination configuration.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-rolearn"></a>
 Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.
*Required*: No
*Type*: String
*Pattern*: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretARN`  <a name="cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-secretarn"></a>
The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True`.
*Required*: No
*Type*: String
*Pattern*: `arn:.*:secretsmanager:[a-zA-Z0-9\-]+:\d{12}:secret:[a-zA-Z0-9\-/_+=.@]+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
