---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-messagetemplate-content.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::MessageTemplate Content
<a name="aws-properties-wisdom-messagetemplate-content"></a>

The content of the message template.

## Syntax
<a name="aws-properties-wisdom-messagetemplate-content-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-messagetemplate-content-syntax.json"></a>

```
{
  "[EmailMessageTemplateContent](#cfn-wisdom-messagetemplate-content-emailmessagetemplatecontent)" : {{EmailMessageTemplateContent}},
  "[SmsMessageTemplateContent](#cfn-wisdom-messagetemplate-content-smsmessagetemplatecontent)" : {{SmsMessageTemplateContent}}
}
```

### YAML
<a name="aws-properties-wisdom-messagetemplate-content-syntax.yaml"></a>

```
  [EmailMessageTemplateContent](#cfn-wisdom-messagetemplate-content-emailmessagetemplatecontent): {{
    EmailMessageTemplateContent}}
  [SmsMessageTemplateContent](#cfn-wisdom-messagetemplate-content-smsmessagetemplatecontent): {{
    SmsMessageTemplateContent}}
```

## Properties
<a name="aws-properties-wisdom-messagetemplate-content-properties"></a>

`EmailMessageTemplateContent`  <a name="cfn-wisdom-messagetemplate-content-emailmessagetemplatecontent"></a>
The content of the message template that applies to the email channel subtype.
*Required*: No
*Type*: [EmailMessageTemplateContent](aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsMessageTemplateContent`  <a name="cfn-wisdom-messagetemplate-content-smsmessagetemplatecontent"></a>
The content of message template that applies to SMS channel subtype.
*Required*: No
*Type*: [SmsMessageTemplateContent](aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
