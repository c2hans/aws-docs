---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-numberattributeconstraints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool NumberAttributeConstraints
<a name="aws-properties-cognito-userpool-numberattributeconstraints"></a>

The minimum and maximum values of an attribute that is of the number type, for example `custom:age`.

## Syntax
<a name="aws-properties-cognito-userpool-numberattributeconstraints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-numberattributeconstraints-syntax.json"></a>

```
{
  "[MaxValue](#cfn-cognito-userpool-numberattributeconstraints-maxvalue)" : {{String}},
  "[MinValue](#cfn-cognito-userpool-numberattributeconstraints-minvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-numberattributeconstraints-syntax.yaml"></a>

```
  [MaxValue](#cfn-cognito-userpool-numberattributeconstraints-maxvalue): {{String}}
  [MinValue](#cfn-cognito-userpool-numberattributeconstraints-minvalue): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-numberattributeconstraints-properties"></a>

`MaxValue`  <a name="cfn-cognito-userpool-numberattributeconstraints-maxvalue"></a>
The maximum length of a number attribute value. Must be a number less than or equal to `2^1023`, represented as a string with a length of 131072 characters or fewer.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValue`  <a name="cfn-cognito-userpool-numberattributeconstraints-minvalue"></a>
The minimum value of an attribute that is of the number data type.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
