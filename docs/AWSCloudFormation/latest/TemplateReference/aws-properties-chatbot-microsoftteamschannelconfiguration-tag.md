---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-chatbot-microsoftteamschannelconfiguration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Chatbot::MicrosoftTeamsChannelConfiguration Tag
<a name="aws-properties-chatbot-microsoftteamschannelconfiguration-tag"></a>

**Note**
AWS Chatbot is now Amazon Q Developer. [Learn more](https://docs.aws.amazon.com/chatbot/latest/adminguide/service-rename.html)
`Type` attribute values remain unchanged.

The Tag type enables you to specify a key-value pair that can be used to store information about a Microsoft Teams channel configuration.

## Syntax
<a name="aws-properties-chatbot-microsoftteamschannelconfiguration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-chatbot-microsoftteamschannelconfiguration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-chatbot-microsoftteamschannelconfiguration-tag-key)" : {{String}},
  "[Value](#cfn-chatbot-microsoftteamschannelconfiguration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-chatbot-microsoftteamschannelconfiguration-tag-syntax.yaml"></a>

```
  [Key](#cfn-chatbot-microsoftteamschannelconfiguration-tag-key): {{String}}
  [Value](#cfn-chatbot-microsoftteamschannelconfiguration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-chatbot-microsoftteamschannelconfiguration-tag-properties"></a>

`Key`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-tag-key"></a>
 A string used to identify this tag. You can specify a maximum of 128 characters for a tag key. Tags owned by Amazon Web Services (AWS) have the reserved prefix: `aws:`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-chatbot-microsoftteamschannelconfiguration-tag-value"></a>
A string containing the value for this tag. You can specify a maximum of 256 characters for a tag value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
