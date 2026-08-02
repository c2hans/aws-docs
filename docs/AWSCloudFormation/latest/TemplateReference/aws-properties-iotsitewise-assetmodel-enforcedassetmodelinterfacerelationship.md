---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel EnforcedAssetModelInterfaceRelationship
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship"></a>

Contains information about applied interface hierarchy and asset model hierarchy

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-syntax.json"></a>

```
{
  "[InterfaceAssetModelId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-interfaceassetmodelid)" : {{String}},
  "[PropertyMappings](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-propertymappings)" : {{[ EnforcedAssetModelInterfacePropertyMapping, ... ]}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-syntax.yaml"></a>

```
  [InterfaceAssetModelId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-interfaceassetmodelid): {{String}}
  [PropertyMappings](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-propertymappings): {{
    - EnforcedAssetModelInterfacePropertyMapping}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-properties"></a>

`InterfaceAssetModelId`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-interfaceassetmodelid"></a>
The ID of the asset model that has the interface applied to it.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropertyMappings`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-propertymappings"></a>
A list of property mappings between the interface asset model and the asset model where the interface is applied.
*Required*: No
*Type*: Array of [EnforcedAssetModelInterfacePropertyMapping](aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
