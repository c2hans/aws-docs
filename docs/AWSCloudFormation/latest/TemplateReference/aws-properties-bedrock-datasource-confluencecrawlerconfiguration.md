---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-confluencecrawlerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ConfluenceCrawlerConfiguration
<a name="aws-properties-bedrock-datasource-confluencecrawlerconfiguration"></a>

The configuration of the Confluence content. For example, configuring specific types of Confluence content.

## Syntax
<a name="aws-properties-bedrock-datasource-confluencecrawlerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-confluencecrawlerconfiguration-syntax.json"></a>

```
{
  "[FilterConfiguration](#cfn-bedrock-datasource-confluencecrawlerconfiguration-filterconfiguration)" : {{CrawlFilterConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-confluencecrawlerconfiguration-syntax.yaml"></a>

```
  [FilterConfiguration](#cfn-bedrock-datasource-confluencecrawlerconfiguration-filterconfiguration): {{
    CrawlFilterConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-confluencecrawlerconfiguration-properties"></a>

`FilterConfiguration`  <a name="cfn-bedrock-datasource-confluencecrawlerconfiguration-filterconfiguration"></a>
The configuration of filtering the Confluence content. For example, configuring regular expression patterns to include or exclude certain content.
*Required*: No
*Type*: [CrawlFilterConfiguration](aws-properties-bedrock-datasource-crawlfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
