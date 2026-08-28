---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-featureactivations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FeatureActivations
<a name="aws-properties-medialive-channel-featureactivations"></a>

Settings to enable specific features. You can't configure these features until you have enabled them in the channel.

The parent of this entity is EncoderSettings.

## Syntax
<a name="aws-properties-medialive-channel-featureactivations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-featureactivations-syntax.json"></a>

```
{
  "[InputPrepareScheduleActions](#cfn-medialive-channel-featureactivations-inputpreparescheduleactions)" : {{String}},
  "[OutputStaticImageOverlayScheduleActions](#cfn-medialive-channel-featureactivations-outputstaticimageoverlayscheduleactions)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-featureactivations-syntax.yaml"></a>

```
  [InputPrepareScheduleActions](#cfn-medialive-channel-featureactivations-inputpreparescheduleactions): {{String}}
  [OutputStaticImageOverlayScheduleActions](#cfn-medialive-channel-featureactivations-outputstaticimageoverlayscheduleactions): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-featureactivations-properties"></a>

`InputPrepareScheduleActions`  <a name="cfn-medialive-channel-featureactivations-inputpreparescheduleactions"></a>
Enables the Input Prepare feature. You can create Input Prepare actions in the schedule only if this feature is enabled. If you disable the feature on an existing schedule, make sure that you first delete all input prepare actions from the schedule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStaticImageOverlayScheduleActions`  <a name="cfn-medialive-channel-featureactivations-outputstaticimageoverlayscheduleactions"></a>
Enables the output static image overlay feature. Enabling this feature allows you to send channel schedule updates to display/clear/modify image overlays on an output-by-output basis.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
