---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12advancedoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12AdvancedOptions
<a name="aws-properties-b2bi-transformer-x12advancedoptions"></a>

Contains advanced options specific to X12 EDI processing, such as splitting large X12 files into smaller units.

## Syntax
<a name="aws-properties-b2bi-transformer-x12advancedoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12advancedoptions-syntax.json"></a>

```
{
  "[SplitOptions](#cfn-b2bi-transformer-x12advancedoptions-splitoptions)" : {{X12SplitOptions}},
  "[ValidationOptions](#cfn-b2bi-transformer-x12advancedoptions-validationoptions)" : {{X12ValidationOptions}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12advancedoptions-syntax.yaml"></a>

```
  [SplitOptions](#cfn-b2bi-transformer-x12advancedoptions-splitoptions): {{
    X12SplitOptions}}
  [ValidationOptions](#cfn-b2bi-transformer-x12advancedoptions-validationoptions): {{
    X12ValidationOptions}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12advancedoptions-properties"></a>

`SplitOptions`  <a name="cfn-b2bi-transformer-x12advancedoptions-splitoptions"></a>
Specifies options for splitting X12 EDI files. These options control how large X12 files are divided into smaller, more manageable units.
*Required*: No
*Type*: [X12SplitOptions](aws-properties-b2bi-transformer-x12splitoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValidationOptions`  <a name="cfn-b2bi-transformer-x12advancedoptions-validationoptions"></a>
Specifies validation options for X12 EDI processing. These options control how validation rules are applied during EDI document processing, including custom validation rules for element length constraints, code list validations, and element requirement checks.
*Required*: No
*Type*: [X12ValidationOptions](aws-properties-b2bi-transformer-x12validationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
