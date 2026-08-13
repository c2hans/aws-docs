---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-customentitytype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::CustomEntityType
<a name="aws-resource-glue-customentitytype"></a>

Creates a custom pattern that is used to detect sensitive data across the columns and rows of your structured data.

Each custom pattern you create specifies a regular expression and an optional list of context words. If no context words are passed only a regular expression is checked.

## Syntax
<a name="aws-resource-glue-customentitytype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-customentitytype-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::CustomEntityType",
  "Properties" : {
      "[ContextWords](#cfn-glue-customentitytype-contextwords)" : {{[ String, ... ]}},
      "[Name](#cfn-glue-customentitytype-name)" : {{String}},
      "[RegexString](#cfn-glue-customentitytype-regexstring)" : {{String}},
      "[Tags](#cfn-glue-customentitytype-tags)" : {{[ [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html), ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-customentitytype-syntax.yaml"></a>

```
Type: AWS::Glue::CustomEntityType
Properties:
  [ContextWords](#cfn-glue-customentitytype-contextwords): {{
    - String}}
  [Name](#cfn-glue-customentitytype-name): {{String}}
  [RegexString](#cfn-glue-customentitytype-regexstring): {{
    String}}
  [Tags](#cfn-glue-customentitytype-tags): {{
    - [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)}}
```

## Properties
<a name="aws-resource-glue-customentitytype-properties"></a>

`ContextWords`  <a name="cfn-glue-customentitytype-contextwords"></a>
A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.
If no context words are passed only a regular expression is checked.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-customentitytype-name"></a>
A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per AWS account.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RegexString`  <a name="cfn-glue-customentitytype-regexstring"></a>
A regular expression string that is used for detecting sensitive data in a custom pattern.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-glue-customentitytype-tags"></a>
AWS tags that contain a key value pair and may be searched by console, command line, or API.
*Required*: No
*Type*: Array of [`Tag`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-customentitytype-return-values"></a>

### Ref
<a name="aws-resource-glue-customentitytype-return-values-ref"></a>
