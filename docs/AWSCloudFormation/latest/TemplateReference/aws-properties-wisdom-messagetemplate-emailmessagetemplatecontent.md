---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate EmailMessageTemplateContent
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent"></a>

The content of the message template that applies to the email channel subtype.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent-syntax.json"></a>

```
{
  "[Body](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-body)" : {{EmailMessageTemplateContentBody}},
  "[Headers](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-headers)" : {{[ EmailMessageTemplateHeader, ... ]}},
  "[Subject](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-subject)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent-syntax.yaml"></a>

```
  [Body](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-body): {{
    EmailMessageTemplateContentBody}}
  [Headers](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-headers): {{
    - EmailMessageTemplateHeader}}
  [Subject](#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-subject): {{String}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent-properties"></a>

`Body`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplatecontent-body"></a>
The body to use in email messages.
*Required*: Yes
*Type*: [EmailMessageTemplateContentBody](aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplatecontent-headers"></a>
The email headers to include in email messages.
*Required*: Yes
*Type*: Array of [EmailMessageTemplateHeader](aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.md)
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subject`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplatecontent-subject"></a>
The subject line, or title, to use in email messages.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
