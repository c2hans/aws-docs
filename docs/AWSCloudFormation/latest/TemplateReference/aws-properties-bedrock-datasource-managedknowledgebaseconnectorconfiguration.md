---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ManagedKnowledgeBaseConnectorConfiguration
<a name="aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration"></a>

Configuration for managed knowledge base connector data sources.

## Syntax
<a name="aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration-syntax.json"></a>

```
{
  "[ConnectorParameters](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-connectorparameters)" : {{Json}},
  "[DeletionProtectionConfiguration](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-deletionprotectionconfiguration)" : {{DeletionProtectionConfiguration}},
  "[MediaExtractionConfiguration](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-mediaextractionconfiguration)" : {{MediaExtractionConfiguration}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration-syntax.yaml"></a>

```
  [ConnectorParameters](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-connectorparameters): {{Json}}
  [DeletionProtectionConfiguration](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-deletionprotectionconfiguration): {{
    DeletionProtectionConfiguration}}
  [MediaExtractionConfiguration](#cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-mediaextractionconfiguration): {{
    MediaExtractionConfiguration}}
```

## Properties
<a name="aws-properties-bedrock-datasource-managedknowledgebaseconnectorconfiguration-properties"></a>

`ConnectorParameters`  <a name="cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-connectorparameters"></a>
Connector-specific parameters. For more information, see [Connect a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-connect-ds.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtectionConfiguration`  <a name="cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-deletionprotectionconfiguration"></a>
A safeguard against accidental bulk deletion of indexed content.
*Required*: No
*Type*: [DeletionProtectionConfiguration](aws-properties-bedrock-datasource-deletionprotectionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaExtractionConfiguration`  <a name="cfn-bedrock-datasource-managedknowledgebaseconnectorconfiguration-mediaextractionconfiguration"></a>
Configuration for extracting media (images, audio, video) from data source files.
*Required*: No
*Type*: [MediaExtractionConfiguration](aws-properties-bedrock-datasource-mediaextractionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
