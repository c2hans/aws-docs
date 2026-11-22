---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-lineagesyncconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog LineageSyncConfiguration

<a name="aws-properties-glue-catalog-lineagesyncconfiguration-description"></a>The `LineageSyncConfiguration` property type specifies Property description not available. for an [AWS::Glue::Catalog](aws-resource-glue-catalog.md).

## Syntax
<a name="aws-properties-glue-catalog-lineagesyncconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-lineagesyncconfiguration-syntax.json"></a>

```json
{
  "[ManagedCrawlerDetails](#cfn-glue-catalog-lineagesyncconfiguration-managedcrawlerdetails)" : {{ManagedCrawlerDetails}},
  "[RefreshIntervalMinutes](#cfn-glue-catalog-lineagesyncconfiguration-refreshintervalminutes)" : {{Integer}},
  "[Status](#cfn-glue-catalog-lineagesyncconfiguration-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-lineagesyncconfiguration-syntax.yaml"></a>

```yaml
  [ManagedCrawlerDetails](#cfn-glue-catalog-lineagesyncconfiguration-managedcrawlerdetails): {{
    ManagedCrawlerDetails}}
  [RefreshIntervalMinutes](#cfn-glue-catalog-lineagesyncconfiguration-refreshintervalminutes): {{Integer}}
  [Status](#cfn-glue-catalog-lineagesyncconfiguration-status): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-lineagesyncconfiguration-properties"></a>

`ManagedCrawlerDetails`  <a name="cfn-glue-catalog-lineagesyncconfiguration-managedcrawlerdetails"></a>
Property description not available.
*Required*: No
*Type*: [ManagedCrawlerDetails](aws-properties-glue-catalog-managedcrawlerdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshIntervalMinutes`  <a name="cfn-glue-catalog-lineagesyncconfiguration-refreshintervalminutes"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `15`
*Maximum*: `10080`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-glue-catalog-lineagesyncconfiguration-status"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
