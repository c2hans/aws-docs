---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FreeTrialFeatureConfigurationResult.html
---

# FreeTrialFeatureConfigurationResult
<a name="API_FreeTrialFeatureConfigurationResult"></a>

Contains information about the free trial period for a feature.

## Contents
<a name="API_FreeTrialFeatureConfigurationResult_Contents"></a>

 ** freeTrialDaysRemaining **   <a name="guardduty-Type-FreeTrialFeatureConfigurationResult-freeTrialDaysRemaining"></a>
The number of the remaining free trial days for the feature.
Type: Integer
Required: No

 ** name **   <a name="guardduty-Type-FreeTrialFeatureConfigurationResult-name"></a>
The name of the feature for which the free trial is configured.
Type: String
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | EC2_RUNTIME_MONITORING | FARGATE_RUNTIME_MONITORING | AI_PROTECTION`
Required: No

## See Also
<a name="API_FreeTrialFeatureConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FreeTrialFeatureConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FreeTrialFeatureConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FreeTrialFeatureConfigurationResult)
