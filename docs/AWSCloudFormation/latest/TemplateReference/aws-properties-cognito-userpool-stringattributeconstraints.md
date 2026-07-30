---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-stringattributeconstraints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool StringAttributeConstraints
<a name="aws-properties-cognito-userpool-stringattributeconstraints"></a>

The minimum and maximum length values of an attribute that is of the string type, for example `custom:department`.

## Syntax
<a name="aws-properties-cognito-userpool-stringattributeconstraints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-stringattributeconstraints-syntax.json"></a>

```
{
  "[MaxLength](#cfn-cognito-userpool-stringattributeconstraints-maxlength)" : {{String}},
  "[MinLength](#cfn-cognito-userpool-stringattributeconstraints-minlength)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-stringattributeconstraints-syntax.yaml"></a>

```
  [MaxLength](#cfn-cognito-userpool-stringattributeconstraints-maxlength): {{String}}
  [MinLength](#cfn-cognito-userpool-stringattributeconstraints-minlength): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-stringattributeconstraints-properties"></a>

`MaxLength`  <a name="cfn-cognito-userpool-stringattributeconstraints-maxlength"></a>
The maximum length of a string attribute value. Must be a number less than or equal to `2^1023`, represented as a string with a length of 131072 characters or fewer.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinLength`  <a name="cfn-cognito-userpool-stringattributeconstraints-minlength"></a>
The minimum length of a string attribute value.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
