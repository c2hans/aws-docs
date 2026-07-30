---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-datasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource DataSourceConfiguration
<a name="aws-properties-bedrock-datasource-datasourceconfiguration"></a>

The connection configuration for the data source.

## Syntax
<a name="aws-properties-bedrock-datasource-datasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-datasourceconfiguration-syntax.json"></a>

```
{
  "[ConfluenceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-confluenceconfiguration)" : {{ConfluenceDataSourceConfiguration}},
  "[ManagedKnowledgeBaseConnectorConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-managedknowledgebaseconnectorconfiguration)" : {{ManagedKnowledgeBaseConnectorConfiguration}},
  "[S3Configuration](#cfn-bedrock-datasource-datasourceconfiguration-s3configuration)" : {{S3DataSourceConfiguration}},
  "[SalesforceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-salesforceconfiguration)" : {{SalesforceDataSourceConfiguration}},
  "[SharePointConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-sharepointconfiguration)" : {{SharePointDataSourceConfiguration}},
  "[Type](#cfn-bedrock-datasource-datasourceconfiguration-type)" : {{String}},
  "[WebConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-webconfiguration)" : {{WebDataSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-datasourceconfiguration-syntax.yaml"></a>

```
  [ConfluenceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-confluenceconfiguration): {{
    ConfluenceDataSourceConfiguration}}
  [ManagedKnowledgeBaseConnectorConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-managedknowledgebaseconnectorconfiguration): {{
    ManagedKnowledgeBaseConnectorConfiguration}}
  [S3Configuration](#cfn-bedrock-datasource-datasourceconfiguration-s3configuration): {{
    S3DataSourceConfiguration}}
  [SalesforceConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-salesforceconfiguration): {{
    SalesforceDataSourceConfiguration}}
  [SharePointConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-sharepointconfiguration): {{
    SharePointDataSourceConfiguration}}
  [Type](#cfn-bedrock-datasource-datasourceconfiguration-type): {{String}}
  [WebConfiguration](#cfn-bedrock-datasource-datasourceconfiguration-webconfiguration): {{
    WebDataSourceConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-datasourceconfiguration-properties"></a>

`ConfluenceConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-confluenceconfiguration"></a>
The configuration information to connect to Confluence as your data source for self-managed knowledge bases.
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). Confluence data source connector for self-managed knowledge bases is in preview release and is subject to change.
*Required*: No
*Type*: [ConfluenceDataSourceConfiguration](aws-properties-bedrock-datasource-confluencedatasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedKnowledgeBaseConnectorConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-managedknowledgebaseconnectorconfiguration"></a>
Contains the configuration for a data source that connects a managed knowledge base to a supported data source connector. Specify this object when the data source type is `MANAGED_KNOWLEDGE_BASE_CONNECTOR`.
*Required*: No
*Type*: [ManagedKnowledgeBaseConnectorConfiguration](aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3Configuration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-s3configuration"></a>
The configuration information to connect to Amazon S3 as your data source for self-managed knowledge bases. To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html).
*Required*: No
*Type*: [S3DataSourceConfiguration](aws-properties-bedrock-datasource-s3datasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SalesforceConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-salesforceconfiguration"></a>
The configuration information to connect to Salesforce as your data source.
Salesforce data source connector for self-managed knowledge bases is in preview release and is subject to change.
*Required*: No
*Type*: [SalesforceDataSourceConfiguration](aws-properties-bedrock-datasource-salesforcedatasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharePointConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-sharepointconfiguration"></a>
The configuration information to connect to SharePoint as your data source for self-managed knowledge bases.
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). SharePoint data source connector for self-managed knowledge bases is in preview release and is subject to change.
*Required*: No
*Type*: [SharePointDataSourceConfiguration](aws-properties-bedrock-datasource-sharepointdatasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-datasource-datasourceconfiguration-type"></a>
The type of data source.
*Required*: Yes
*Type*: String
*Allowed values*: `S3 | CONFLUENCE | SALESFORCE | SHAREPOINT | WEB | CUSTOM | REDSHIFT_METADATA | MANAGED_KNOWLEDGE_BASE_CONNECTOR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WebConfiguration`  <a name="cfn-bedrock-datasource-datasourceconfiguration-webconfiguration"></a>
The configuration of web URLs to crawl for your data source. You should be authorized to crawl the URLs.
To configure this data source for managed knowledge bases, use [managedKnowledgeBaseConnectorConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ManagedKnowledgeBaseConnectorConfiguration.html). Web crawler data source connector for self-managed knowledge bases is in preview release and is subject to change.
*Required*: No
*Type*: [WebDataSourceConfiguration](aws-properties-bedrock-datasource-webdatasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
