---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UsageFeatureResult.html
---

# UsageFeatureResult
<a name="API_UsageFeatureResult"></a>

Contains information about the result of the total usage based on the feature.

## Contents
<a name="API_UsageFeatureResult_Contents"></a>

 ** feature **   <a name="guardduty-Type-UsageFeatureResult-feature"></a>
The feature that generated the usage cost.
Type: String
Valid Values: `FLOW_LOGS | CLOUD_TRAIL | DNS_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | EC2_RUNTIME_MONITORING | FARGATE_RUNTIME_MONITORING | RDS_DBI_PROTECTION_PROVISIONED | RDS_DBI_PROTECTION_SERVERLESS | AI_PROTECTION`
Required: No

 ** total **   <a name="guardduty-Type-UsageFeatureResult-total"></a>
Contains the total usage with the corresponding currency unit for that value.
Type: [Total](API_Total.md) object
Required: No

## See Also
<a name="API_UsageFeatureResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UsageFeatureResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UsageFeatureResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UsageFeatureResult)
