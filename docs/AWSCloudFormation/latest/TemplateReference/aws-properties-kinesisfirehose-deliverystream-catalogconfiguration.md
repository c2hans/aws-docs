---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-catalogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream CatalogConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-catalogconfiguration"></a>

 Describes the containers where the destination Apache Iceberg Tables are persisted.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-catalogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-catalogconfiguration-syntax.json"></a>

```
{
  "[CatalogArn](#cfn-kinesisfirehose-deliverystream-catalogconfiguration-catalogarn)" : {{String}},
  "[WarehouseLocation](#cfn-kinesisfirehose-deliverystream-catalogconfiguration-warehouselocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-catalogconfiguration-syntax.yaml"></a>

```
  [CatalogArn](#cfn-kinesisfirehose-deliverystream-catalogconfiguration-catalogarn): {{String}}
  [WarehouseLocation](#cfn-kinesisfirehose-deliverystream-catalogconfiguration-warehouselocation): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-catalogconfiguration-properties"></a>

`CatalogArn`  <a name="cfn-kinesisfirehose-deliverystream-catalogconfiguration-catalogarn"></a>
 Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables. You must specify the ARN in the format `arn:aws:glue:region:account-id:catalog`.
*Required*: No
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WarehouseLocation`  <a name="cfn-kinesisfirehose-deliverystream-catalogconfiguration-warehouselocation"></a>
The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: String
*Pattern*: `s3:\/\/.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
