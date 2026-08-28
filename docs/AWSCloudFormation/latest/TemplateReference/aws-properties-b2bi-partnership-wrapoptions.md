---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-partnership-wrapoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Partnership WrapOptions
<a name="aws-properties-b2bi-partnership-wrapoptions"></a>

Contains options for wrapping (line folding) in X12 EDI files. Wrapping controls how long lines are handled in the EDI output.

## Syntax
<a name="aws-properties-b2bi-partnership-wrapoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-partnership-wrapoptions-syntax.json"></a>

```
{
  "[LineLength](#cfn-b2bi-partnership-wrapoptions-linelength)" : {{Number}},
  "[LineTerminator](#cfn-b2bi-partnership-wrapoptions-lineterminator)" : {{String}},
  "[WrapBy](#cfn-b2bi-partnership-wrapoptions-wrapby)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-partnership-wrapoptions-syntax.yaml"></a>

```
  [LineLength](#cfn-b2bi-partnership-wrapoptions-linelength): {{Number}}
  [LineTerminator](#cfn-b2bi-partnership-wrapoptions-lineterminator): {{String}}
  [WrapBy](#cfn-b2bi-partnership-wrapoptions-wrapby): {{String}}
```

## Properties
<a name="aws-properties-b2bi-partnership-wrapoptions-properties"></a>

`LineLength`  <a name="cfn-b2bi-partnership-wrapoptions-linelength"></a>
Specifies the maximum length of a line before wrapping occurs. This value is used when `wrapBy` is set to `LINE_LENGTH`.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineTerminator`  <a name="cfn-b2bi-partnership-wrapoptions-lineterminator"></a>
Specifies the character sequence used to terminate lines when wrapping. Valid values:
+ `CRLF`: carriage return and line feed
+ `LF`: line feed)
+ `CR`: carriage return
*Required*: No
*Type*: String
*Allowed values*: `CRLF | LF | CR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WrapBy`  <a name="cfn-b2bi-partnership-wrapoptions-wrapby"></a>
Specifies the method used for wrapping lines in the EDI output. Valid values:
+ `SEGMENT`: Wraps by segment.
+ `ONE_LINE`: Indicates that the entire content is on a single line.
**Note**
When you specify `ONE_LINE`, do not provide either the line length nor the line terminator value.
+ `LINE_LENGTH`: Wraps by character count, as specified by `lineLength` value.
*Required*: No
*Type*: String
*Allowed values*: `SEGMENT | ONE_LINE | LINE_LENGTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
