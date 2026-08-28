---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-datasourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DataSourceConfiguration
<a name="aws-properties-lex-bot-datasourceconfiguration"></a>

Contains details about the configuration of the knowledge store used for the `AMAZON.QnAIntent`. You must have already created the knowledge store and indexed the documents within it.

## Syntax
<a name="aws-properties-lex-bot-datasourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-datasourceconfiguration-syntax.json"></a>

```
{
  "[BedrockKnowledgeStoreConfiguration](#cfn-lex-bot-datasourceconfiguration-bedrockknowledgestoreconfiguration)" : {{BedrockKnowledgeStoreConfiguration}},
  "[KendraConfiguration](#cfn-lex-bot-datasourceconfiguration-kendraconfiguration)" : {{QnAKendraConfiguration}},
  "[OpensearchConfiguration](#cfn-lex-bot-datasourceconfiguration-opensearchconfiguration)" : {{OpensearchConfiguration}}
}
```

### YAML
<a name="aws-properties-lex-bot-datasourceconfiguration-syntax.yaml"></a>

```
  [BedrockKnowledgeStoreConfiguration](#cfn-lex-bot-datasourceconfiguration-bedrockknowledgestoreconfiguration): {{
    BedrockKnowledgeStoreConfiguration}}
  [KendraConfiguration](#cfn-lex-bot-datasourceconfiguration-kendraconfiguration): {{
    QnAKendraConfiguration}}
  [OpensearchConfiguration](#cfn-lex-bot-datasourceconfiguration-opensearchconfiguration): {{
    OpensearchConfiguration}}
```

## Properties
<a name="aws-properties-lex-bot-datasourceconfiguration-properties"></a>

`BedrockKnowledgeStoreConfiguration`  <a name="cfn-lex-bot-datasourceconfiguration-bedrockknowledgestoreconfiguration"></a>
Contains details about the configuration of the Amazon Bedrock knowledge base used for the `AMAZON.QnAIntent`. To set up a knowledge base, follow the steps at [Building a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html).
*Required*: No
*Type*: [BedrockKnowledgeStoreConfiguration](aws-properties-lex-bot-bedrockknowledgestoreconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KendraConfiguration`  <a name="cfn-lex-bot-datasourceconfiguration-kendraconfiguration"></a>
Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent`. To create a Amazon Kendra index, follow the steps at [Creating an index](https://docs.aws.amazon.com/kendra/latest/dg/create-index.html).
*Required*: No
*Type*: [QnAKendraConfiguration](aws-properties-lex-bot-qnakendraconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpensearchConfiguration`  <a name="cfn-lex-bot-datasourceconfiguration-opensearchconfiguration"></a>
Contains details about the configuration of the Amazon OpenSearch Service database used for the `AMAZON.QnAIntent`. To create a domain, follow the steps at [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).
*Required*: No
*Type*: [OpensearchConfiguration](aws-properties-lex-bot-opensearchconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
