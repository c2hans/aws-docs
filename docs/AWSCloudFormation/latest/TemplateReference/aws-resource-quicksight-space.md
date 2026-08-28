---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-space.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Space
<a name="aws-resource-quicksight-space"></a>

<a name="aws-resource-quicksight-space-description"></a>The `AWS::QuickSight::Space` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-space-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-space-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Space",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-space-awsaccountid)" : {{String}},
      "[Description](#cfn-quicksight-space-description)" : {{String}},
      "[Name](#cfn-quicksight-space-name)" : {{String}},
      "[Permissions](#cfn-quicksight-space-permissions)" : {{[ ResourcePermission, ... ]}},
      "[Resources](#cfn-quicksight-space-resources)" : {{[ SpaceResource, ... ]}},
      "[SpaceId](#cfn-quicksight-space-spaceid)" : {{String}},
      "[Tags](#cfn-quicksight-space-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-space-syntax.yaml"></a>

```
Type: AWS::QuickSight::Space
Properties:
  [AwsAccountId](#cfn-quicksight-space-awsaccountid): {{String}}
  [Description](#cfn-quicksight-space-description): {{String}}
  [Name](#cfn-quicksight-space-name): {{String}}
  [Permissions](#cfn-quicksight-space-permissions): {{
    - ResourcePermission}}
  [Resources](#cfn-quicksight-space-resources): {{
    - SpaceResource}}
  [SpaceId](#cfn-quicksight-space-spaceid): {{String}}
  [Tags](#cfn-quicksight-space-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-space-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-space-awsaccountid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-quicksight-space-description"></a>
The description of the space.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-space-name"></a>
The display name of the space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-space-permissions"></a>
Property description not available.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-space-resourcepermission.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-quicksight-space-resources"></a>
The resources in the space.
*Required*: No
*Type*: Array of [SpaceResource](aws-properties-quicksight-space-spaceresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceId`  <a name="cfn-quicksight-space-spaceid"></a>
The ID of the space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-space-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-space-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-space-return-values"></a>

### Ref
<a name="aws-resource-quicksight-space-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-space-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-space-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the space.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the space was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The user name of the principal who created the space.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the space was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
