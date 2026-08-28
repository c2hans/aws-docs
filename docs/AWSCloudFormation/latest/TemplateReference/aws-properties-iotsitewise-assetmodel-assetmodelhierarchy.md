---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel AssetModelHierarchy
<a name="aws-properties-iotsitewise-assetmodel-assetmodelhierarchy"></a>

Describes an asset hierarchy that contains a hierarchy's name, ID, and child asset model ID that specifies the type of asset that can be in this hierarchy.

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-assetmodelhierarchy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-assetmodelhierarchy-syntax.json"></a>

```
{
  "[ChildAssetModelId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid)" : {{String}},
  "[ExternalId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-externalid)" : {{String}},
  "[Id](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-id)" : {{String}},
  "[LogicalId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid)" : {{String}},
  "[Name](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-assetmodelhierarchy-syntax.yaml"></a>

```
  [ChildAssetModelId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid): {{String}}
  [ExternalId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-externalid): {{String}}
  [Id](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-id): {{String}}
  [LogicalId](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid): {{String}}
  [Name](#cfn-iotsitewise-assetmodel-assetmodelhierarchy-name): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-assetmodelhierarchy-properties"></a>

`ChildAssetModelId`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid"></a>
The ID of the asset model, in UUID format. All assets in this hierarchy must be instances of the `childAssetModelId` asset model. AWS IoT SiteWise will always return the actual asset model ID for this value. However, when you are specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html), you may provide either the asset model ID or else `externalId:` followed by the asset model's external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchy-externalid"></a>
The external ID (if any) provided in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) operation. You can assign an external ID by specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html). However, you can't change the external ID if one is already assigned. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
One of `ExternalId` or `LogicalId` must be specified.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchy-id"></a>
The ID of the asset model hierarchy. This ID is a `hierarchyId`.
This is a return value and can't be set.
+ If you are callling [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) to create a *new* hierarchy: You can specify its ID here, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
+ If you are calling UpdateAssetModel to modify an *existing* hierarchy: This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid"></a>
The `LogicalID` of the asset model hierarchy. This ID is a `hierarchyLogicalId`.
One of `ExternalId` or `LogicalId` must be specified.
*Required*: No
*Type*: String
*Pattern*: `[^\u0000-\u001F\u007F]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchy-name"></a>
The name of the asset model hierarchy that you specify by using the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) API operation.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
