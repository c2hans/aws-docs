---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lex-botalias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::BotAlias
<a name="aws-resource-lex-botalias"></a>

**Note**
Amazon Lex V2 is the only supported version in CloudFormation.

Specifies an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.

For example, you can specify an alias called "PROD" that your applications use to call the Amazon Lex bot.

## Syntax
<a name="aws-resource-lex-botalias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lex-botalias-syntax.json"></a>

```
{
  "Type" : "AWS::Lex::BotAlias",
  "Properties" : {
      "[BotAliasLocaleSettings](#cfn-lex-botalias-botaliaslocalesettings)" : {{[ BotAliasLocaleSettingsItem, ... ]}},
      "[BotAliasName](#cfn-lex-botalias-botaliasname)" : {{String}},
      "[BotAliasTags](#cfn-lex-botalias-botaliastags)" : {{[ Tag, ... ]}},
      "[BotId](#cfn-lex-botalias-botid)" : {{String}},
      "[BotVersion](#cfn-lex-botalias-botversion)" : {{String}},
      "[ConversationLogSettings](#cfn-lex-botalias-conversationlogsettings)" : {{ConversationLogSettings}},
      "[Description](#cfn-lex-botalias-description)" : {{String}},
      "[SentimentAnalysisSettings](#cfn-lex-botalias-sentimentanalysissettings)" : {{SentimentAnalysisSettings}}
    }
}
```

### YAML
<a name="aws-resource-lex-botalias-syntax.yaml"></a>

```
Type: AWS::Lex::BotAlias
Properties:
  [BotAliasLocaleSettings](#cfn-lex-botalias-botaliaslocalesettings): {{
    - BotAliasLocaleSettingsItem}}
  [BotAliasName](#cfn-lex-botalias-botaliasname): {{String}}
  [BotAliasTags](#cfn-lex-botalias-botaliastags): {{
    - Tag}}
  [BotId](#cfn-lex-botalias-botid): {{String}}
  [BotVersion](#cfn-lex-botalias-botversion): {{String}}
  [ConversationLogSettings](#cfn-lex-botalias-conversationlogsettings): {{
    ConversationLogSettings}}
  [Description](#cfn-lex-botalias-description): {{String}}
  [SentimentAnalysisSettings](#cfn-lex-botalias-sentimentanalysissettings): {{
    SentimentAnalysisSettings}}
```

## Properties
<a name="aws-resource-lex-botalias-properties"></a>

`BotAliasLocaleSettings`  <a name="cfn-lex-botalias-botaliaslocalesettings"></a>
Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the bot's locale.
*Required*: No
*Type*: [Array](aws-properties-lex-botalias-botaliaslocalesettings.md) of [BotAliasLocaleSettingsItem](aws-properties-lex-botalias-botaliaslocalesettingsitem.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotAliasName`  <a name="cfn-lex-botalias-botaliasname"></a>
The name of the bot alias.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotAliasTags`  <a name="cfn-lex-botalias-botaliastags"></a>
An array of key-value pairs to apply to this resource.
You can only add tags when you specify an alias.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-lex-botalias-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotId`  <a name="cfn-lex-botalias-botid"></a>
The unique identifier of the bot.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]+$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BotVersion`  <a name="cfn-lex-botalias-botversion"></a>
The version of the bot that the bot alias references.
*Required*: No
*Type*: String
*Pattern*: `^(DRAFT|[0-9]+)$`
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConversationLogSettings`  <a name="cfn-lex-botalias-conversationlogsettings"></a>
Specifies whether Amazon Lex logs text and audio for conversations with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch logs. Audio logs store input in Amazon S3.
*Required*: No
*Type*: [ConversationLogSettings](aws-properties-lex-botalias-conversationlogsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lex-botalias-description"></a>
The description of the bot alias.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SentimentAnalysisSettings`  <a name="cfn-lex-botalias-sentimentanalysissettings"></a>
Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
*Required*: No
*Type*: [SentimentAnalysisSettings](aws-properties-lex-botalias-sentimentanalysissettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lex-botalias-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-lex-botalias-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lex-botalias-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the bot alias.

`BotAliasId`  <a name="BotAliasId-fn::getatt"></a>
The unique identifier of the bot alias.

`BotAliasStatus`  <a name="BotAliasStatus-fn::getatt"></a>
The current status of the bot alias. When the status is Available the alias is ready for use with your bot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
