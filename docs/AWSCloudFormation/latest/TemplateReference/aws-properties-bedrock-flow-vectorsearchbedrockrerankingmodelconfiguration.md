---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow VectorSearchBedrockRerankingModelConfiguration
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration"></a>

Configuration for the Amazon Bedrock foundation model used for reranking vector search results. This specifies which model to use and any additional parameters required by the model.

## Syntax
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields)" : {{Json}},
  "[ModelArn](#cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields): {{Json}}
  [ModelArn](#cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-modelarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-additionalmodelrequestfields"></a>
A list of additional fields to include in the model request during reranking. These fields provide extra context or configuration options specific to the selected foundation model.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelArn`  <a name="cfn-bedrock-flow-vectorsearchbedrockrerankingmodelconfiguration-modelarn"></a>
The Amazon Resource Name (ARN) of the foundation model to use for reranking. This model processes the query and search results to determine a more relevant ordering.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/(.*))?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
