---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Component MutationActionSetStateParameter
<a name="aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter"></a>

Represents the state configuration when an action modifies a property of another element within the same component.

## Syntax
<a name="aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter-syntax.json"></a>

```
{
  "[ComponentName](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-componentname)" : {{String}},
  "[Property](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-property)" : {{String}},
  "[Set](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-set)" : {{ComponentProperty}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter-syntax.yaml"></a>

```
  [ComponentName](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-componentname): {{String}}
  [Property](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-property): {{String}}
  [Set](#cfn-amplifyuibuilder-component-mutationactionsetstateparameter-set): {{
    ComponentProperty}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-component-mutationactionsetstateparameter-properties"></a>

`ComponentName`  <a name="cfn-amplifyuibuilder-component-mutationactionsetstateparameter-componentname"></a>
The name of the component that is being modified.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Property`  <a name="cfn-amplifyuibuilder-component-mutationactionsetstateparameter-property"></a>
The name of the component property to apply the state configuration to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Set`  <a name="cfn-amplifyuibuilder-component-mutationactionsetstateparameter-set"></a>
The state configuration to assign to the property.
*Required*: Yes
*Type*: [ComponentProperty](aws-properties-amplifyuibuilder-component-componentproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
