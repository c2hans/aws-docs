---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lex-botversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::BotVersion
<a name="aws-resource-lex-botversion"></a>

**Note**
Amazon Lex V2 is the only supported version in CloudFormation.

Specifies a new version of the bot based on the `DRAFT` version. If the `DRAFT` version of this resource hasn't changed since you created the last version, Amazon Lex doesn't create a new version, it returns the last created version.

When you specify the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1.

## Syntax
<a name="aws-resource-lex-botversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lex-botversion-syntax.json"></a>

```
{
  "Type" : "AWS::Lex::BotVersion",
  "Properties" : {
      "[BotId](#cfn-lex-botversion-botid)" : {{String}},
      "[BotVersionLocaleSpecification](#cfn-lex-botversion-botversionlocalespecification)" : {{[ BotVersionLocaleSpecification, ... ]}},
      "[Description](#cfn-lex-botversion-description)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lex-botversion-syntax.yaml"></a>

```
Type: AWS::Lex::BotVersion
Properties:
  [BotId](#cfn-lex-botversion-botid): {{String}}
  [BotVersionLocaleSpecification](#cfn-lex-botversion-botversionlocalespecification): {{
    - BotVersionLocaleSpecification}}
  [Description](#cfn-lex-botversion-description): {{String}}
```

## Properties
<a name="aws-resource-lex-botversion-properties"></a>

`BotId`  <a name="cfn-lex-botversion-botid"></a>
The unique identifier of the bot.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z]+$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BotVersionLocaleSpecification`  <a name="cfn-lex-botversion-botversionlocalespecification"></a>
Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.
*Required*: Yes
*Type*: [Array](aws-properties-lex-botversion-botversionlocalespecification.md) of [BotVersionLocaleSpecification](aws-properties-lex-botversion-botversionlocalespecification.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lex-botversion-description"></a>
The description of the version.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lex-botversion-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-lex-botversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lex-botversion-return-values-fn--getatt-fn--getatt"></a>

`BotVersion`  <a name="BotVersion-fn::getatt"></a>
The version of the bot.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
