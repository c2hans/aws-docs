---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-formstyleconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormStyleConfig
<a name="aws-properties-amplifyuibuilder-form-formstyleconfig"></a>

The `FormStyleConfig` property specifies the configuration settings for the form's style properties.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-formstyleconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-formstyleconfig-syntax.json"></a>

```
{
  "[TokenReference](#cfn-amplifyuibuilder-form-formstyleconfig-tokenreference)" : {{String}},
  "[Value](#cfn-amplifyuibuilder-form-formstyleconfig-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-formstyleconfig-syntax.yaml"></a>

```
  [TokenReference](#cfn-amplifyuibuilder-form-formstyleconfig-tokenreference): {{String}}
  [Value](#cfn-amplifyuibuilder-form-formstyleconfig-value): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-formstyleconfig-properties"></a>

`TokenReference`  <a name="cfn-amplifyuibuilder-form-formstyleconfig-tokenreference"></a>
A reference to a design token to use to bind the form's style properties to an existing theme.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-amplifyuibuilder-form-formstyleconfig-value"></a>
The value of the style setting.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
