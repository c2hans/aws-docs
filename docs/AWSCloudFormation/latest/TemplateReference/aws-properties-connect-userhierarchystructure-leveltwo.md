---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-userhierarchystructure-leveltwo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::UserHierarchyStructure LevelTwo
<a name="aws-properties-connect-userhierarchystructure-leveltwo"></a>

The update for level two.

## Syntax
<a name="aws-properties-connect-userhierarchystructure-leveltwo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-userhierarchystructure-leveltwo-syntax.json"></a>

```
{
  "[HierarchyLevelArn](#cfn-connect-userhierarchystructure-leveltwo-hierarchylevelarn)" : {{String}},
  "[HierarchyLevelId](#cfn-connect-userhierarchystructure-leveltwo-hierarchylevelid)" : {{String}},
  "[Name](#cfn-connect-userhierarchystructure-leveltwo-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-userhierarchystructure-leveltwo-syntax.yaml"></a>

```
  [HierarchyLevelArn](#cfn-connect-userhierarchystructure-leveltwo-hierarchylevelarn): {{String}}
  [HierarchyLevelId](#cfn-connect-userhierarchystructure-leveltwo-hierarchylevelid): {{String}}
  [Name](#cfn-connect-userhierarchystructure-leveltwo-name): {{String}}
```

## Properties
<a name="aws-properties-connect-userhierarchystructure-leveltwo-properties"></a>

`HierarchyLevelArn`  <a name="cfn-connect-userhierarchystructure-leveltwo-hierarchylevelarn"></a>
The Amazon Resource Name (ARN) of the hierarchy level.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent-group-level/[-0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyLevelId`  <a name="cfn-connect-userhierarchystructure-leveltwo-hierarchylevelid"></a>
The identifier of the hierarchy level.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-userhierarchystructure-leveltwo-name"></a>
The name of the hierarchy level.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
