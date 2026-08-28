---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowversion-lexflownodeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion LexFlowNodeConfiguration
<a name="aws-properties-bedrock-flowversion-lexflownodeconfiguration"></a>

Contains configurations for a Lex node in the flow. You specify a Amazon Lex bot to invoke. This node takes an utterance as the input and returns as the output the intent identified by the Amazon Lex bot. For more information, see [Node types in a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-properties-bedrock-flowversion-lexflownodeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowversion-lexflownodeconfiguration-syntax.json"></a>

```
{
  "[BotAliasArn](#cfn-bedrock-flowversion-lexflownodeconfiguration-botaliasarn)" : {{String}},
  "[LocaleId](#cfn-bedrock-flowversion-lexflownodeconfiguration-localeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowversion-lexflownodeconfiguration-syntax.yaml"></a>

```
  [BotAliasArn](#cfn-bedrock-flowversion-lexflownodeconfiguration-botaliasarn): {{String}}
  [LocaleId](#cfn-bedrock-flowversion-lexflownodeconfiguration-localeid): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowversion-lexflownodeconfiguration-properties"></a>

`BotAliasArn`  <a name="cfn-bedrock-flowversion-lexflownodeconfiguration-botaliasarn"></a>
The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-us-gov):lex:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:bot-alias/[0-9a-zA-Z]+/[0-9a-zA-Z]+$`
*Maximum*: `78`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocaleId`  <a name="cfn-bedrock-flowversion-lexflownodeconfiguration-localeid"></a>
The Region to invoke the Amazon Lex bot in.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
