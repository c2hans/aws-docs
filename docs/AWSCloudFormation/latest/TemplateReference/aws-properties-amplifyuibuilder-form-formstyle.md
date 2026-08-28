---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-formstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormStyle
<a name="aws-properties-amplifyuibuilder-form-formstyle"></a>

The `FormStyle` property specifies the configuration for the form's style.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-formstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-formstyle-syntax.json"></a>

```
{
  "[HorizontalGap](#cfn-amplifyuibuilder-form-formstyle-horizontalgap)" : {{FormStyleConfig}},
  "[OuterPadding](#cfn-amplifyuibuilder-form-formstyle-outerpadding)" : {{FormStyleConfig}},
  "[VerticalGap](#cfn-amplifyuibuilder-form-formstyle-verticalgap)" : {{FormStyleConfig}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-formstyle-syntax.yaml"></a>

```
  [HorizontalGap](#cfn-amplifyuibuilder-form-formstyle-horizontalgap): {{
    FormStyleConfig}}
  [OuterPadding](#cfn-amplifyuibuilder-form-formstyle-outerpadding): {{
    FormStyleConfig}}
  [VerticalGap](#cfn-amplifyuibuilder-form-formstyle-verticalgap): {{
    FormStyleConfig}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-formstyle-properties"></a>

`HorizontalGap`  <a name="cfn-amplifyuibuilder-form-formstyle-horizontalgap"></a>
The spacing for the horizontal gap.
*Required*: No
*Type*: [FormStyleConfig](aws-properties-amplifyuibuilder-form-formstyleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OuterPadding`  <a name="cfn-amplifyuibuilder-form-formstyle-outerpadding"></a>
The size of the outer padding for the form.
*Required*: No
*Type*: [FormStyleConfig](aws-properties-amplifyuibuilder-form-formstyleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerticalGap`  <a name="cfn-amplifyuibuilder-form-formstyle-verticalgap"></a>
The spacing for the vertical gap.
*Required*: No
*Type*: [FormStyleConfig](aws-properties-amplifyuibuilder-form-formstyleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
