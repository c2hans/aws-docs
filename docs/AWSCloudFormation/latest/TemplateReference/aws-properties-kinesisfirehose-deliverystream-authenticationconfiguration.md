---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream AuthenticationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration"></a>

The authentication configuration of the Amazon MSK cluster.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration-syntax.json"></a>

```
{
  "[Connectivity](#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity)" : {{String}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration-syntax.yaml"></a>

```
  [Connectivity](#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity): {{String}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration-properties"></a>

`Connectivity`  <a name="cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity"></a>
The type of connectivity used to access the Amazon MSK cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLIC | PRIVATE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn"></a>
The ARN of the role used to access the Amazon MSK cluster.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
