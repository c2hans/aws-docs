---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-botmember.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BotMember
<a name="aws-properties-lex-bot-botmember"></a>

A bot that is a member of a network of bots.

## Syntax
<a name="aws-properties-lex-bot-botmember-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-botmember-syntax.json"></a>

```
{
  "[BotMemberAliasId](#cfn-lex-bot-botmember-botmemberaliasid)" : {{String}},
  "[BotMemberAliasName](#cfn-lex-bot-botmember-botmemberaliasname)" : {{String}},
  "[BotMemberId](#cfn-lex-bot-botmember-botmemberid)" : {{String}},
  "[BotMemberName](#cfn-lex-bot-botmember-botmembername)" : {{String}},
  "[BotMemberVersion](#cfn-lex-bot-botmember-botmemberversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-botmember-syntax.yaml"></a>

```
  [BotMemberAliasId](#cfn-lex-bot-botmember-botmemberaliasid): {{String}}
  [BotMemberAliasName](#cfn-lex-bot-botmember-botmemberaliasname): {{String}}
  [BotMemberId](#cfn-lex-bot-botmember-botmemberid): {{String}}
  [BotMemberName](#cfn-lex-bot-botmember-botmembername): {{String}}
  [BotMemberVersion](#cfn-lex-bot-botmember-botmemberversion): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-botmember-properties"></a>

`BotMemberAliasId`  <a name="cfn-lex-bot-botmember-botmemberaliasid"></a>
The alias ID of a bot that is a member of this network of bots.
*Required*: Yes
*Type*: String
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotMemberAliasName`  <a name="cfn-lex-bot-botmember-botmemberaliasname"></a>
The alias name of a bot that is a member of this network of bots.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotMemberId`  <a name="cfn-lex-bot-botmember-botmemberid"></a>
The unique ID of a bot that is a member of this network of bots.
*Required*: Yes
*Type*: String
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotMemberName`  <a name="cfn-lex-bot-botmember-botmembername"></a>
The unique name of a bot that is a member of this network of bots.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BotMemberVersion`  <a name="cfn-lex-bot-botmember-botmemberversion"></a>
The version of a bot that is a member of this network of bots.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
