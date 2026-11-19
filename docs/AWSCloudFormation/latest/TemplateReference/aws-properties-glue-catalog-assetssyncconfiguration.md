---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-assetssyncconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog AssetsSyncConfiguration

<a name="aws-properties-glue-catalog-assetssyncconfiguration-description"></a>The `AssetsSyncConfiguration` property type specifies Property description not available. for an [AWS::Glue::Catalog](aws-resource-glue-catalog.md).

## Syntax
<a name="aws-properties-glue-catalog-assetssyncconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-assetssyncconfiguration-syntax.json"></a>

```
{
  "[ManagedCrawlerDetails](#cfn-glue-catalog-assetssyncconfiguration-managedcrawlerdetails)" : {{ManagedCrawlerDetails}},
  "[RefreshIntervalMinutes](#cfn-glue-catalog-assetssyncconfiguration-refreshintervalminutes)" : {{Integer}},
  "[Status](#cfn-glue-catalog-assetssyncconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-assetssyncconfiguration-syntax.yaml"></a>

```
  [ManagedCrawlerDetails](#cfn-glue-catalog-assetssyncconfiguration-managedcrawlerdetails): {{
    ManagedCrawlerDetails}}
  [RefreshIntervalMinutes](#cfn-glue-catalog-assetssyncconfiguration-refreshintervalminutes): {{Integer}}
  [Status](#cfn-glue-catalog-assetssyncconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-assetssyncconfiguration-properties"></a>

`ManagedCrawlerDetails`  <a name="cfn-glue-catalog-assetssyncconfiguration-managedcrawlerdetails"></a>
Property description not available.
*Required*: No
*Type*: [ManagedCrawlerDetails](aws-properties-glue-catalog-managedcrawlerdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshIntervalMinutes`  <a name="cfn-glue-catalog-assetssyncconfiguration-refreshintervalminutes"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `15`
*Maximum*: `10080`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-glue-catalog-assetssyncconfiguration-status"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
