---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channel-inputswitchconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel InputSwitchConfiguration
<a name="aws-properties-mediapackagev2-channel-inputswitchconfiguration"></a>

The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive.

## Syntax
<a name="aws-properties-mediapackagev2-channel-inputswitchconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channel-inputswitchconfiguration-syntax.json"></a>

```
{
  "[MQCSInputSwitching](#cfn-mediapackagev2-channel-inputswitchconfiguration-mqcsinputswitching)" : {{Boolean}},
  "[PreferredInput](#cfn-mediapackagev2-channel-inputswitchconfiguration-preferredinput)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channel-inputswitchconfiguration-syntax.yaml"></a>

```
  [MQCSInputSwitching](#cfn-mediapackagev2-channel-inputswitchconfiguration-mqcsinputswitching): {{Boolean}}
  [PreferredInput](#cfn-mediapackagev2-channel-inputswitchconfiguration-preferredinput): {{Integer}}
```

## Properties
<a name="aws-properties-mediapackagev2-channel-inputswitchconfiguration-properties"></a>

`MQCSInputSwitching`  <a name="cfn-mediapackagev2-channel-inputswitchconfiguration-mqcsinputswitching"></a>
When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is false. This setting is valid only when `InputType` is `CMAF`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreferredInput`  <a name="cfn-mediapackagev2-channel-inputswitchconfiguration-preferredinput"></a>
For CMAF inputs, indicates which input MediaPackage should prefer when both inputs have equal MQCS scores. Select `1` to prefer the first ingest endpoint, or `2` to prefer the second ingest endpoint. If you don't specify a preferred input, MediaPackage uses its default switching behavior when MQCS scores are equal.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
