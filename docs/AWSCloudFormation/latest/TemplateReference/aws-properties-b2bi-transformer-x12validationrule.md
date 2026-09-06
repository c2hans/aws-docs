---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12validationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12ValidationRule
<a name="aws-properties-b2bi-transformer-x12validationrule"></a>

Represents a single validation rule that can be applied during X12 EDI processing. This is a union type that can contain one of several specific validation rule types: code list validation rules for modifying allowed element codes, element length validation rules for enforcing custom length constraints, or element requirement validation rules for changing mandatory/optional status. Each validation rule targets specific aspects of EDI document validation to ensure compliance with trading partner requirements and business rules.

## Syntax
<a name="aws-properties-b2bi-transformer-x12validationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12validationrule-syntax.json"></a>

```
{
  "[CodeListValidationRule](#cfn-b2bi-transformer-x12validationrule-codelistvalidationrule)" : {{X12CodeListValidationRule}},
  "[ElementLengthValidationRule](#cfn-b2bi-transformer-x12validationrule-elementlengthvalidationrule)" : {{X12ElementLengthValidationRule}},
  "[ElementRequirementValidationRule](#cfn-b2bi-transformer-x12validationrule-elementrequirementvalidationrule)" : {{X12ElementRequirementValidationRule}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12validationrule-syntax.yaml"></a>

```
  [CodeListValidationRule](#cfn-b2bi-transformer-x12validationrule-codelistvalidationrule): {{
    X12CodeListValidationRule}}
  [ElementLengthValidationRule](#cfn-b2bi-transformer-x12validationrule-elementlengthvalidationrule): {{
    X12ElementLengthValidationRule}}
  [ElementRequirementValidationRule](#cfn-b2bi-transformer-x12validationrule-elementrequirementvalidationrule): {{
    X12ElementRequirementValidationRule}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12validationrule-properties"></a>

`CodeListValidationRule`  <a name="cfn-b2bi-transformer-x12validationrule-codelistvalidationrule"></a>
Specifies a code list validation rule that modifies the allowed code values for a specific X12 element. This rule enables you to customize which codes are considered valid for an element, allowing for trading partner-specific code requirements.
*Required*: No
*Type*: [X12CodeListValidationRule](aws-properties-b2bi-transformer-x12codelistvalidationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementLengthValidationRule`  <a name="cfn-b2bi-transformer-x12validationrule-elementlengthvalidationrule"></a>
Specifies an element length validation rule that defines custom length constraints for a specific X12 element. This rule allows you to enforce minimum and maximum length requirements that may differ from the standard X12 specification.
*Required*: No
*Type*: [X12ElementLengthValidationRule](aws-properties-b2bi-transformer-x12elementlengthvalidationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementRequirementValidationRule`  <a name="cfn-b2bi-transformer-x12validationrule-elementrequirementvalidationrule"></a>
Specifies an element requirement validation rule that modifies whether a specific X12 element is required or optional within a segment. This rule provides flexibility to accommodate different trading partner requirements for element presence.
*Required*: No
*Type*: [X12ElementRequirementValidationRule](aws-properties-b2bi-transformer-x12elementrequirementvalidationrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
