---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-fieldposition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FieldPosition
<a name="aws-properties-amplifyuibuilder-form-fieldposition"></a>

The `FieldPosition` property specifies the field position.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-fieldposition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-fieldposition-syntax.json"></a>

```
{
  "[Below](#cfn-amplifyuibuilder-form-fieldposition-below)" : {{String}},
  "[Fixed](#cfn-amplifyuibuilder-form-fieldposition-fixed)" : {{String}},
  "[RightOf](#cfn-amplifyuibuilder-form-fieldposition-rightof)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-fieldposition-syntax.yaml"></a>

```
  [Below](#cfn-amplifyuibuilder-form-fieldposition-below): {{String}}
  [Fixed](#cfn-amplifyuibuilder-form-fieldposition-fixed): {{String}}
  [RightOf](#cfn-amplifyuibuilder-form-fieldposition-rightof): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-fieldposition-properties"></a>

`Below`  <a name="cfn-amplifyuibuilder-form-fieldposition-below"></a>
The field position is below the field specified by the string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fixed`  <a name="cfn-amplifyuibuilder-form-fieldposition-fixed"></a>
The field position is fixed and doesn't change in relation to other fields.
*Required*: No
*Type*: String
*Allowed values*: `first`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RightOf`  <a name="cfn-amplifyuibuilder-form-fieldposition-rightof"></a>
The field position is to the right of the field specified by the string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
