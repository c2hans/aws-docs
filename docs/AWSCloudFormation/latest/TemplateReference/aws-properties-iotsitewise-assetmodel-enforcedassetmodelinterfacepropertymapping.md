---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::AssetModel EnforcedAssetModelInterfacePropertyMapping
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping"></a>

Contains information about applied interface property and asset model property

## Syntax
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-syntax.json"></a>

```
{
  "[AssetModelPropertyExternalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertyexternalid)" : {{String}},
  "[AssetModelPropertyLogicalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertylogicalid)" : {{String}},
  "[InterfaceAssetModelPropertyExternalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-interfaceassetmodelpropertyexternalid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-syntax.yaml"></a>

```
  [AssetModelPropertyExternalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertyexternalid): {{String}}
  [AssetModelPropertyLogicalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertylogicalid): {{String}}
  [InterfaceAssetModelPropertyExternalId](#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-interfaceassetmodelpropertyexternalid): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-properties"></a>

`AssetModelPropertyExternalId`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertyexternalid"></a>
The external ID of the linked asset model property
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetModelPropertyLogicalId`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertylogicalid"></a>
The logical ID of the linked asset model property
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceAssetModelPropertyExternalId`  <a name="cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-interfaceassetmodelpropertyexternalid"></a>
The external ID of the applied interface property
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
