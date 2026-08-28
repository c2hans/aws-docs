---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-x12delimiters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership X12Delimiters
<a name="aws-properties-b2bi-partnership-x12delimiters"></a>

In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header. The delimiters are part of the message's syntax and divide up its different elements.

## Syntax
<a name="aws-properties-b2bi-partnership-x12delimiters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-x12delimiters-syntax.json"></a>

```
{
  "[ComponentSeparator](#cfn-b2bi-partnership-x12delimiters-componentseparator)" : {{String}},
  "[DataElementSeparator](#cfn-b2bi-partnership-x12delimiters-dataelementseparator)" : {{String}},
  "[SegmentTerminator](#cfn-b2bi-partnership-x12delimiters-segmentterminator)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-x12delimiters-syntax.yaml"></a>

```
  [ComponentSeparator](#cfn-b2bi-partnership-x12delimiters-componentseparator): {{String}}
  [DataElementSeparator](#cfn-b2bi-partnership-x12delimiters-dataelementseparator): {{String}}
  [SegmentTerminator](#cfn-b2bi-partnership-x12delimiters-segmentterminator): {{String}}
```

## Properties
<a name="aws-properties-b2bi-partnership-x12delimiters-properties"></a>

`ComponentSeparator`  <a name="cfn-b2bi-partnership-x12delimiters-componentseparator"></a>
The component, or sub-element, separator. The default value is `:` (colon).
*Required*: No
*Type*: String
*Pattern*: `^[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataElementSeparator`  <a name="cfn-b2bi-partnership-x12delimiters-dataelementseparator"></a>
The data element separator. The default value is `*` (asterisk).
*Required*: No
*Type*: String
*Pattern*: `^[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentTerminator`  <a name="cfn-b2bi-partnership-x12delimiters-segmentterminator"></a>
The segment terminator. The default value is `~` (tilde).
*Required*: No
*Type*: String
*Pattern*: `^[!&'()*+,\-./:;?=%@\[\]_{}|<>~^`"]$`
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
