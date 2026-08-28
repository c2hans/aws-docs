---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel AssetModelPropertyBindingValue
<a name="aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue"></a>

Contains information about an `assetModelProperty` binding value.

## Syntax
<a name="aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue-syntax.json"></a>

```
{
  "[AssetModelId](#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-assetmodelid)" : {{String}},
  "[PropertyId](#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-propertyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue-syntax.yaml"></a>

```
  [AssetModelId](#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-assetmodelid): {{String}}
  [PropertyId](#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-propertyid): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue-properties"></a>

`AssetModelId`  <a name="cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-assetmodelid"></a>
The ID of the asset model, in UUID format.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyId`  <a name="cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-propertyid"></a>
The ID of the asset model property used in data binding value.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
