---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-sharepointdatasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SharePointDataSourceConfiguration
<a name="aws-properties-bedrock-datasource-sharepointdatasourceconfiguration"></a>

The configuration information to connect to SharePoint as your data source for self-managed knowledge bases.

## Syntax
<a name="aws-properties-bedrock-datasource-sharepointdatasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-sharepointdatasourceconfiguration-syntax.json"></a>

```
{
  "[CrawlerConfiguration](#cfn-bedrock-datasource-sharepointdatasourceconfiguration-crawlerconfiguration)" : {{SharePointCrawlerConfiguration}},
  "[SourceConfiguration](#cfn-bedrock-datasource-sharepointdatasourceconfiguration-sourceconfiguration)" : {{SharePointSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-sharepointdatasourceconfiguration-syntax.yaml"></a>

```
  [CrawlerConfiguration](#cfn-bedrock-datasource-sharepointdatasourceconfiguration-crawlerconfiguration): {{
    SharePointCrawlerConfiguration}}
  [SourceConfiguration](#cfn-bedrock-datasource-sharepointdatasourceconfiguration-sourceconfiguration): {{
    SharePointSourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-sharepointdatasourceconfiguration-properties"></a>

`CrawlerConfiguration`  <a name="cfn-bedrock-datasource-sharepointdatasourceconfiguration-crawlerconfiguration"></a>
The configuration of the SharePoint content. For example, configuring specific types of SharePoint content.
*Required*: No
*Type*: [SharePointCrawlerConfiguration](aws-properties-bedrock-datasource-sharepointcrawlerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConfiguration`  <a name="cfn-bedrock-datasource-sharepointdatasourceconfiguration-sourceconfiguration"></a>
The endpoint information to connect to your SharePoint data source.
*Required*: Yes
*Type*: [SharePointSourceConfiguration](aws-properties-bedrock-datasource-sharepointsourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
