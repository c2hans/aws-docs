---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-advancedoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer AdvancedOptions
<a name="aws-properties-b2bi-transformer-advancedoptions"></a>

A structure that contains advanced options for EDI processing. Currently, only X12 advanced options are supported.

## Syntax
<a name="aws-properties-b2bi-transformer-advancedoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-advancedoptions-syntax.json"></a>

```
{
  "[X12](#cfn-b2bi-transformer-advancedoptions-x12)" : {{X12AdvancedOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-advancedoptions-syntax.yaml"></a>

```
  [X12](#cfn-b2bi-transformer-advancedoptions-x12): {{
    X12AdvancedOptions}}
```

## Properties
<a name="aws-properties-b2bi-transformer-advancedoptions-properties"></a>

`X12`  <a name="cfn-b2bi-transformer-advancedoptions-x12"></a>
A structure that contains X12-specific advanced options, such as split options for processing X12 EDI files.
*Required*: No
*Type*: [X12AdvancedOptions](aws-properties-b2bi-transformer-x12advancedoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
