---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configurationrecorder-recordingmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationRecorder RecordingMode
<a name="aws-properties-config-configurationrecorder-recordingmode"></a>

Specifies the default recording frequency that AWS Config uses to record configuration changes. AWS Config supports *Continuous recording* and *Daily recording*.
+ Continuous recording allows you to record configuration changes continuously whenever a change occurs.
+ Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.

**Note**
AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

You can also override the recording frequency for specific resource types.

## Syntax
<a name="aws-properties-config-configurationrecorder-recordingmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configurationrecorder-recordingmode-syntax.json"></a>

```
{
  "[RecordingFrequency](#cfn-config-configurationrecorder-recordingmode-recordingfrequency)" : {{String}},
  "[RecordingModeOverrides](#cfn-config-configurationrecorder-recordingmode-recordingmodeoverrides)" : {{[ RecordingModeOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-config-configurationrecorder-recordingmode-syntax.yaml"></a>

```
  [RecordingFrequency](#cfn-config-configurationrecorder-recordingmode-recordingfrequency): {{String}}
  [RecordingModeOverrides](#cfn-config-configurationrecorder-recordingmode-recordingmodeoverrides): {{
    - RecordingModeOverride}}
```

## Properties
<a name="aws-properties-config-configurationrecorder-recordingmode-properties"></a>

`RecordingFrequency`  <a name="cfn-config-configurationrecorder-recordingmode-recordingfrequency"></a>
The default recording frequency that AWS Config uses to record configuration changes.
Daily recording cannot be specified for the following resource types:
+  `AWS::Config::ResourceCompliance`
+  `AWS::Config::ConformancePackCompliance`
+  `AWS::Config::ConfigurationRecorder`
For the **allSupported** (`ALL_SUPPORTED_RESOURCE_TYPES`) recording strategy, these resource types will be set to Continuous recording.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTINUOUS | DAILY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordingModeOverrides`  <a name="cfn-config-configurationrecorder-recordingmode-recordingmodeoverrides"></a>
An array of `recordingModeOverride` objects for you to specify your overrides for the recording mode. The `recordingModeOverride` object in the `recordingModeOverrides` array consists of three fields: a `description`, the new `recordingFrequency`, and an array of `resourceTypes` to override.
*Required*: No
*Type*: Array of [RecordingModeOverride](aws-properties-config-configurationrecorder-recordingmodeoverride.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
