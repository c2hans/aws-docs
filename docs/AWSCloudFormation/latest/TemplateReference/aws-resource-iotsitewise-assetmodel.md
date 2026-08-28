---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-assetmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel
<a name="aws-resource-iotsitewise-assetmodel"></a>

Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model's property and hierarchy definitions. For more information, see [Defining asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html) in the *AWS IoT SiteWise User Guide*.

You can create three types of asset models, `ASSET_MODEL`, `COMPONENT_MODEL`, or an `INTERFACE`.
+ **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+ **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
+ **INTERFACE** – An interface is a type of model that defines a standard structure that can be applied to different asset models.

## Syntax
<a name="aws-resource-iotsitewise-assetmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-assetmodel-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::AssetModel",
  "Properties" : {
      "[AssetModelCompositeModels](#cfn-iotsitewise-assetmodel-assetmodelcompositemodels)" : {{[ AssetModelCompositeModel, ... ]}},
      "[AssetModelDescription](#cfn-iotsitewise-assetmodel-assetmodeldescription)" : {{String}},
      "[AssetModelExternalId](#cfn-iotsitewise-assetmodel-assetmodelexternalid)" : {{String}},
      "[AssetModelHierarchies](#cfn-iotsitewise-assetmodel-assetmodelhierarchies)" : {{[ AssetModelHierarchy, ... ]}},
      "[AssetModelName](#cfn-iotsitewise-assetmodel-assetmodelname)" : {{String}},
      "[AssetModelProperties](#cfn-iotsitewise-assetmodel-assetmodelproperties)" : {{[ AssetModelProperty, ... ]}},
      "[AssetModelType](#cfn-iotsitewise-assetmodel-assetmodeltype)" : {{String}},
      "[EnforcedAssetModelInterfaceRelationships](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationships)" : {{[ EnforcedAssetModelInterfaceRelationship, ... ]}},
      "[Tags](#cfn-iotsitewise-assetmodel-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-assetmodel-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::AssetModel
Properties:
  [AssetModelCompositeModels](#cfn-iotsitewise-assetmodel-assetmodelcompositemodels): {{
    - AssetModelCompositeModel}}
  [AssetModelDescription](#cfn-iotsitewise-assetmodel-assetmodeldescription): {{String}}
  [AssetModelExternalId](#cfn-iotsitewise-assetmodel-assetmodelexternalid): {{String}}
  [AssetModelHierarchies](#cfn-iotsitewise-assetmodel-assetmodelhierarchies): {{
    - AssetModelHierarchy}}
  [AssetModelName](#cfn-iotsitewise-assetmodel-assetmodelname): {{String}}
  [AssetModelProperties](#cfn-iotsitewise-assetmodel-assetmodelproperties): {{
    - AssetModelProperty}}
  [AssetModelType](#cfn-iotsitewise-assetmodel-assetmodeltype): {{String}}
  [EnforcedAssetModelInterfaceRelationships](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationships): {{
    - EnforcedAssetModelInterfaceRelationship}}
  [Tags](#cfn-iotsitewise-assetmodel-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-assetmodel-properties"></a>

`AssetModelCompositeModels`  <a name="cfn-iotsitewise-assetmodel-assetmodelcompositemodels"></a>
The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.
When creating custom composite models, you need to use [CreateAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html). For more information, see [Creating custom composite models (Components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [AssetModelCompositeModel](aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelDescription`  <a name="cfn-iotsitewise-assetmodel-assetmodeldescription"></a>
A description for the asset model.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelExternalId`  <a name="cfn-iotsitewise-assetmodel-assetmodelexternalid"></a>
The external ID of the asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_][a-zA-Z_\-0-9.:]*[a-zA-Z0-9_]+`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelHierarchies`  <a name="cfn-iotsitewise-assetmodel-assetmodelhierarchies"></a>
The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *AWS IoT SiteWise User Guide*.
You can specify up to 10 hierarchies per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [AssetModelHierarchy](aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelName`  <a name="cfn-iotsitewise-assetmodel-assetmodelname"></a>
A unique name for the asset model.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelProperties`  <a name="cfn-iotsitewise-assetmodel-assetmodelproperties"></a>
The property definitions of the asset model. For more information, see [Asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html) in the *AWS IoT SiteWise User Guide*.
You can specify up to 200 properties per asset model. For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [AssetModelProperty](aws-properties-iotsitewise-assetmodel-assetmodelproperty.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelType`  <a name="cfn-iotsitewise-assetmodel-assetmodeltype"></a>
The type of asset model.
+ **ASSET\_MODEL** – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
+ **COMPONENT\_MODEL** – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
+ **INTERFACE** – An interface is a type of model that defines a standard structure that can be applied to different asset models.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnforcedAssetModelInterfaceRelationships`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationships"></a>
Property description not available.
*Required*: No
*Type*: Array of [EnforcedAssetModelInterfaceRelationship](aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-assetmodel-tags"></a>
A list of key-value pairs that contain metadata for the asset. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-assetmodel-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-assetmodel-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-assetmodel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `AssetModelId`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-assetmodel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-assetmodel-return-values-fn--getatt-fn--getatt"></a>

`AssetModelId`  <a name="AssetModelId-fn::getatt"></a>
The ID of the asset model.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
