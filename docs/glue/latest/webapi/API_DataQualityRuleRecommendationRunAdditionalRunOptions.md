---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityRuleRecommendationRunAdditionalRunOptions.html
---

# DataQualityRuleRecommendationRunAdditionalRunOptions
<a name="API_DataQualityRuleRecommendationRunAdditionalRunOptions"></a>

Additional run options you can specify for a recommendation run.

## Contents
<a name="API_DataQualityRuleRecommendationRunAdditionalRunOptions_Contents"></a>

 ** CustomLogGroupPrefix **   <a name="Glue-Type-DataQualityRuleRecommendationRunAdditionalRunOptions-CustomLogGroupPrefix"></a>
A custom prefix for the CloudWatch log group names. When specified, recommendation run logs are written to `<CustomLogGroupPrefix>/error` and `<CustomLogGroupPrefix>/output` instead of the default `/aws-glue/data-quality/error` and `/aws-glue/data-quality/output` log groups.
Type: String
Required: No

## See Also
<a name="API_DataQualityRuleRecommendationRunAdditionalRunOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityRuleRecommendationRunAdditionalRunOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityRuleRecommendationRunAdditionalRunOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityRuleRecommendationRunAdditionalRunOptions)
