---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-channel-logconfigurationforchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Channel LogConfigurationForChannel

The log configuration for the channel.

## Syntax
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax.json"></a>

```json
{
  "[LogTypes](#cfn-mediatailor-channel-logconfigurationforchannel-logtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediatailor-channel-logconfigurationforchannel-syntax.yaml"></a>

```yaml
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
