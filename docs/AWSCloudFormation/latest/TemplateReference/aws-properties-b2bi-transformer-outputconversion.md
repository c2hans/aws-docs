---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-outputconversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer OutputConversion
<a name="aws-properties-b2bi-transformer-outputconversion"></a>

Contains the formatting options for an outbound transformer (takes JSON or XML as input and converts it to an EDI document (currently only X12 format is supported).

## Syntax
<a name="aws-properties-b2bi-transformer-outputconversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-outputconversion-syntax.json"></a>

```
{
  "[AdvancedOptions](#cfn-b2bi-transformer-outputconversion-advancedoptions)" : {{AdvancedOptions}},
  "[FormatOptions](#cfn-b2bi-transformer-outputconversion-formatoptions)" : {{FormatOptions}},
  "[ToFormat](#cfn-b2bi-transformer-outputconversion-toformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-outputconversion-syntax.yaml"></a>

```
  [AdvancedOptions](#cfn-b2bi-transformer-outputconversion-advancedoptions): {{
    AdvancedOptions}}
  [FormatOptions](#cfn-b2bi-transformer-outputconversion-formatoptions): {{
    FormatOptions}}
  [ToFormat](#cfn-b2bi-transformer-outputconversion-toformat): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-outputconversion-properties"></a>

`AdvancedOptions`  <a name="cfn-b2bi-transformer-outputconversion-advancedoptions"></a>
Property description not available.
*Required*: No
*Type*: [AdvancedOptions](aws-properties-b2bi-transformer-advancedoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormatOptions`  <a name="cfn-b2bi-transformer-outputconversion-formatoptions"></a>
A structure that contains the X12 transaction set and version for the transformer output.
*Required*: No
*Type*: [FormatOptions](aws-properties-b2bi-transformer-formatoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToFormat`  <a name="cfn-b2bi-transformer-outputconversion-toformat"></a>
The format for the output from an outbound transformer: only X12 is currently supported.
*Required*: Yes
*Type*: String
*Allowed values*: `X12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
