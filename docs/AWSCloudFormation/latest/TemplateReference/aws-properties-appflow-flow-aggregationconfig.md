---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-aggregationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow AggregationConfig
<a name="aws-properties-appflow-flow-aggregationconfig"></a>

 The aggregation settings that you can use to customize the output format of your flow data.

## Syntax
<a name="aws-properties-appflow-flow-aggregationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-aggregationconfig-syntax.json"></a>

```
{
  "[AggregationType](#cfn-appflow-flow-aggregationconfig-aggregationtype)" : {{String}},
  "[TargetFileSize](#cfn-appflow-flow-aggregationconfig-targetfilesize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appflow-flow-aggregationconfig-syntax.yaml"></a>

```
  [AggregationType](#cfn-appflow-flow-aggregationconfig-aggregationtype): {{String}}
  [TargetFileSize](#cfn-appflow-flow-aggregationconfig-targetfilesize): {{Integer}}
```

## Properties
<a name="aws-properties-appflow-flow-aggregationconfig-properties"></a>

`AggregationType`  <a name="cfn-appflow-flow-aggregationconfig-aggregationtype"></a>
 Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.
*Required*: No
*Type*: String
*Allowed values*: `None | SingleFile`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetFileSize`  <a name="cfn-appflow-flow-aggregationconfig-targetfilesize"></a>
The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-flow-aggregationconfig--seealso"></a>
+ [AggregationConfig](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_AggregationConfig.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
