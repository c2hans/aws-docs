---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet Tag
<a name="aws-properties-gamelift-fleet-tag"></a>

A label that you can assign to a Amazon GameLift Servers resource.

 **Learn more**

[Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*

 [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Syntax
<a name="aws-properties-gamelift-fleet-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-tag-syntax.json"></a>

```
{
  "[Key](#cfn-gamelift-fleet-tag-key)" : {{String}},
  "[Value](#cfn-gamelift-fleet-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-tag-syntax.yaml"></a>

```
  [Key](#cfn-gamelift-fleet-tag-key): {{String}}
  [Value](#cfn-gamelift-fleet-tag-value): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-tag-properties"></a>

`Key`  <a name="cfn-gamelift-fleet-tag-key"></a>
The key for a developer-defined key value pair for tagging an AWS resource.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-gamelift-fleet-tag-value"></a>
The value for a developer-defined key value pair for tagging an AWS resource.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
