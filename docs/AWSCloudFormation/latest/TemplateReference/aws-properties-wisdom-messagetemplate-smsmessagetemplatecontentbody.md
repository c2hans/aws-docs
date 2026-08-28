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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
