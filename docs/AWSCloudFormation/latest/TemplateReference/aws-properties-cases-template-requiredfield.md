---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-template-requiredfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Template RequiredField
<a name="aws-properties-cases-template-requiredfield"></a>

List of fields that must have a value provided to create a case.

## Syntax
<a name="aws-properties-cases-template-requiredfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-template-requiredfield-syntax.json"></a>

```
{
  "[FieldId](#cfn-cases-template-requiredfield-fieldid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-template-requiredfield-syntax.yaml"></a>

```
  [FieldId](#cfn-cases-template-requiredfield-fieldid): {{String}}
```

## Properties
<a name="aws-properties-cases-template-requiredfield-properties"></a>

`FieldId`  <a name="cfn-cases-template-requiredfield-fieldid"></a>
Unique identifier of a field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
