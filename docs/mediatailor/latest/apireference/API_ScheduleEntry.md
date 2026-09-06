---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ScheduleEntry.html
---

# ScheduleEntry
<a name="API_ScheduleEntry"></a>

The properties for a schedule.

## Contents
<a name="API_ScheduleEntry_Contents"></a>

 ** Arn **   <a name="mediatailor-Type-ScheduleEntry-Arn"></a>
The ARN of the program.
Type: String
Required: Yes

 ** ChannelName **   <a name="mediatailor-Type-ScheduleEntry-ChannelName"></a>
The name of the channel that uses this schedule.
Type: String
Required: Yes

 ** ProgramName **   <a name="mediatailor-Type-ScheduleEntry-ProgramName"></a>
The name of the program.
Type: String
Required: Yes

 ** SourceLocationName **   <a name="mediatailor-Type-ScheduleEntry-SourceLocationName"></a>
The name of the source location.
Type: String
Required: Yes

 ** ApproximateDurationSeconds **   <a name="mediatailor-Type-ScheduleEntry-ApproximateDurationSeconds"></a>
The approximate duration of this program, in seconds.
Type: Long
Required: No

 ** ApproximateStartTime **   <a name="mediatailor-Type-ScheduleEntry-ApproximateStartTime"></a>
The approximate time that the program will start playing.
Type: Timestamp
Required: No

 ** Audiences **   <a name="mediatailor-Type-ScheduleEntry-Audiences"></a>
The list of audiences defined in ScheduleEntry.
Type: Array of strings
Required: No

 ** LiveSourceName **   <a name="mediatailor-Type-ScheduleEntry-LiveSourceName"></a>
The name of the live source used for the program.
Type: String
Required: No

 ** ScheduleAdBreaks **   <a name="mediatailor-Type-ScheduleEntry-ScheduleAdBreaks"></a>
The schedule's ad break properties.
Type: Array of [ScheduleAdBreak](API_ScheduleAdBreak.md) objects
Required: No

 ** ScheduleEntryType **   <a name="mediatailor-Type-ScheduleEntry-ScheduleEntryType"></a>
The type of schedule entry.
Type: String
Valid Values: `PROGRAM | FILLER_SLATE | ALTERNATE_MEDIA`
Required: No

 ** VodSourceName **   <a name="mediatailor-Type-ScheduleEntry-VodSourceName"></a>
The name of the VOD source.
Type: String
Required: No

## See Also
<a name="API_ScheduleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ScheduleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ScheduleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ScheduleEntry)
