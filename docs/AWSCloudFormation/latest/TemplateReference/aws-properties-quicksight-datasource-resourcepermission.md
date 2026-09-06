---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-resourcepermission.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource ResourcePermission
<a name="aws-properties-quicksight-datasource-resourcepermission"></a>

Permission for the resource.

## Syntax
<a name="aws-properties-quicksight-datasource-resourcepermission-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-resourcepermission-syntax.json"></a>

```
{
  "[Actions](#cfn-quicksight-datasource-resourcepermission-actions)" : {{[ String, ... ]}},
  "[Principal](#cfn-quicksight-datasource-resourcepermission-principal)" : {{String}},
  "[Resource](#cfn-quicksight-datasource-resourcepermission-resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-resourcepermission-syntax.yaml"></a>

```
  [Actions](#cfn-quicksight-datasource-resourcepermission-actions): {{
    - String}}
  [Principal](#cfn-quicksight-datasource-resourcepermission-principal): {{String}}
  [Resource](#cfn-quicksight-datasource-resourcepermission-resource): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-resourcepermission-properties"></a>

`Actions`  <a name="cfn-quicksight-datasource-resourcepermission-actions"></a>
The IAM action to grant or revoke permissions on.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-quicksight-datasource-resourcepermission-principal"></a>
The Amazon Resource Name (ARN) of the principal. This can be one of the following:
+ The ARN of an Amazon Quick user or group associated with a data source or dataset. (This is common.)
+ The ARN of an Amazon Quick user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)
+ The ARN of an AWS account root: This is an IAM ARN rather than a Quick ARN. Use this option only to share resources (templates) across AWS accounts. (This is less common.)
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-quicksight-datasource-resourcepermission-resource"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
