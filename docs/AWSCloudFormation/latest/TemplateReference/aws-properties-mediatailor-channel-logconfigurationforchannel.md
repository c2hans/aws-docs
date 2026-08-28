---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-logconfigurationforchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel LogConfigurationForChannel
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel"></a>

The log configuration for the channel.

## Syntax
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax.json"></a>

```
{
  "[LogTypes](#cfn-mediatailor-channel-logconfigurationforchannel-logtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax.yaml"></a>

```
  [LogTypes](#cfn-mediatailor-channel-logconfigurationforchannel-logtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-properties"></a>

`LogTypes`  <a name="cfn-mediatailor-channel-logconfigurationforchannel-logtypes"></a>
The log types.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
