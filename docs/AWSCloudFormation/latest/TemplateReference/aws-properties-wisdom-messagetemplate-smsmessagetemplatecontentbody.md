---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate SmsMessageTemplateContentBody
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody"></a>

The body to use in SMS messages.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody-syntax.json"></a>

```
{
  "[PlainText](#cfn-wisdom-messagetemplate-smsmessagetemplatecontentbody-plaintext)" : {{MessageTemplateBodyContentProvider}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody-syntax.yaml"></a>

```
  [PlainText](#cfn-wisdom-messagetemplate-smsmessagetemplatecontentbody-plaintext): {{
    MessageTemplateBodyContentProvider}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody-properties"></a>

`PlainText`  <a name="cfn-wisdom-messagetemplate-smsmessagetemplatecontentbody-plaintext"></a>
The message body to use in SMS messages.
*Required*: No
*Type*: [MessageTemplateBodyContentProvider](aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
