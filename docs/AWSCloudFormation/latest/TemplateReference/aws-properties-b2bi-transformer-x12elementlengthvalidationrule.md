---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12elementlengthvalidationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12ElementLengthValidationRule
<a name="aws-properties-b2bi-transformer-x12elementlengthvalidationrule"></a>

Defines a validation rule that specifies custom length constraints for a specific X12 element. This rule allows you to override the standard minimum and maximum length requirements for an element, enabling validation of trading partner-specific length requirements that may differ from the X12 specification. Both minimum and maximum length values must be specified.

## Syntax
<a name="aws-properties-b2bi-transformer-x12elementlengthvalidationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12elementlengthvalidationrule-syntax.json"></a>

```
{
  "[ElementId](#cfn-b2bi-transformer-x12elementlengthvalidationrule-elementid)" : {{String}},
  "[MaxLength](#cfn-b2bi-transformer-x12elementlengthvalidationrule-maxlength)" : {{Number}},
  "[MinLength](#cfn-b2bi-transformer-x12elementlengthvalidationrule-minlength)" : {{Number}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12elementlengthvalidationrule-syntax.yaml"></a>

```
  [ElementId](#cfn-b2bi-transformer-x12elementlengthvalidationrule-elementid): {{String}}
  [MaxLength](#cfn-b2bi-transformer-x12elementlengthvalidationrule-maxlength): {{Number}}
  [MinLength](#cfn-b2bi-transformer-x12elementlengthvalidationrule-minlength): {{Number}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12elementlengthvalidationrule-properties"></a>

`ElementId`  <a name="cfn-b2bi-transformer-x12elementlengthvalidationrule-elementid"></a>
Specifies the four-digit element ID to which the length constraints will be applied. This identifies which X12 element will have its length requirements modified.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{4}$`
*Minimum*: `4`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxLength`  <a name="cfn-b2bi-transformer-x12elementlengthvalidationrule-maxlength"></a>
Specifies the maximum allowed length for the identified element. This value defines the upper limit for the element's content length.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinLength`  <a name="cfn-b2bi-transformer-x12elementlengthvalidationrule-minlength"></a>
Specifies the minimum required length for the identified element. This value defines the lower limit for the element's content length.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `1000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
