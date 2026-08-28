---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-confluencedatasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ConfluenceDataSourceConfiguration
<a name="aws-properties-bedrock-datasource-confluencedatasourceconfiguration"></a>

The configuration information to connect to Confluence as your data source for self-managed knowledge bases.

## Syntax
<a name="aws-properties-bedrock-datasource-confluencedatasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-confluencedatasourceconfiguration-syntax.json"></a>

```
{
  "[CrawlerConfiguration](#cfn-bedrock-datasource-confluencedatasourceconfiguration-crawlerconfiguration)" : {{ConfluenceCrawlerConfiguration}},
  "[SourceConfiguration](#cfn-bedrock-datasource-confluencedatasourceconfiguration-sourceconfiguration)" : {{ConfluenceSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-confluencedatasourceconfiguration-syntax.yaml"></a>

```
  [CrawlerConfiguration](#cfn-bedrock-datasource-confluencedatasourceconfiguration-crawlerconfiguration): {{
    ConfluenceCrawlerConfiguration}}
  [SourceConfiguration](#cfn-bedrock-datasource-confluencedatasourceconfiguration-sourceconfiguration): {{
    ConfluenceSourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-confluencedatasourceconfiguration-properties"></a>

`CrawlerConfiguration`  <a name="cfn-bedrock-datasource-confluencedatasourceconfiguration-crawlerconfiguration"></a>
The configuration of the Confluence content. For example, configuring specific types of Confluence content.
*Required*: No
*Type*: [ConfluenceCrawlerConfiguration](aws-properties-bedrock-datasource-confluencecrawlerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConfiguration`  <a name="cfn-bedrock-datasource-confluencedatasourceconfiguration-sourceconfiguration"></a>
The endpoint information to connect to your Confluence data source.
*Required*: Yes
*Type*: [ConfluenceSourceConfiguration](aws-properties-bedrock-datasource-confluencesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
