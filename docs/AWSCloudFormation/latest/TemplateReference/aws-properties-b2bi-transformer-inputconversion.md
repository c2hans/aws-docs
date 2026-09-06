---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-inputconversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer InputConversion
<a name="aws-properties-b2bi-transformer-inputconversion"></a>

Contains the input formatting options for an inbound transformer (takes an X12-formatted EDI document as input and converts it to JSON or XML.

## Syntax
<a name="aws-properties-b2bi-transformer-inputconversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-inputconversion-syntax.json"></a>

```
{
  "[AdvancedOptions](#cfn-b2bi-transformer-inputconversion-advancedoptions)" : {{AdvancedOptions}},
  "[FormatOptions](#cfn-b2bi-transformer-inputconversion-formatoptions)" : {{FormatOptions}},
  "[FromFormat](#cfn-b2bi-transformer-inputconversion-fromformat)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-inputconversion-syntax.yaml"></a>

```
  [AdvancedOptions](#cfn-b2bi-transformer-inputconversion-advancedoptions): {{
    AdvancedOptions}}
  [FormatOptions](#cfn-b2bi-transformer-inputconversion-formatoptions): {{
    FormatOptions}}
  [FromFormat](#cfn-b2bi-transformer-inputconversion-fromformat): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-inputconversion-properties"></a>

`AdvancedOptions`  <a name="cfn-b2bi-transformer-inputconversion-advancedoptions"></a>
Specifies advanced options for the input conversion process. These options provide additional control over how EDI files are processed during transformation.
*Required*: No
*Type*: [AdvancedOptions](aws-properties-b2bi-transformer-advancedoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormatOptions`  <a name="cfn-b2bi-transformer-inputconversion-formatoptions"></a>
A structure that contains the formatting options for an inbound transformer.
*Required*: No
*Type*: [FormatOptions](aws-properties-b2bi-transformer-formatoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromFormat`  <a name="cfn-b2bi-transformer-inputconversion-fromformat"></a>
The format for the transformer input: currently on `X12` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `X12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
