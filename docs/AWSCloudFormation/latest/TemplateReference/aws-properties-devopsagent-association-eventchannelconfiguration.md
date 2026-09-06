---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-eventchannelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association EventChannelConfiguration
<a name="aws-properties-devopsagent-association-eventchannelconfiguration"></a>

Configuration for Event Channel integration. Defines webhook update settings to enable the Agent Space to receive real-time event notifications from event channel integrations.

## Syntax
<a name="aws-properties-devopsagent-association-eventchannelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-eventchannelconfiguration-syntax.json"></a>

```
{
  "[EnableWebhookUpdates](#cfn-devopsagent-association-eventchannelconfiguration-enablewebhookupdates)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-eventchannelconfiguration-syntax.yaml"></a>

```
  [EnableWebhookUpdates](#cfn-devopsagent-association-eventchannelconfiguration-enablewebhookupdates): {{Boolean}}
```

## Properties
<a name="aws-properties-devopsagent-association-eventchannelconfiguration-properties"></a>

`EnableWebhookUpdates`  <a name="cfn-devopsagent-association-eventchannelconfiguration-enablewebhookupdates"></a>
When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
