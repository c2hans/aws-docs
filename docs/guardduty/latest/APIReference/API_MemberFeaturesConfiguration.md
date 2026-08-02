---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberFeaturesConfiguration.html
---

# MemberFeaturesConfiguration
<a name="API_MemberFeaturesConfiguration"></a>

Contains information about the features for the member account.

## Contents
<a name="API_MemberFeaturesConfiguration_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-MemberFeaturesConfiguration-additionalConfiguration"></a>
Additional configuration of the feature for the member account.
Type: Array of [MemberAdditionalConfiguration](API_MemberAdditionalConfiguration.md) objects
Required: No

 ** name **   <a name="guardduty-Type-MemberFeaturesConfiguration-name"></a>
The name of the feature.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION`
Required: No

 ** status **   <a name="guardduty-Type-MemberFeaturesConfiguration-status"></a>
The status of the feature.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_MemberFeaturesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberFeaturesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberFeaturesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberFeaturesConfiguration)
