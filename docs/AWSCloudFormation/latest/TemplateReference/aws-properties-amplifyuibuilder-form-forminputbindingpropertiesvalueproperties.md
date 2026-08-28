---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Form FormInputBindingPropertiesValueProperties
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties"></a>

Represents the data binding configuration for a specific property using data stored in AWS. For AWS connected properties, you can bind a property to data stored in an Amplify DataStore model.

## Syntax
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-syntax.json"></a>

```
{
  "[Model](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-model)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-syntax.yaml"></a>

```
  [Model](#cfn-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-model): {{String}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-properties"></a>

`Model`  <a name="cfn-amplifyuibuilder-form-forminputbindingpropertiesvalueproperties-model"></a>
An Amplify DataStore model.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
