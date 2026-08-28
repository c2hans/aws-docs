---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kendraranking-executionplan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KendraRanking::ExecutionPlan
<a name="aws-resource-kendraranking-executionplan"></a>

Creates a rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the `Rescore` API. You set the number of capacity units that you require for Amazon Kendra Intelligent Ranking to rescore or re-rank a search service's results.

For an example of using the `CreateRescoreExecutionPlan` API, including using the Python and Java SDKs, see [Semantically ranking a search service's results](https://docs.aws.amazon.com/kendra/latest/dg/search-service-rerank.html).

## Syntax
<a name="aws-resource-kendraranking-executionplan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kendraranking-executionplan-syntax.json"></a>

```
{
  "Type" : "AWS::KendraRanking::ExecutionPlan",
  "Properties" : {
      "[CapacityUnits](#cfn-kendraranking-executionplan-capacityunits)" : {{CapacityUnitsConfiguration}},
      "[Description](#cfn-kendraranking-executionplan-description)" : {{String}},
      "[Name](#cfn-kendraranking-executionplan-name)" : {{String}},
      "[Tags](#cfn-kendraranking-executionplan-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kendraranking-executionplan-syntax.yaml"></a>

```
Type: AWS::KendraRanking::ExecutionPlan
Properties:
  [CapacityUnits](#cfn-kendraranking-executionplan-capacityunits): {{
    CapacityUnitsConfiguration}}
  [Description](#cfn-kendraranking-executionplan-description): {{String}}
  [Name](#cfn-kendraranking-executionplan-name): {{String}}
  [Tags](#cfn-kendraranking-executionplan-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kendraranking-executionplan-properties"></a>

`CapacityUnits`  <a name="cfn-kendraranking-executionplan-capacityunits"></a>
You can set additional capacity units to meet the needs of your rescore execution plan. You are given a single capacity unit by default. If you want to use the default capacity, you don't set additional capacity units. For more information on the default capacity and additional capacity units, see [Adjusting capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html).
*Required*: No
*Type*: [CapacityUnitsConfiguration](aws-properties-kendraranking-executionplan-capacityunitsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-kendraranking-executionplan-description"></a>
A description for the rescore execution plan.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kendraranking-executionplan-name"></a>
A name for the rescore execution plan.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kendraranking-executionplan-tags"></a>
A list of key-value pairs that identify or categorize your rescore execution plan. You can also use tags to help control access to the rescore execution plan. Tag keys and values can consist of Unicode letters, digits, white space. They can also consist of underscore, period, colon, equal, plus, and asperand.
*Required*: No
*Type*: Array of [Tag](aws-properties-kendraranking-executionplan-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kendraranking-executionplan-return-values"></a>

### Ref
<a name="aws-resource-kendraranking-executionplan-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the rescore execution plan ID. For example:

 `{"Ref": "rescore-execution-plan-id"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-kendraranking-executionplan-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-kendraranking-executionplan-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the rescore execution plan.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the rescore execution plan.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
