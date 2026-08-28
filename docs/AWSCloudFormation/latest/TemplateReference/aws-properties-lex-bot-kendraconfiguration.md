---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-kendraconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot KendraConfiguration
<a name="aws-properties-lex-bot-kendraconfiguration"></a>

Provides configuration information for the `AMAZON.KendraSearchIntent` intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance.

## Syntax
<a name="aws-properties-lex-bot-kendraconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-kendraconfiguration-syntax.json"></a>

```
{
  "[KendraIndex](#cfn-lex-bot-kendraconfiguration-kendraindex)" : {{String}},
  "[QueryFilterString](#cfn-lex-bot-kendraconfiguration-queryfilterstring)" : {{String}},
  "[QueryFilterStringEnabled](#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-kendraconfiguration-syntax.yaml"></a>

```
  [KendraIndex](#cfn-lex-bot-kendraconfiguration-kendraindex): {{String}}
  [QueryFilterString](#cfn-lex-bot-kendraconfiguration-queryfilterstring): {{
    String}}
  [QueryFilterStringEnabled](#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-kendraconfiguration-properties"></a>

`KendraIndex`  <a name="cfn-lex-bot-kendraconfiguration-kendraindex"></a>
The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the `AMAZON.KendraSearchIntent` intent to search. The index must be in the same account and Region as the Amazon Lex bot.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:kendra:[a-z]+-(?:[a-z]+-)*[0-9]:[0-9]{12}:index/[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `32`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryFilterString`  <a name="cfn-lex-bot-kendraconfiguration-queryfilterstring"></a>
A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryFilterStringEnabled`  <a name="cfn-lex-bot-kendraconfiguration-queryfilterstringenabled"></a>
Determines whether the `AMAZON.KendraSearchIntent` intent uses a custom query string to query the Amazon Kendra index.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
