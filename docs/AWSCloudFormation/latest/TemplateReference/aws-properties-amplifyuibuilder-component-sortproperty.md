---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-component-sortproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Component SortProperty
<a name="aws-properties-amplifyuibuilder-component-sortproperty"></a>

The `SortProperty` property specifies how to sort the data that you bind to a component.

## Syntax
<a name="aws-properties-amplifyuibuilder-component-sortproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-component-sortproperty-syntax.json"></a>

```
{
  "[Direction](#cfn-amplifyuibuilder-component-sortproperty-direction)" : {{String}},
  "[Field](#cfn-amplifyuibuilder-component-sortproperty-field)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-component-sortproperty-syntax.yaml"></a>

```
  [Direction](#cfn-amplifyuibuilder-component-sortproperty-direction): {{String}}
  [Field](#cfn-amplifyuibuilder-component-sortproperty-field): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-component-sortproperty-properties"></a>

`Direction`  <a name="cfn-amplifyuibuilder-component-sortproperty-direction"></a>
The direction of the sort, either ascending or descending.
*Required*: Yes
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Field`  <a name="cfn-amplifyuibuilder-component-sortproperty-field"></a>
The field to perform the sort on.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
