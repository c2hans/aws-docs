---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate EmailMessageTemplateContentBody
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody"></a>

The body to use in email messages.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody-syntax.json"></a>

```
{
  "[Html](#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-html)" : {{MessageTemplateBodyContentProvider}},
  "[PlainText](#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-plaintext)" : {{MessageTemplateBodyContentProvider}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody-syntax.yaml"></a>

```
  [Html](#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-html): {{
    MessageTemplateBodyContentProvider}}
  [PlainText](#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-plaintext): {{
    MessageTemplateBodyContentProvider}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody-properties"></a>

`Html`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-html"></a>
The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.
*Required*: No
*Type*: [MessageTemplateBodyContentProvider](aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlainText`  <a name="cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-plaintext"></a>
The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.
*Required*: No
*Type*: [MessageTemplateBodyContentProvider](aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
