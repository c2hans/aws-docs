---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-authorizerlogs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster AuthorizerLogs
<a name="aws-properties-msk-cluster-authorizerlogs"></a>

<a name="aws-properties-msk-cluster-authorizerlogs-description"></a>The `AuthorizerLogs` property type specifies Property description not available. for an [AWS::MSK::Cluster](aws-resource-msk-cluster.md).

## Syntax
<a name="aws-properties-msk-cluster-authorizerlogs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-authorizerlogs-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-msk-cluster-authorizerlogs-cloudwatchlogs)" : {{CloudWatchLogs}},
  "[Firehose](#cfn-msk-cluster-authorizerlogs-firehose)" : {{Firehose}},
  "[S3](#cfn-msk-cluster-authorizerlogs-s3)" : {{S3}}
}
```

### YAML
<a name="aws-properties-msk-cluster-authorizerlogs-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-msk-cluster-authorizerlogs-cloudwatchlogs): {{
    CloudWatchLogs}}
  [Firehose](#cfn-msk-cluster-authorizerlogs-firehose): {{
    Firehose}}
  [S3](#cfn-msk-cluster-authorizerlogs-s3): {{
    S3}}
```

## Properties
<a name="aws-properties-msk-cluster-authorizerlogs-properties"></a>

`CloudWatchLogs`  <a name="cfn-msk-cluster-authorizerlogs-cloudwatchlogs"></a>
Property description not available.
*Required*: No
*Type*: [CloudWatchLogs](aws-properties-msk-cluster-cloudwatchlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Firehose`  <a name="cfn-msk-cluster-authorizerlogs-firehose"></a>
Property description not available.
*Required*: No
*Type*: [Firehose](aws-properties-msk-cluster-firehose.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-msk-cluster-authorizerlogs-s3"></a>
Property description not available.
*Required*: No
*Type*: [S3](aws-properties-msk-cluster-s3.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
