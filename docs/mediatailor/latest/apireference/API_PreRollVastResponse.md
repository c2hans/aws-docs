---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PreRollVastResponse.html
---

# PreRollVastResponse
<a name="API_PreRollVastResponse"></a>

The settings that control how MediaTailor processes VAST responses from the ad decision server for live pre-roll ad breaks.

## Contents
<a name="API_PreRollVastResponse_Contents"></a>

 ** AdSequencingMode **   <a name="mediatailor-Type-PreRollVastResponse-AdSequencingMode"></a>
The ad sequencing mode for live pre-roll ads. `FOLLOW_AD_SEQUENCE` inserts sequenced ads in increasing order and uses standalone ads only as replacements when a sequenced ad fails. `IGNORE_AD_SEQUENCE` inserts ads in the order they appear in the VAST response, regardless of sequence attributes. The default behavior is `IGNORE_AD_SEQUENCE`.
Type: String
Valid Values: `FOLLOW_AD_SEQUENCE | IGNORE_AD_SEQUENCE`
Required: No

## See Also
<a name="API_PreRollVastResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PreRollVastResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PreRollVastResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PreRollVastResponse)
