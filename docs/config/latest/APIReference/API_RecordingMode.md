---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingMode.html
---

# RecordingMode
<a name="API_RecordingMode"></a>

Specifies the default recording frequency that AWS Config uses to record configuration changes. AWS Config supports *Continuous recording* and *Daily recording*.
+ Continuous recording allows you to record configuration changes continuously whenever a change occurs.
+ Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.

**Note**
 AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

You can also override the recording frequency for specific resource types.

## Contents
<a name="API_RecordingMode_Contents"></a>

 ** recordingFrequency **   <a name="config-Type-RecordingMode-recordingFrequency"></a>
The default recording frequency that AWS Config uses to record configuration changes.
Daily recording cannot be specified for the following resource types:
+  `AWS::Config::ResourceCompliance`
+  `AWS::Config::ConformancePackCompliance`
+  `AWS::Config::ConfigurationRecorder`
For the **allSupported** (`ALL_SUPPORTED_RESOURCE_TYPES`) recording strategy, these resource types will be set to Continuous recording.
Type: String
Valid Values: `CONTINUOUS | DAILY`
Required: Yes

 ** recordingModeOverrides **   <a name="config-Type-RecordingMode-recordingModeOverrides"></a>
An array of `recordingModeOverride` objects for you to specify your overrides for the recording mode. The `recordingModeOverride` object in the `recordingModeOverrides` array consists of three fields: a `description`, the new `recordingFrequency`, and an array of `resourceTypes` to override.
Type: Array of [RecordingModeOverride](API_RecordingModeOverride.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_RecordingMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RecordingMode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RecordingMode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RecordingMode)
