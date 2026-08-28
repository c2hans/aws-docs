---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-inputlossfailoversettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel InputLossFailoverSettings
<a name="aws-properties-medialive-channel-inputlossfailoversettings"></a>

MediaLive will perform a failover if content is not detected in this input for the specified period.

The parent of this entity is FailoverConditionSettings.

## Syntax
<a name="aws-properties-medialive-channel-inputlossfailoversettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-inputlossfailoversettings-syntax.json"></a>

```
{
  "[InputLossThresholdMsec](#cfn-medialive-channel-inputlossfailoversettings-inputlossthresholdmsec)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-inputlossfailoversettings-syntax.yaml"></a>

```
  [InputLossThresholdMsec](#cfn-medialive-channel-inputlossfailoversettings-inputlossthresholdmsec): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-inputlossfailoversettings-properties"></a>

`InputLossThresholdMsec`  <a name="cfn-medialive-channel-inputlossfailoversettings-inputlossthresholdmsec"></a>
The amount of time (in milliseconds) that no input is detected. After that time, an input failover will occur.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
