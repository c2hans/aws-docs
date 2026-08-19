---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_LivePreRollConfiguration.html
---

# LivePreRollConfiguration
<a name="API_LivePreRollConfiguration"></a>

The configuration for pre-roll ad insertion.

## Contents
<a name="API_LivePreRollConfiguration_Contents"></a>

 ** AdDecisionServerConfiguration **   <a name="mediatailor-Type-LivePreRollConfiguration-AdDecisionServerConfiguration"></a>
The configuration for the ad decision server (ADS) for live pre-roll ads. The configuration contains settings that control how MediaTailor processes VAST responses for pre-roll ad breaks.
Type: [PreRollAdDecisionServerConfiguration](API_PreRollAdDecisionServerConfiguration.md) object
Required: No

 ** AdDecisionServerUrl **   <a name="mediatailor-Type-LivePreRollConfiguration-AdDecisionServerUrl"></a>
The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.
Type: String
Required: No

 ** MaxDurationSeconds **   <a name="mediatailor-Type-LivePreRollConfiguration-MaxDurationSeconds"></a>
The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor won't play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.
Type: Integer
Required: No

## See Also
<a name="API_LivePreRollConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/LivePreRollConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/LivePreRollConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/LivePreRollConfiguration)
