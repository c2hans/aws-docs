---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_ClipRange.html
---

# ClipRange
<a name="API_ClipRange"></a>

Clip range configuration for the VOD source associated with the program.

## Contents
<a name="API_ClipRange_Contents"></a>

 ** EndOffsetMillis **   <a name="mediatailor-Type-ClipRange-EndOffsetMillis"></a>
The end offset of the clip range, in milliseconds, starting from the beginning of the VOD source associated with the program.
Type: Long
Required: No

 ** StartOffsetMillis **   <a name="mediatailor-Type-ClipRange-StartOffsetMillis"></a>
The start offset of the clip range, in milliseconds. This offset truncates the start at the number of milliseconds into the duration of the VOD source.
Type: Long
Required: No

## See Also
<a name="API_ClipRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/ClipRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/ClipRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/ClipRange)
