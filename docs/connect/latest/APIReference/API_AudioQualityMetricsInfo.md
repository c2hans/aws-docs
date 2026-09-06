---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AudioQualityMetricsInfo.html
---

# AudioQualityMetricsInfo
<a name="API_AudioQualityMetricsInfo"></a>

Contains information for score and potential quality issues for Audio

## Contents
<a name="API_AudioQualityMetricsInfo_Contents"></a>

 ** PotentialQualityIssues **   <a name="connect-Type-AudioQualityMetricsInfo-PotentialQualityIssues"></a>
List of potential issues causing degradation of quality on a media connection. If the service did not detect any potential quality issues the list is empty.
Valid values: `HighPacketLoss` \| `HighRoundTripTime` \| `HighJitterBuffer`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** QualityScore **   <a name="connect-Type-AudioQualityMetricsInfo-QualityScore"></a>
Number measuring the estimated quality of the media connection.
Type: Float
Required: No

## See Also
<a name="API_AudioQualityMetricsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AudioQualityMetricsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AudioQualityMetricsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AudioQualityMetricsInfo)
