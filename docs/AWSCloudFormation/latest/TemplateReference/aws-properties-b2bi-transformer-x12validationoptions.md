---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12validationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12ValidationOptions
<a name="aws-properties-b2bi-transformer-x12validationoptions"></a>

Contains configuration options for X12 EDI validation. This structure allows you to specify custom validation rules that will be applied during EDI document processing, including element length constraints, code list modifications, and element requirement changes. These validation options provide flexibility to accommodate trading partner-specific requirements while maintaining EDI compliance. The validation rules are applied in addition to standard X12 validation to ensure documents meet both standard and custom requirements.

## Syntax
<a name="aws-properties-b2bi-transformer-x12validationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12validationoptions-syntax.json"></a>

```
{
  "[ValidationRules](#cfn-b2bi-transformer-x12validationoptions-validationrules)" : {{[ X12ValidationRule, ... ]}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12validationoptions-syntax.yaml"></a>

```
  [ValidationRules](#cfn-b2bi-transformer-x12validationoptions-validationrules): {{
    - X12ValidationRule}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12validationoptions-properties"></a>

`ValidationRules`  <a name="cfn-b2bi-transformer-x12validationoptions-validationrules"></a>
Specifies a list of validation rules to apply during EDI document processing. These rules can include code list modifications, element length constraints, and element requirement changes.
*Required*: No
*Type*: Array of [X12ValidationRule](aws-properties-b2bi-transformer-x12validationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
