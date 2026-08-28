---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Transition.html
---

# Transition
<a name="API_Transition"></a>

Program transition configuration.

## Contents
<a name="API_Transition_Contents"></a>

 ** RelativePosition **   <a name="mediatailor-Type-Transition-RelativePosition"></a>
The position where this program will be inserted relative to the `RelativePosition`.
Type: String
Valid Values: `BEFORE_PROGRAM | AFTER_PROGRAM`
Required: Yes

 ** Type **   <a name="mediatailor-Type-Transition-Type"></a>
Defines when the program plays in the schedule. You can set the value to `ABSOLUTE` or `RELATIVE`.
 `ABSOLUTE` - The program plays at a specific wall clock time. This setting can only be used for channels using the `LINEAR` `PlaybackMode`.
Note the following considerations when using `ABSOLUTE` transitions:
If the preceding program in the schedule has a duration that extends past the wall clock time, MediaTailor truncates the preceding program on a common segment boundary.
If there are gaps in playback, MediaTailor plays the `FillerSlate` you configured for your linear channel.
 `RELATIVE` - The program is inserted into the schedule either before or after a program that you specify via `RelativePosition`.
Type: String
Required: Yes

 ** DurationMillis **   <a name="mediatailor-Type-Transition-DurationMillis"></a>
The duration of the live program in seconds.
Type: Long
Required: No

 ** RelativeProgram **   <a name="mediatailor-Type-Transition-RelativeProgram"></a>
The name of the program that this program will be inserted next to, as defined by `RelativePosition`.
Type: String
Required: No

 ** ScheduledStartTimeMillis **   <a name="mediatailor-Type-Transition-ScheduledStartTimeMillis"></a>
The date and time that the program is scheduled to start, in epoch milliseconds.
Type: Long
Required: No

## See Also
<a name="API_Transition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/Transition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/Transition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/Transition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
