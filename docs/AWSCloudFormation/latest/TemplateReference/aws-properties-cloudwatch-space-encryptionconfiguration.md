---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-space-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Space EncryptionConfiguration
<a name="aws-properties-cloudwatch-space-encryptionconfiguration"></a>

The encryption configuration for the space.

## Syntax
<a name="aws-properties-cloudwatch-space-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-space-encryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionStrategy](#cfn-cloudwatch-space-encryptionconfiguration-encryptionstrategy)" : {{String}},
  "[KmsKeyArn](#cfn-cloudwatch-space-encryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-space-encryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionStrategy](#cfn-cloudwatch-space-encryptionconfiguration-encryptionstrategy): {{String}}
  [KmsKeyArn](#cfn-cloudwatch-space-encryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-space-encryptionconfiguration-properties"></a>

`EncryptionStrategy`  <a name="cfn-cloudwatch-space-encryptionconfiguration-encryptionstrategy"></a>
Whether the space is encrypted with an AWS owned key or a customer managed key.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_OWNED | CUSTOMER_MANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-cloudwatch-space-encryptionconfiguration-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the customer managed KMS key. Required when encryptionStrategy is CUSTOMER\_MANAGED.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov):kms:[a-z0-9-]+:[0-9]{12}:key/(?:mrk-)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
