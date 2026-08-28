---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-bandwidthreductionfiltersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel BandwidthReductionFilterSettings
<a name="aws-properties-medialive-channel-bandwidthreductionfiltersettings"></a>

Bandwidth reduction filter settings.

The parent of this entity is H264FilterSettings or H265FilterSettings.

## Syntax
<a name="aws-properties-medialive-channel-bandwidthreductionfiltersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-bandwidthreductionfiltersettings-syntax.json"></a>

```
{
  "[PostFilterSharpening](#cfn-medialive-channel-bandwidthreductionfiltersettings-postfiltersharpening)" : {{String}},
  "[Strength](#cfn-medialive-channel-bandwidthreductionfiltersettings-strength)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-bandwidthreductionfiltersettings-syntax.yaml"></a>

```
  [PostFilterSharpening](#cfn-medialive-channel-bandwidthreductionfiltersettings-postfiltersharpening): {{String}}
  [Strength](#cfn-medialive-channel-bandwidthreductionfiltersettings-strength): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-bandwidthreductionfiltersettings-properties"></a>

`PostFilterSharpening`  <a name="cfn-medialive-channel-bandwidthreductionfiltersettings-postfiltersharpening"></a>
Configures the sharpening control, which is available when the bandwidth reduction filter is enabled. This control sharpens edges and contours, which produces a specific artistic effect that you might want. We recommend that you test each of the values (including DISABLED) to observe the sharpening effect on the content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strength`  <a name="cfn-medialive-channel-bandwidthreductionfiltersettings-strength"></a>
Enables the bandwidth reduction filter. The filter strengths range from 1 to 4. We recommend that you always enable this filter and use AUTO, to let MediaLive apply the optimum filtering for the context.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
