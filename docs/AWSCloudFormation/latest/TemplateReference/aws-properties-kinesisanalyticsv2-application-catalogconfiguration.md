---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application CatalogConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-catalogconfiguration"></a>

The configuration parameters for the default Amazon Glue database. You use this database for SQL queries that you write in a Kinesis Data Analytics Studio notebook.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-catalogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-catalogconfiguration-syntax.json"></a>

```
{
  "[GlueDataCatalogConfiguration](#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration)" : {{GlueDataCatalogConfiguration}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-catalogconfiguration-syntax.yaml"></a>

```
  [GlueDataCatalogConfiguration](#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration): {{
    GlueDataCatalogConfiguration}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-catalogconfiguration-properties"></a>

`GlueDataCatalogConfiguration`  <a name="cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration"></a>
The configuration parameters for the default Amazon Glue database. You use this database for Apache Flink SQL queries and table API transforms that you write in a Kinesis Data Analytics Studio notebook.
*Required*: No
*Type*: [GlueDataCatalogConfiguration](aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
