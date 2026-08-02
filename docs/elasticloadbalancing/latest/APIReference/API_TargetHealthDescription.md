---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetHealthDescription.html
---

# TargetHealthDescription
<a name="API_TargetHealthDescription"></a>

Information about the health of a target.

## Contents
<a name="API_TargetHealthDescription_Contents"></a>

 ** AdministrativeOverride **
The administrative override information for the target.
Type: [AdministrativeOverride](API_AdministrativeOverride.md) object
Required: No

 ** AnomalyDetection **
The anomaly detection result for the target.
If no anomalies were detected, the result is `normal`.
If anomalies were detected, the result is `anomalous`.
Type: [AnomalyDetection](API_AnomalyDetection.md) object
Required: No

 ** HealthCheckPort **
The port to use to connect with the target.
Type: String
Required: No

 ** Target **
The description of the target.
Type: [TargetDescription](API_TargetDescription.md) object
Required: No

 ** TargetHealth **
The health information for the target.
Type: [TargetHealth](API_TargetHealth.md) object
Required: No

## See Also
<a name="API_TargetHealthDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TargetHealthDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TargetHealthDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TargetHealthDescription)
