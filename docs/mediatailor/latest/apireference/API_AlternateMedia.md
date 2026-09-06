---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AlternateMedia.html
---

# AlternateMedia
<a name="API_AlternateMedia"></a>

A playlist of media (VOD and/or live) to be played instead of the default media on a particular program.

## Contents
<a name="API_AlternateMedia_Contents"></a>

 ** AdBreaks **   <a name="mediatailor-Type-AlternateMedia-AdBreaks"></a>
Ad break configuration parameters defined in AlternateMedia.
Type: Array of [AdBreak](API_AdBreak.md) objects
Required: No

 ** ClipRange **   <a name="mediatailor-Type-AlternateMedia-ClipRange"></a>
Clip range configuration for the VOD source associated with the program.
Type: [ClipRange](API_ClipRange.md) object
Required: No

 ** DurationMillis **   <a name="mediatailor-Type-AlternateMedia-DurationMillis"></a>
The duration of the alternateMedia in milliseconds.
Type: Long
Required: No

 ** LiveSourceName **   <a name="mediatailor-Type-AlternateMedia-LiveSourceName"></a>
The name of the live source for alternateMedia.
Type: String
Required: No

 ** ScheduledStartTimeMillis **   <a name="mediatailor-Type-AlternateMedia-ScheduledStartTimeMillis"></a>
The date and time that the alternateMedia is scheduled to start, in epoch milliseconds.
Type: Long
Required: No

 ** SourceLocationName **   <a name="mediatailor-Type-AlternateMedia-SourceLocationName"></a>
The name of the source location for alternateMedia.
Type: String
Required: No

 ** VodSourceName **   <a name="mediatailor-Type-AlternateMedia-VodSourceName"></a>
The name of the VOD source for alternateMedia.
Type: String
Required: No

## See Also
<a name="API_AlternateMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AlternateMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AlternateMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AlternateMedia)
