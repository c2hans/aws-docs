---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpointemail-configurationset-sendingoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PinpointEmail::ConfigurationSet SendingOptions
<a name="aws-properties-pinpointemail-configurationset-sendingoptions"></a>

Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.

## Syntax
<a name="aws-properties-pinpointemail-configurationset-sendingoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpointemail-configurationset-sendingoptions-syntax.json"></a>

```
{
  "[SendingEnabled](#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-pinpointemail-configurationset-sendingoptions-syntax.yaml"></a>

```
  [SendingEnabled](#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-pinpointemail-configurationset-sendingoptions-properties"></a>

`SendingEnabled`  <a name="cfn-pinpointemail-configurationset-sendingoptions-sendingenabled"></a>
If `true`, email sending is enabled for the configuration set. If `false`, email sending is disabled for the configuration set.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
