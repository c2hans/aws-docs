---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-salesforcecrawlerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SalesforceCrawlerConfiguration
<a name="aws-properties-bedrock-datasource-salesforcecrawlerconfiguration"></a>

The configuration of the Salesforce content. For example, configuring specific types of Salesforce content.

## Syntax
<a name="aws-properties-bedrock-datasource-salesforcecrawlerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-salesforcecrawlerconfiguration-syntax.json"></a>

```
{
  "[FilterConfiguration](#cfn-bedrock-datasource-salesforcecrawlerconfiguration-filterconfiguration)" : {{CrawlFilterConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-salesforcecrawlerconfiguration-syntax.yaml"></a>

```
  [FilterConfiguration](#cfn-bedrock-datasource-salesforcecrawlerconfiguration-filterconfiguration): {{
    CrawlFilterConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-salesforcecrawlerconfiguration-properties"></a>

`FilterConfiguration`  <a name="cfn-bedrock-datasource-salesforcecrawlerconfiguration-filterconfiguration"></a>
The configuration of filtering the Salesforce content. For example, configuring regular expression patterns to include or exclude certain content.
*Required*: No
*Type*: [CrawlFilterConfiguration](aws-properties-bedrock-datasource-crawlfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
