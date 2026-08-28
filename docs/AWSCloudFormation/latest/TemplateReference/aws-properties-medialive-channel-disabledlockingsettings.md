---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-disabledlockingsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel DisabledLockingSettings
<a name="aws-properties-medialive-channel-disabledlockingsettings"></a>

Disabled Locking Settings

## Syntax
<a name="aws-properties-medialive-channel-disabledlockingsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-disabledlockingsettings-syntax.json"></a>

```
{
  "[CustomEpoch](#cfn-medialive-channel-disabledlockingsettings-customepoch)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-disabledlockingsettings-syntax.yaml"></a>

```
  [CustomEpoch](#cfn-medialive-channel-disabledlockingsettings-customepoch): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-disabledlockingsettings-properties"></a>

`CustomEpoch`  <a name="cfn-medialive-channel-disabledlockingsettings-customepoch"></a>
Optional. Only applies to CMAF Ingest Output Group and MediaPackage V2 Output Group. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
