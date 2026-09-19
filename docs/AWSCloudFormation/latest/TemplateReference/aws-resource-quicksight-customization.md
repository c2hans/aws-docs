---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-customization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Customization
<a name="aws-resource-quicksight-customization"></a>

Creates Amazon Quick Sight customizations. Currently, you can add a custom default theme by using the `CreateAccountCustomization` or `UpdateAccountCustomization` API operation. To further customize Amazon Quick Sight by removing Amazon Quick Sight sample assets and videos for all new users, see [Customizing Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight.html) in the *Amazon Quick Sight User Guide.*

You can create customizations for your AWS account or, if you specify a namespace, for a Quick Sight namespace instead. Customizations that apply to a namespace always override customizations that apply to an AWS account. To find out which customizations apply, use the `DescribeAccountCustomization` API operation.

Before you use the `CreateAccountCustomization` API operation to add a theme as the namespace default, make sure that you first share the theme with the namespace. If you don't share it with the namespace, the theme isn't visible to your users even if you make it the default theme. To check if the theme is shared, view the current permissions by using the ` [DescribeThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeThemePermissions.html) ` API operation. To share the theme, grant permissions by using the ` [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html) ` API operation.

## Syntax
<a name="aws-resource-quicksight-customization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-customization-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Customization",
  "Properties" : {
      "[DefaultTheme](#cfn-quicksight-customization-defaulttheme)" : {{String}},
      "[Namespace](#cfn-quicksight-customization-namespace)" : {{String}},
      "[Tags](#cfn-quicksight-customization-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-customization-syntax.yaml"></a>

```
Type: AWS::QuickSight::Customization
Properties:
  [DefaultTheme](#cfn-quicksight-customization-defaulttheme): {{String}}
  [Namespace](#cfn-quicksight-customization-namespace): {{String}}
  [Tags](#cfn-quicksight-customization-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-customization-properties"></a>

`DefaultTheme`  <a name="cfn-quicksight-customization-defaulttheme"></a>
The default theme for this Quick Sight subscription.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-quicksight-customization-namespace"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-customization-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-customization-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-customization-return-values"></a>

### Ref
<a name="aws-resource-quicksight-customization-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-customization-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-customization-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AwsAccountId`  <a name="AwsAccountId-fn::getatt"></a>
Property description not available.
