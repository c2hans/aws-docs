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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
