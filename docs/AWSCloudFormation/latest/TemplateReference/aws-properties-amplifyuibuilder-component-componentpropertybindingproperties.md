---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-component-componentpropertybindingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Component ComponentPropertyBindingProperties
<a name="aws-properties-amplifyuibuilder-component-componentpropertybindingproperties"></a>

The `ComponentPropertyBindingProperties` property specifies a component property to associate with a binding property. This enables exposed properties on the top level component to propagate data to the component's property values.

## Syntax
<a name="aws-properties-amplifyuibuilder-component-componentpropertybindingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-component-componentpropertybindingproperties-syntax.json"></a>

```
{
  "[Field](#cfn-amplifyuibuilder-component-componentpropertybindingproperties-field)" : {{String}},
  "[Property](#cfn-amplifyuibuilder-component-componentpropertybindingproperties-property)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-component-componentpropertybindingproperties-syntax.yaml"></a>

```
  [Field](#cfn-amplifyuibuilder-component-componentpropertybindingproperties-field): {{String}}
  [Property](#cfn-amplifyuibuilder-component-componentpropertybindingproperties-property): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-component-componentpropertybindingproperties-properties"></a>

`Field`  <a name="cfn-amplifyuibuilder-component-componentpropertybindingproperties-field"></a>
The data field to bind the property to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Property`  <a name="cfn-amplifyuibuilder-component-componentpropertybindingproperties-property"></a>
The component property to bind to the data field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
