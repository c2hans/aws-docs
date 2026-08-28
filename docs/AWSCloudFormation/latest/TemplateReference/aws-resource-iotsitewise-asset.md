---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-asset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Asset
<a name="aws-resource-iotsitewise-asset"></a>

Creates an asset from an existing asset model. For more information, see [Creating assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-resource-iotsitewise-asset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-asset-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Asset",
  "Properties" : {
      "[AssetDescription](#cfn-iotsitewise-asset-assetdescription)" : {{String}},
      "[AssetExternalId](#cfn-iotsitewise-asset-assetexternalid)" : {{String}},
      "[AssetHierarchies](#cfn-iotsitewise-asset-assethierarchies)" : {{[ AssetHierarchy, ... ]}},
      "[AssetModelId](#cfn-iotsitewise-asset-assetmodelid)" : {{String}},
      "[AssetName](#cfn-iotsitewise-asset-assetname)" : {{String}},
      "[AssetProperties](#cfn-iotsitewise-asset-assetproperties)" : {{[ AssetProperty, ... ]}},
      "[Tags](#cfn-iotsitewise-asset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-asset-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Asset
Properties:
  [AssetDescription](#cfn-iotsitewise-asset-assetdescription): {{String}}
  [AssetExternalId](#cfn-iotsitewise-asset-assetexternalid): {{String}}
  [AssetHierarchies](#cfn-iotsitewise-asset-assethierarchies): {{
    - AssetHierarchy}}
  [AssetModelId](#cfn-iotsitewise-asset-assetmodelid): {{String}}
  [AssetName](#cfn-iotsitewise-asset-assetname): {{String}}
  [AssetProperties](#cfn-iotsitewise-asset-assetproperties): {{
    - AssetProperty}}
  [Tags](#cfn-iotsitewise-asset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-asset-properties"></a>

`AssetDescription`  <a name="cfn-iotsitewise-asset-assetdescription"></a>
The ID of the asset, in UUID format.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetExternalId`  <a name="cfn-iotsitewise-asset-assetexternalid"></a>
The external ID of the asset model composite model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetHierarchies`  <a name="cfn-iotsitewise-asset-assethierarchies"></a>
A list of asset hierarchies that each contain a `hierarchyId`. A hierarchy specifies allowed parent/child asset relationships.
*Required*: No
*Type*: Array of [AssetHierarchy](aws-properties-iotsitewise-asset-assethierarchy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelId`  <a name="cfn-iotsitewise-asset-assetmodelid"></a>
The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *AWS IoT SiteWise User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetName`  <a name="cfn-iotsitewise-asset-assetname"></a>
A friendly name for the asset.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetProperties`  <a name="cfn-iotsitewise-asset-assetproperties"></a>
The list of asset properties for the asset.
This object doesn't include properties that you define in composite models. You can find composite model properties in the `assetCompositeModels` object.
*Required*: No
*Type*: Array of [AssetProperty](aws-properties-iotsitewise-asset-assetproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-asset-tags"></a>
A list of key-value pairs that contain metadata for the asset. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-asset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-asset-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-asset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`AssetId` and `AssetArn`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-asset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-asset-return-values-fn--getatt-fn--getatt"></a>

`AssetArn`  <a name="AssetArn-fn::getatt"></a>
The ARN of the asset.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`AssetId`  <a name="AssetId-fn::getatt"></a>
The ID of the asset.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
