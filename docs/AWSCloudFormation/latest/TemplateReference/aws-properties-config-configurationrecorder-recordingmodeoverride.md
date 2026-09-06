---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configurationrecorder-recordingmodeoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationRecorder RecordingModeOverride
<a name="aws-properties-config-configurationrecorder-recordingmodeoverride"></a>

An object for you to specify your overrides for the recording mode.

## Syntax
<a name="aws-properties-config-configurationrecorder-recordingmodeoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configurationrecorder-recordingmodeoverride-syntax.json"></a>

```
{
  "[Description](#cfn-config-configurationrecorder-recordingmodeoverride-description)" : {{String}},
  "[RecordingFrequency](#cfn-config-configurationrecorder-recordingmodeoverride-recordingfrequency)" : {{String}},
  "[ResourceTypes](#cfn-config-configurationrecorder-recordingmodeoverride-resourcetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-config-configurationrecorder-recordingmodeoverride-syntax.yaml"></a>

```
  [Description](#cfn-config-configurationrecorder-recordingmodeoverride-description): {{String}}
  [RecordingFrequency](#cfn-config-configurationrecorder-recordingmodeoverride-recordingfrequency): {{String}}
  [ResourceTypes](#cfn-config-configurationrecorder-recordingmodeoverride-resourcetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-config-configurationrecorder-recordingmodeoverride-properties"></a>

`Description`  <a name="cfn-config-configurationrecorder-recordingmodeoverride-description"></a>
A description that you provide for the override.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordingFrequency`  <a name="cfn-config-configurationrecorder-recordingmodeoverride-recordingfrequency"></a>
The recording frequency that will be applied to all the resource types specified in the override.
+ Continuous recording allows you to record configuration changes continuously whenever a change occurs.
+ Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.
AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTINUOUS | DAILY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypes`  <a name="cfn-config-configurationrecorder-recordingmodeoverride-resourcetypes"></a>
A comma-separated list that specifies which resource types AWS Config includes in the override.
Daily recording cannot be specified for the following resource types:
+  `AWS::Config::ResourceCompliance`
+  `AWS::Config::ConformancePackCompliance`
+  `AWS::Config::ConfigurationRecorder`
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
