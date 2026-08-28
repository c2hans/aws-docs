---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AudioLogSetting.html
---

# AudioLogSetting
<a name="API_AudioLogSetting"></a>

Settings for logging audio of conversations between Amazon Lex and a user. You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.

## Contents
<a name="API_AudioLogSetting_Contents"></a>

 ** destination **   <a name="lexv2-Type-AudioLogSetting-destination"></a>
The location of audio log files collected when conversation logging is enabled for a bot.
Type: [AudioLogDestination](API_AudioLogDestination.md) object
Required: Yes

 ** enabled **   <a name="lexv2-Type-AudioLogSetting-enabled"></a>
Determines whether audio logging in enabled for the bot.
Type: Boolean
Required: Yes

 ** selectiveLoggingEnabled **   <a name="lexv2-Type-AudioLogSetting-selectiveLoggingEnabled"></a>
The option to enable selective conversation log capture for audio.
Type: Boolean
Required: No

## See Also
<a name="API_AudioLogSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/AudioLogSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/AudioLogSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/AudioLogSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
