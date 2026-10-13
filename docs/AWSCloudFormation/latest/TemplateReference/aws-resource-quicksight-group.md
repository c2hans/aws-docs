---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-group.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Group
<a name="aws-resource-quicksight-group"></a>

A *group* in Quick Sight consists of a set of users. You can use groups to make it easier to manage access and security.

## Syntax
<a name="aws-resource-quicksight-group-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-group-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Group",
  "Properties" : {
      "[Description](#cfn-quicksight-group-description)" : {{String}},
      "[GroupName](#cfn-quicksight-group-groupname)" : {{String}},
      "[Namespace](#cfn-quicksight-group-namespace)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-group-syntax.yaml"></a>

```
Type: AWS::QuickSight::Group
Properties:
  [Description](#cfn-quicksight-group-description): {{String}}
  [GroupName](#cfn-quicksight-group-groupname): {{String}}
  [Namespace](#cfn-quicksight-group-namespace): {{String}}
```

## Properties
<a name="aws-resource-quicksight-group-properties"></a>

`Description`  <a name="cfn-quicksight-group-description"></a>
The group description.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupName`  <a name="cfn-quicksight-group-groupname"></a>
The name of the group.
*Required*: Yes
*Type*: String
*Pattern*: `^[\u0020-\u00FF]+$`
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-quicksight-group-namespace"></a>
The namespace that you want the group to be a part of.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]*$`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-quicksight-group-return-values"></a>

### Ref
<a name="aws-resource-quicksight-group-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-group-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-group-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the group.

`PrincipalId`  <a name="PrincipalId-fn::getatt"></a>
The principal ID of the group.
