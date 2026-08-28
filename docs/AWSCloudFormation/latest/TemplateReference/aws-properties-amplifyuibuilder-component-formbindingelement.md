---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-component-formbindingelement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Component FormBindingElement
<a name="aws-properties-amplifyuibuilder-component-formbindingelement"></a>

Describes how to bind a component property to form data.

## Syntax
<a name="aws-properties-amplifyuibuilder-component-formbindingelement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-component-formbindingelement-syntax.json"></a>

```
{
  "[Element](#cfn-amplifyuibuilder-component-formbindingelement-element)" : {{String}},
  "[Property](#cfn-amplifyuibuilder-component-formbindingelement-property)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-component-formbindingelement-syntax.yaml"></a>

```
  [Element](#cfn-amplifyuibuilder-component-formbindingelement-element): {{String}}
  [Property](#cfn-amplifyuibuilder-component-formbindingelement-property): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-component-formbindingelement-properties"></a>

`Element`  <a name="cfn-amplifyuibuilder-component-formbindingelement-element"></a>
The name of the component to retrieve a value from.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Property`  <a name="cfn-amplifyuibuilder-component-formbindingelement-property"></a>
The property to retrieve a value from.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
