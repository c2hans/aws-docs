---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel AssetPropertyBindingValue
<a name="aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue"></a>

Represents a data binding value referencing a specific asset property. It's used to bind computation model variables to actual asset property values for processing.

## Syntax
<a name="aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue-syntax.json"></a>

```
{
  "[AssetId](#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-assetid)" : {{String}},
  "[PropertyId](#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-propertyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue-syntax.yaml"></a>

```
  [AssetId](#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-assetid): {{String}}
  [PropertyId](#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-propertyid): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue-properties"></a>

`AssetId`  <a name="cfn-iotsitewise-computationmodel-assetpropertybindingvalue-assetid"></a>
The ID of the asset containing the property. This identifies the specific asset instance's property value used in the computation model.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyId`  <a name="cfn-iotsitewise-computationmodel-assetpropertybindingvalue-propertyid"></a>
The ID of the property within the asset. This identifies the specific property's value used in the computation model.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
