---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ATIModelPerformance.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ATIModelPerformance
<a name="API_ATIModelPerformance"></a>

 The Account Takeover Insights (ATI) model performance score.

## Contents
<a name="API_ATIModelPerformance_Contents"></a>

 ** asi **   <a name="FraudDetector-Type-ATIModelPerformance-asi"></a>
 The anomaly separation index (ASI) score. This metric summarizes the overall ability of the model to separate anomalous activities from the normal behavior. Depending on the business, a large fraction of these anomalous activities can be malicious and correspond to the account takeover attacks. A model with no separability power will have the lowest possible ASI score of 0.5, whereas the a model with a high separability power will have the highest possible ASI score of 1.0
Type: Float
Required: No

## See Also
<a name="API_ATIModelPerformance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ATIModelPerformance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ATIModelPerformance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ATIModelPerformance)
