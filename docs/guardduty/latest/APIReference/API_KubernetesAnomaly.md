---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_KubernetesAnomaly.html
---

# KubernetesAnomaly
<a name="API_KubernetesAnomaly"></a>

Contains details about anomalous Kubernetes behavior.

## Contents
<a name="API_KubernetesAnomaly_Contents"></a>

 ** anomalyScore **   <a name="guardduty-Type-KubernetesAnomaly-anomalyScore"></a>
The anomaly score of the behavior.
Type: String
Required: No

 ** baselineContext **   <a name="guardduty-Type-KubernetesAnomaly-baselineContext"></a>
A description of the normal behavior that the activity was compared against.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** trainingPeriod **   <a name="guardduty-Type-KubernetesAnomaly-trainingPeriod"></a>
The period over which the normal behavior was established.
Type: String
Required: No

 ** unusualBehavior **   <a name="guardduty-Type-KubernetesAnomaly-unusualBehavior"></a>
A description of the unusual behavior.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_KubernetesAnomaly_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/KubernetesAnomaly)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/KubernetesAnomaly)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/KubernetesAnomaly)
