---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::CacheCluster KinesisFirehoseDestinationDetails
<a name="aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails"></a>

The configuration details of the Kinesis Data Firehose destination. Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.

## Syntax
<a name="aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails-syntax.json"></a>

```
{
  "[DeliveryStream](#cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails-syntax.yaml"></a>

```
  [DeliveryStream](#cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream): {{String}}
```

## Properties
<a name="aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails-properties"></a>

`DeliveryStream`  <a name="cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream"></a>
The name of the Kinesis Data Firehose delivery stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
