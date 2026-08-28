---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-trigger-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Trigger Condition
<a name="aws-properties-glue-trigger-condition"></a>

Defines a condition under which a trigger fires.

## Syntax
<a name="aws-properties-glue-trigger-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-trigger-condition-syntax.json"></a>

```
{
  "[CrawlerName](#cfn-glue-trigger-condition-crawlername)" : {{String}},
  "[CrawlState](#cfn-glue-trigger-condition-crawlstate)" : {{String}},
  "[JobName](#cfn-glue-trigger-condition-jobname)" : {{String}},
  "[LogicalOperator](#cfn-glue-trigger-condition-logicaloperator)" : {{String}},
  "[State](#cfn-glue-trigger-condition-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-trigger-condition-syntax.yaml"></a>

```
  [CrawlerName](#cfn-glue-trigger-condition-crawlername): {{String}}
  [CrawlState](#cfn-glue-trigger-condition-crawlstate): {{String}}
  [JobName](#cfn-glue-trigger-condition-jobname): {{String}}
  [LogicalOperator](#cfn-glue-trigger-condition-logicaloperator): {{String}}
  [State](#cfn-glue-trigger-condition-state): {{String}}
```

## Properties
<a name="aws-properties-glue-trigger-condition-properties"></a>

`CrawlerName`  <a name="cfn-glue-trigger-condition-crawlername"></a>
The name of the crawler to which this condition applies.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CrawlState`  <a name="cfn-glue-trigger-condition-crawlstate"></a>
The state of the crawler to which this condition applies.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobName`  <a name="cfn-glue-trigger-condition-jobname"></a>
The name of the job whose `JobRuns` this condition applies to, and on which this trigger waits.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalOperator`  <a name="cfn-glue-trigger-condition-logicaloperator"></a>
A logical operator.
*Required*: No
*Type*: String
*Allowed values*: `EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-glue-trigger-condition-state"></a>
The condition state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT`, and `FAILED`.
*Required*: No
*Type*: String
*Allowed values*: `STARTING | RUNNING | STOPPING | STOPPED | SUCCEEDED | FAILED | TIMEOUT | ERROR | WAITING | EXPIRED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-glue-trigger-condition--seealso"></a>
+ [Condition Structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html#aws-glue-api-jobs-trigger-Condition) in the *AWS Glue Developer Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
