---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartRecommendationsRequestEntry.html
---

# StartRecommendationsRequestEntry
<a name="API_StartRecommendationsRequestEntry"></a>

Provides information about the source database to analyze and provide target recommendations according to the specified requirements.

## Contents
<a name="API_StartRecommendationsRequestEntry_Contents"></a>

 ** DatabaseId **   <a name="DMS-Type-StartRecommendationsRequestEntry-DatabaseId"></a>
The identifier of the source database.
Type: String
Required: Yes

 ** Settings **   <a name="DMS-Type-StartRecommendationsRequestEntry-Settings"></a>
The required target engine settings.
Type: [RecommendationSettings](API_RecommendationSettings.md) object
Required: Yes

## See Also
<a name="API_StartRecommendationsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartRecommendationsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartRecommendationsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartRecommendationsRequestEntry)
