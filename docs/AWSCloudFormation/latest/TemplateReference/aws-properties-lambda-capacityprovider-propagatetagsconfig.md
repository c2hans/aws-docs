---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-propagatetagsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider PropagateTagsConfig
<a name="aws-properties-lambda-capacityprovider-propagatetagsconfig"></a>

Configuration that defines how tags are propagated to managed resources.

## Syntax
<a name="aws-properties-lambda-capacityprovider-propagatetagsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-propagatetagsconfig-syntax.json"></a>

```
{
  "[ExplicitTags](#cfn-lambda-capacityprovider-propagatetagsconfig-explicittags)" : {{[ Tag, ... ]}},
  "[Mode](#cfn-lambda-capacityprovider-propagatetagsconfig-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-propagatetagsconfig-syntax.yaml"></a>

```
  [ExplicitTags](#cfn-lambda-capacityprovider-propagatetagsconfig-explicittags): {{
    - Tag}}
  [Mode](#cfn-lambda-capacityprovider-propagatetagsconfig-mode): {{String}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-propagatetagsconfig-properties"></a>

`ExplicitTags`  <a name="cfn-lambda-capacityprovider-propagatetagsconfig-explicittags"></a>
A list of tags to explicitly propagate to managed resources. Maximum of 40 tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-capacityprovider-tag.md)
*Minimum*: `0`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-lambda-capacityprovider-propagatetagsconfig-mode"></a>
The mode for tag propagation. Use `Explicit` to propagate specific tags, or `None` to disable propagation.
*Required*: No
*Type*: String
*Allowed values*: `None | Explicit`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
