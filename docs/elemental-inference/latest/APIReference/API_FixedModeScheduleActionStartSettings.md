---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_FixedModeScheduleActionStartSettings.html
---

# FixedModeScheduleActionStartSettings
<a name="API_FixedModeScheduleActionStartSettings"></a>

Sets the time at which a schedule action runs once. This is a type of ScheduleActionStartConfiguration.

## Contents
<a name="API_FixedModeScheduleActionStartSettings_Contents"></a>

 ** scheduledAt **   <a name="elementalinference-Type-FixedModeScheduleActionStartSettings-scheduledAt"></a>
The UTC time at which the action runs. Specify the time in whole seconds. For the range of times that you can specify, see the AWS Elemental Inference User Guide.
This time is approximate. The change can take a few minutes to take effect on the media that the feed is processing.
Type: Timestamp
Required: Yes

## See Also
<a name="API_FixedModeScheduleActionStartSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/FixedModeScheduleActionStartSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/FixedModeScheduleActionStartSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/FixedModeScheduleActionStartSettings)
