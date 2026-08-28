---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_ScheduleConfig.html
---

# ScheduleConfig
<a name="API_ScheduleConfig"></a>

This API enables you to specify the duration that the camera, or local media file, should record onto the Edge Agent. The `ScheduleConfig` consists of the `ScheduleExpression` and the `DurationInMinutes` attributes.

If the `ScheduleConfig` is not provided in the `RecorderConfig`, then the Edge Agent will always be set to recording mode.

If the `ScheduleConfig` is not provided in the `UploaderConfig`, then the Edge Agent will upload at regular intervals (every 1 hour).

## Contents
<a name="API_ScheduleConfig_Contents"></a>

 ** DurationInSeconds **   <a name="KinesisVideo-Type-ScheduleConfig-DurationInSeconds"></a>
The total duration to record the media. If the `ScheduleExpression` attribute is provided, then the `DurationInSeconds` attribute should also be specified.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: Yes

 ** ScheduleExpression **   <a name="KinesisVideo-Type-ScheduleConfig-ScheduleExpression"></a>
The Quartz cron expression that takes care of scheduling jobs to record from the camera, or local media file, onto the Edge Agent. If the `ScheduleExpression` is not provided for the `RecorderConfig`, then the Edge Agent will always be set to recording mode.
For more information about Quartz, refer to the [*Cron Trigger Tutorial*](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) page to understand the valid expressions and its use.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Pattern: `[^\n]{11,100}`
Required: Yes

## See Also
<a name="API_ScheduleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisvideo-2017-09-30/ScheduleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisvideo-2017-09-30/ScheduleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisvideo-2017-09-30/ScheduleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
