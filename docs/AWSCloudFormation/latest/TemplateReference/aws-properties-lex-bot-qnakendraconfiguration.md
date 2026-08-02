---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-qnakendraconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot QnAKendraConfiguration
<a name="aws-properties-lex-bot-qnakendraconfiguration"></a>

Contains details about the configuration of the Amazon Kendra index used for the `AMAZON.QnAIntent`.

## Syntax
<a name="aws-properties-lex-bot-qnakendraconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-qnakendraconfiguration-syntax.json"></a>

```
{
  "[ExactResponse](#cfn-lex-bot-qnakendraconfiguration-exactresponse)" : {{Boolean}},
  "[KendraIndex](#cfn-lex-bot-qnakendraconfiguration-kendraindex)" : {{String}},
  "[QueryFilterString](#cfn-lex-bot-qnakendraconfiguration-queryfilterstring)" : {{String}},
  "[QueryFilterStringEnabled](#cfn-lex-bot-qnakendraconfiguration-queryfilterstringenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-qnakendraconfiguration-syntax.yaml"></a>

```
  [ExactResponse](#cfn-lex-bot-qnakendraconfiguration-exactresponse): {{Boolean}}
  [KendraIndex](#cfn-lex-bot-qnakendraconfiguration-kendraindex): {{String}}
  [QueryFilterString](#cfn-lex-bot-qnakendraconfiguration-queryfilterstring): {{
    String}}
  [QueryFilterStringEnabled](#cfn-lex-bot-qnakendraconfiguration-queryfilterstringenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-qnakendraconfiguration-properties"></a>

`ExactResponse`  <a name="cfn-lex-bot-qnakendraconfiguration-exactresponse"></a>
Specifies whether to return an exact response from the Amazon Kendra index or to let the Amazon Bedrock model you select generate a response based on the results. To use this feature, you must first add FAQ questions to your index by following the steps at [Adding frequently asked questions (FAQs) to an index](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html).
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KendraIndex`  <a name="cfn-lex-bot-qnakendraconfiguration-kendraindex"></a>
The ARN of the Amazon Kendra index to use.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryFilterString`  <a name="cfn-lex-bot-qnakendraconfiguration-queryfilterstring"></a>
Contains the Amazon Kendra filter string to use if enabled. For more information on the Amazon Kendra search filter JSON format, see [Using document attributes to filter search results](https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryFilterStringEnabled`  <a name="cfn-lex-bot-qnakendraconfiguration-queryfilterstringenabled"></a>
Specifies whether to enable an Amazon Kendra filter string or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
