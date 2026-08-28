---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::CacheCluster CloudWatchLogsDestinationDetails
<a name="aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails"></a>

Configuration details of a CloudWatch Logs destination. Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.

## Syntax
<a name="aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails-syntax.json"></a>

```
{
  "[LogGroup](#cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails-syntax.yaml"></a>

```
  [LogGroup](#cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup): {{String}}
```

## Properties
<a name="aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails-properties"></a>

`LogGroup`  <a name="cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup"></a>
The name of the CloudWatch Logs log group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
