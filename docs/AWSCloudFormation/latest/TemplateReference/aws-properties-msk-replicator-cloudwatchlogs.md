---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-cloudwatchlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator CloudWatchLogs
<a name="aws-properties-msk-replicator-cloudwatchlogs"></a>

CloudWatch Logs details for ReplicatorLogDelivery.

## Syntax
<a name="aws-properties-msk-replicator-cloudwatchlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-cloudwatchlogs-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-replicator-cloudwatchlogs-enabled)" : {{Boolean}},
  "[LogGroup](#cfn-msk-replicator-cloudwatchlogs-loggroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-msk-replicator-cloudwatchlogs-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-replicator-cloudwatchlogs-enabled): {{Boolean}}
  [LogGroup](#cfn-msk-replicator-cloudwatchlogs-loggroup): {{String}}
```

## Properties
<a name="aws-properties-msk-replicator-cloudwatchlogs-properties"></a>

`Enabled`  <a name="cfn-msk-replicator-cloudwatchlogs-enabled"></a>
Whether log delivery to CloudWatch Logs is enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroup`  <a name="cfn-msk-replicator-cloudwatchlogs-loggroup"></a>
The CloudWatch log group that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
