---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftQueryEngineConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration"></a>

Contains configurations for an Amazon Redshift query engine. Specify the type of query engine in `type` and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration-syntax.json"></a>

```
{
  "[ProvisionedConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-provisionedconfiguration)" : {{RedshiftProvisionedConfiguration}},
  "[ServerlessConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-serverlessconfiguration)" : {{RedshiftServerlessConfiguration}},
  "[Type](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration-syntax.yaml"></a>

```
  [ProvisionedConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-provisionedconfiguration): {{
    RedshiftProvisionedConfiguration}}
  [ServerlessConfiguration](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-serverlessconfiguration): {{
    RedshiftServerlessConfiguration}}
  [Type](#cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineconfiguration-properties"></a>

`ProvisionedConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-provisionedconfiguration"></a>
Specifies configurations for a provisioned Amazon Redshift query engine.
*Required*: No
*Type*: [RedshiftProvisionedConfiguration](aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerlessConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-serverlessconfiguration"></a>
Specifies configurations for a serverless Amazon Redshift query engine.
*Required*: No
*Type*: [RedshiftServerlessConfiguration](aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineconfiguration-type"></a>
The type of query engine.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVERLESS | PROVISIONED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
