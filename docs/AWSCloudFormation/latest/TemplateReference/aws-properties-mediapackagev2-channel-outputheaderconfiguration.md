---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channel-outputheaderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel OutputHeaderConfiguration
<a name="aws-properties-mediapackagev2-channel-outputheaderconfiguration"></a>

The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.

## Syntax
<a name="aws-properties-mediapackagev2-channel-outputheaderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channel-outputheaderconfiguration-syntax.json"></a>

```
{
  "[PublishMQCS](#cfn-mediapackagev2-channel-outputheaderconfiguration-publishmqcs)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channel-outputheaderconfiguration-syntax.yaml"></a>

```
  [PublishMQCS](#cfn-mediapackagev2-channel-outputheaderconfiguration-publishmqcs): {{Boolean}}
```

## Properties
<a name="aws-properties-mediapackagev2-channel-outputheaderconfiguration-properties"></a>

`PublishMQCS`  <a name="cfn-mediapackagev2-channel-outputheaderconfiguration-publishmqcs"></a>
When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when `InputType` is `CMAF`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
