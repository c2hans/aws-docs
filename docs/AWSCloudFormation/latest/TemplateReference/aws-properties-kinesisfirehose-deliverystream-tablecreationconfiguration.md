---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream TableCreationConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration"></a>

The configuration to enable automatic table creation.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-tablecreationconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-tablecreationconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-tablecreationconfiguration-enabled"></a>
 Specify whether you want to enable automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
