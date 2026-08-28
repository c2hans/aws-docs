---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-webdatasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource WebDataSourceConfiguration
<a name="aws-properties-bedrock-datasource-webdatasourceconfiguration"></a>

The configuration details for the web data source.

## Syntax
<a name="aws-properties-bedrock-datasource-webdatasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-webdatasourceconfiguration-syntax.json"></a>

```
{
  "[CrawlerConfiguration](#cfn-bedrock-datasource-webdatasourceconfiguration-crawlerconfiguration)" : {{WebCrawlerConfiguration}},
  "[SourceConfiguration](#cfn-bedrock-datasource-webdatasourceconfiguration-sourceconfiguration)" : {{WebSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-webdatasourceconfiguration-syntax.yaml"></a>

```
  [CrawlerConfiguration](#cfn-bedrock-datasource-webdatasourceconfiguration-crawlerconfiguration): {{
    WebCrawlerConfiguration}}
  [SourceConfiguration](#cfn-bedrock-datasource-webdatasourceconfiguration-sourceconfiguration): {{
    WebSourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-webdatasourceconfiguration-properties"></a>

`CrawlerConfiguration`  <a name="cfn-bedrock-datasource-webdatasourceconfiguration-crawlerconfiguration"></a>
The Web Crawler configuration details for the web data source.
*Required*: No
*Type*: [WebCrawlerConfiguration](aws-properties-bedrock-datasource-webcrawlerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConfiguration`  <a name="cfn-bedrock-datasource-webdatasourceconfiguration-sourceconfiguration"></a>
The source configuration details for the web data source.
*Required*: Yes
*Type*: [WebSourceConfiguration](aws-properties-bedrock-datasource-websourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
