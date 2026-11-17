---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-syncconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog SyncConfiguration
<a name="aws-properties-glue-catalog-syncconfiguration"></a>

<a name="aws-properties-glue-catalog-syncconfiguration-description"></a>The `SyncConfiguration` property type specifies Property description not available. for an [AWS::Glue::Catalog](aws-resource-glue-catalog.md).

## Syntax
<a name="aws-properties-glue-catalog-syncconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-syncconfiguration-syntax.json"></a>

```
{
  "[AssetsSyncConfiguration](#cfn-glue-catalog-syncconfiguration-assetssyncconfiguration)" : {{AssetsSyncConfiguration}},
  "[LineageSyncConfiguration](#cfn-glue-catalog-syncconfiguration-lineagesyncconfiguration)" : {{LineageSyncConfiguration}},
  "[RoleArn](#cfn-glue-catalog-syncconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-syncconfiguration-syntax.yaml"></a>

```
  [AssetsSyncConfiguration](#cfn-glue-catalog-syncconfiguration-assetssyncconfiguration): {{
    AssetsSyncConfiguration}}
  [LineageSyncConfiguration](#cfn-glue-catalog-syncconfiguration-lineagesyncconfiguration): {{
    LineageSyncConfiguration}}
  [RoleArn](#cfn-glue-catalog-syncconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-syncconfiguration-properties"></a>

`AssetsSyncConfiguration`  <a name="cfn-glue-catalog-syncconfiguration-assetssyncconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [AssetsSyncConfiguration](aws-properties-glue-catalog-assetssyncconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineageSyncConfiguration`  <a name="cfn-glue-catalog-syncconfiguration-lineagesyncconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [LineageSyncConfiguration](aws-properties-glue-catalog-lineagesyncconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-glue-catalog-syncconfiguration-rolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
