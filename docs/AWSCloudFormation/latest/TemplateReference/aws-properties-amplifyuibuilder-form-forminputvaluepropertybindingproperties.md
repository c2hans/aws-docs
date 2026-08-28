---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormInputValuePropertyBindingProperties
<a name="aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties"></a>

Associates a form property to a binding property. This enables exposed properties on the top level form to propagate data to the form's property values.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties-syntax.json"></a>

```
{
  "[Field](#cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-field)" : {{String}},
  "[Property](#cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-property)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties-syntax.yaml"></a>

```
  [Field](#cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-field): {{String}}
  [Property](#cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-property): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-forminputvaluepropertybindingproperties-properties"></a>

`Field`  <a name="cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-field"></a>
The data field to bind the property to.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Property`  <a name="cfn-amplifyuibuilder-form-forminputvaluepropertybindingproperties-property"></a>
The form property to bind to the data field.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
