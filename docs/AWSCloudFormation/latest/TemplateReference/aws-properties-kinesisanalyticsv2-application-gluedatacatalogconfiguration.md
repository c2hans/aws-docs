---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application GlueDataCatalogConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration"></a>

The configuration of the Glue Data Catalog that you use for Apache Flink SQL queries and table API transforms that you write in an application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration-syntax.json"></a>

```
{
  "[DatabaseARN](#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration-syntax.yaml"></a>

```
  [DatabaseARN](#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration-properties"></a>

`DatabaseARN`  <a name="cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn"></a>
The Amazon Resource Name (ARN) of the database.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
