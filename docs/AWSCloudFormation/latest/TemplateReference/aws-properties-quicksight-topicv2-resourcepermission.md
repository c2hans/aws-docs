---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topicv2-resourcepermission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::TopicV2 ResourcePermission
<a name="aws-properties-quicksight-topicv2-resourcepermission"></a>

<a name="aws-properties-quicksight-topicv2-resourcepermission-description"></a>The `ResourcePermission` property type specifies Property description not available. for an [AWS::QuickSight::TopicV2](aws-resource-quicksight-topicv2.md).

## Syntax
<a name="aws-properties-quicksight-topicv2-resourcepermission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topicv2-resourcepermission-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-topicv2-resourcepermission-actions)" : {{[ String, ... ]}},
  "[Principal](#cfn-quicksight-topicv2-resourcepermission-principal)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-topicv2-resourcepermission-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-topicv2-resourcepermission-actions): {{
    - String}}
  [Principal](#cfn-quicksight-topicv2-resourcepermission-principal): {{String}}
```

## Properties
<a name="aws-properties-quicksight-topicv2-resourcepermission-properties"></a>

`Actions`  <a name="cfn-quicksight-topicv2-resourcepermission-actions"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-quicksight-topicv2-resourcepermission-principal"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
