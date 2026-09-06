---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-userhierarchystructure-levelfour.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::UserHierarchyStructure LevelFour
<a name="aws-properties-connect-userhierarchystructure-levelfour"></a>

The update for level four.

## Syntax
<a name="aws-properties-connect-userhierarchystructure-levelfour-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-userhierarchystructure-levelfour-syntax.json"></a>

```
{
  "[HierarchyLevelArn](#cfn-connect-userhierarchystructure-levelfour-hierarchylevelarn)" : {{String}},
  "[HierarchyLevelId](#cfn-connect-userhierarchystructure-levelfour-hierarchylevelid)" : {{String}},
  "[Name](#cfn-connect-userhierarchystructure-levelfour-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-userhierarchystructure-levelfour-syntax.yaml"></a>

```
  [HierarchyLevelArn](#cfn-connect-userhierarchystructure-levelfour-hierarchylevelarn): {{String}}
  [HierarchyLevelId](#cfn-connect-userhierarchystructure-levelfour-hierarchylevelid): {{String}}
  [Name](#cfn-connect-userhierarchystructure-levelfour-name): {{String}}
```

## Properties
<a name="aws-properties-connect-userhierarchystructure-levelfour-properties"></a>

`HierarchyLevelArn`  <a name="cfn-connect-userhierarchystructure-levelfour-hierarchylevelarn"></a>
The Amazon Resource Name (ARN) of the hierarchy level.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent-group-level/[-0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyLevelId`  <a name="cfn-connect-userhierarchystructure-levelfour-hierarchylevelid"></a>
The identifier of the hierarchy level.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-userhierarchystructure-levelfour-name"></a>
The name of the hierarchy level.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
