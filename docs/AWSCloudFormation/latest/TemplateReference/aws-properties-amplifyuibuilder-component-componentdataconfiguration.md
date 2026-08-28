---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplifyuibuilder-component-componentdataconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::Component ComponentDataConfiguration
<a name="aws-properties-amplifyuibuilder-component-componentdataconfiguration"></a>

The `ComponentDataConfiguration` property specifies the configuration for binding a component's properties to data.

## Syntax
<a name="aws-properties-amplifyuibuilder-component-componentdataconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplifyuibuilder-component-componentdataconfiguration-syntax.json"></a>

```
{
  "[Identifiers](#cfn-amplifyuibuilder-component-componentdataconfiguration-identifiers)" : {{[ String, ... ]}},
  "[Model](#cfn-amplifyuibuilder-component-componentdataconfiguration-model)" : {{String}},
  "[Predicate](#cfn-amplifyuibuilder-component-componentdataconfiguration-predicate)" : {{Predicate}},
  "[Sort](#cfn-amplifyuibuilder-component-componentdataconfiguration-sort)" : {{[ SortProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-amplifyuibuilder-component-componentdataconfiguration-syntax.yaml"></a>

```
  [Identifiers](#cfn-amplifyuibuilder-component-componentdataconfiguration-identifiers): {{
    - String}}
  [Model](#cfn-amplifyuibuilder-component-componentdataconfiguration-model): {{String}}
  [Predicate](#cfn-amplifyuibuilder-component-componentdataconfiguration-predicate): {{
    Predicate}}
  [Sort](#cfn-amplifyuibuilder-component-componentdataconfiguration-sort): {{
    - SortProperty}}
```

## Properties
<a name="aws-properties-amplifyuibuilder-component-componentdataconfiguration-properties"></a>

`Identifiers`  <a name="cfn-amplifyuibuilder-component-componentdataconfiguration-identifiers"></a>
A list of IDs to use to bind data to a component. Use this property to bind specifically chosen data, rather than data retrieved from a query.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-amplifyuibuilder-component-componentdataconfiguration-model"></a>
The name of the data model to use to bind data to a component.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Predicate`  <a name="cfn-amplifyuibuilder-component-componentdataconfiguration-predicate"></a>
Represents the conditional logic to use when binding data to a component. Use this property to retrieve only a subset of the data in a collection.
*Required*: No
*Type*: [Predicate](aws-properties-amplifyuibuilder-component-predicate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sort`  <a name="cfn-amplifyuibuilder-component-componentdataconfiguration-sort"></a>
Describes how to sort the component's properties.
*Required*: No
*Type*: Array of [SortProperty](aws-properties-amplifyuibuilder-component-sortproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
