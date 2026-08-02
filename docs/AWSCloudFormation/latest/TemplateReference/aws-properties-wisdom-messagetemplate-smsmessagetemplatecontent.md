---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate SmsMessageTemplateContent
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent"></a>

The content of the message template that applies to the SMS channel subtype.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent-syntax.json"></a>

```
{
  "[Body](#cfn-wisdom-messagetemplate-smsmessagetemplatecontent-body)" : {{SmsMessageTemplateContentBody}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent-syntax.yaml"></a>

```
  [Body](#cfn-wisdom-messagetemplate-smsmessagetemplatecontent-body): {{
    SmsMessageTemplateContentBody}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent-properties"></a>

`Body`  <a name="cfn-wisdom-messagetemplate-smsmessagetemplatecontent-body"></a>
The body to use in SMS messages.
*Required*: Yes
*Type*: [SmsMessageTemplateContentBody](aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
