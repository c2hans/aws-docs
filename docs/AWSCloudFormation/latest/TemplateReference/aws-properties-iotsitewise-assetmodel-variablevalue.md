---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-variablevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel VariableValue
<a name="aws-properties-iotsitewise-assetmodel-variablevalue"></a>

Identifies a property value used in an expression.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-variablevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-variablevalue-syntax.json"></a>

```
{
  "[HierarchyExternalId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchyexternalid)" : {{String}},
  "[HierarchyId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchyid)" : {{String}},
  "[HierarchyLogicalId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid)" : {{String}},
  "[PropertyExternalId](#cfn-iotsitewise-assetmodel-variablevalue-propertyexternalid)" : {{String}},
  "[PropertyId](#cfn-iotsitewise-assetmodel-variablevalue-propertyid)" : {{String}},
  "[PropertyLogicalId](#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid)" : {{String}},
  "[PropertyPath](#cfn-iotsitewise-assetmodel-variablevalue-propertypath)" : {{[ PropertyPathDefinition, ... ]}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-variablevalue-syntax.yaml"></a>

```
  [HierarchyExternalId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchyexternalid): {{String}}
  [HierarchyId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchyid): {{String}}
  [HierarchyLogicalId](#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid): {{String}}
  [PropertyExternalId](#cfn-iotsitewise-assetmodel-variablevalue-propertyexternalid): {{String}}
  [PropertyId](#cfn-iotsitewise-assetmodel-variablevalue-propertyid): {{String}}
  [PropertyLogicalId](#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid): {{String}}
  [PropertyPath](#cfn-iotsitewise-assetmodel-variablevalue-propertypath): {{
    - PropertyPathDefinition}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-variablevalue-properties"></a>

`HierarchyExternalId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-hierarchyexternalid"></a>
The external ID of the hierarchy being referenced. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-hierarchyid"></a>
The ID of the hierarchy to query for the property ID. You can use the hierarchy's name instead of the hierarchy's ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId`. For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HierarchyLogicalId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid"></a>
The `LogicalID` of the hierarchy to query for the `PropertyLogicalID`.
You use a `hierarchyLogicalID` instead of a model ID because you can have several hierarchies using the same model and therefore the same property. For example, you might have separately grouped assets that come from the same asset model. For more information, see [Defining relationships between asset models (hierarchies)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyExternalId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-propertyexternalid"></a>
The external ID of the property being referenced. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-propertyid"></a>
The ID of the property to use as the variable. You can use the property `name` if it's from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
This is a return value and can't be set.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyLogicalId`  <a name="cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid"></a>
The `LogicalID` of the property that is being referenced.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyPath`  <a name="cfn-iotsitewise-assetmodel-variablevalue-propertypath"></a>
The path of the property. Each step of the path is the name of the step. See the following example:

```
PropertyPath:
  Name: AssetModelName
  Name: Composite1
  Name: NestedComposite
```
*Required*: No
*Type*: Array of [PropertyPathDefinition](aws-properties-iotsitewise-assetmodel-propertypathdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
