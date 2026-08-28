---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase SqlKnowledgeBaseConfiguration
<a name="aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration"></a>

Contains configurations for a knowledge base connected to an SQL database. Specify the SQL database type in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration-syntax.json"></a>

```
{
  "[RedshiftConfiguration](#cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-redshiftconfiguration)" : {{RedshiftConfiguration}},
  "[Type](#cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration-syntax.yaml"></a>

```
  [RedshiftConfiguration](#cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-redshiftconfiguration): {{
    RedshiftConfiguration}}
  [Type](#cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-sqlknowledgebaseconfiguration-properties"></a>

`RedshiftConfiguration`  <a name="cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-redshiftconfiguration"></a>
Specifies configurations for a knowledge base connected to an Amazon Redshift database.
*Required*: No
*Type*: [RedshiftConfiguration](aws-properties-bedrock-knowledgebase-redshiftconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-knowledgebase-sqlknowledgebaseconfiguration-type"></a>
The type of SQL database to connect to the knowledge base.
*Required*: Yes
*Type*: String
*Allowed values*: `REDSHIFT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
