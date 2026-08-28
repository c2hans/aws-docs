---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-salesforcedatasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource SalesforceDataSourceConfiguration
<a name="aws-properties-bedrock-datasource-salesforcedatasourceconfiguration"></a>

The configuration information to connect to Salesforce as your data source.

## Syntax
<a name="aws-properties-bedrock-datasource-salesforcedatasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-salesforcedatasourceconfiguration-syntax.json"></a>

```
{
  "[CrawlerConfiguration](#cfn-bedrock-datasource-salesforcedatasourceconfiguration-crawlerconfiguration)" : {{SalesforceCrawlerConfiguration}},
  "[SourceConfiguration](#cfn-bedrock-datasource-salesforcedatasourceconfiguration-sourceconfiguration)" : {{SalesforceSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-salesforcedatasourceconfiguration-syntax.yaml"></a>

```
  [CrawlerConfiguration](#cfn-bedrock-datasource-salesforcedatasourceconfiguration-crawlerconfiguration): {{
    SalesforceCrawlerConfiguration}}
  [SourceConfiguration](#cfn-bedrock-datasource-salesforcedatasourceconfiguration-sourceconfiguration): {{
    SalesforceSourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-salesforcedatasourceconfiguration-properties"></a>

`CrawlerConfiguration`  <a name="cfn-bedrock-datasource-salesforcedatasourceconfiguration-crawlerconfiguration"></a>
The configuration of the Salesforce content. For example, configuring specific types of Salesforce content.
*Required*: No
*Type*: [SalesforceCrawlerConfiguration](aws-properties-bedrock-datasource-salesforcecrawlerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceConfiguration`  <a name="cfn-bedrock-datasource-salesforcedatasourceconfiguration-sourceconfiguration"></a>
The endpoint information to connect to your Salesforce data source.
*Required*: Yes
*Type*: [SalesforceSourceConfiguration](aws-properties-bedrock-datasource-salesforcesourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
