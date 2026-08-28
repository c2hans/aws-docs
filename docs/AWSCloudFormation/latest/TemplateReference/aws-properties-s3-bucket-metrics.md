---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-metrics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket Metrics
<a name="aws-properties-s3-bucket-metrics"></a>

 A container specifying replication metrics-related settings enabling replication metrics and events.

## Syntax
<a name="aws-properties-s3-bucket-metrics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-metrics-syntax.json"></a>

```
{
  "[EventThreshold](#cfn-s3-bucket-metrics-eventthreshold)" : {{ReplicationTimeValue}},
  "[Status](#cfn-s3-bucket-metrics-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-metrics-syntax.yaml"></a>

```
  [EventThreshold](#cfn-s3-bucket-metrics-eventthreshold): {{
    ReplicationTimeValue}}
  [Status](#cfn-s3-bucket-metrics-status): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-metrics-properties"></a>

`EventThreshold`  <a name="cfn-s3-bucket-metrics-eventthreshold"></a>
 A container specifying the time threshold for emitting the `s3:Replication:OperationMissedThreshold` event.
*Required*: No
*Type*: [ReplicationTimeValue](aws-properties-s3-bucket-replicationtimevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-s3-bucket-metrics-status"></a>
 Specifies whether the replication metrics are enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `Disabled | Enabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-s3-bucket-metrics--seealso"></a>
+ AWS::S3::Bucket [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#aws-properties-s3-bucket--examples)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
