---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationDetectorFeatureConfiguration.html
---

# InvestigationDetectorFeatureConfiguration
<a name="API_InvestigationDetectorFeatureConfiguration"></a>

Contains information about the configuration of a detector feature. Each member is optional.

## Contents
<a name="API_InvestigationDetectorFeatureConfiguration_Contents"></a>

 ** name **   <a name="guardduty-Type-InvestigationDetectorFeatureConfiguration-name"></a>
The name of the feature. Possible values are `CLOUD_TRAIL`, `DNS_LOGS`, `FLOW_LOGS`, `S3_DATA_EVENTS`, `EKS_AUDIT_LOGS`, `EBS_MALWARE_PROTECTION`, `RDS_LOGIN_EVENTS`, `EKS_RUNTIME_MONITORING`, `EKS_ADDON_MANAGEMENT`, `LAMBDA_NETWORK_LOGS`, `RUNTIME_MONITORING`, `ECS_FARGATE_AGENT_MANAGEMENT`, and `EC2_AGENT_MANAGEMENT`.
Type: String
Valid Values: `CLOUD_TRAIL | DNS_LOGS | FLOW_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | EKS_RUNTIME_MONITORING | EKS_ADDON_MANAGEMENT | LAMBDA_NETWORK_LOGS | RUNTIME_MONITORING | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** status **   <a name="guardduty-Type-InvestigationDetectorFeatureConfiguration-status"></a>
The status of the feature. Possible values are `ENABLED` and `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** updatedAt **   <a name="guardduty-Type-InvestigationDetectorFeatureConfiguration-updatedAt"></a>
The timestamp at which the feature configuration was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_InvestigationDetectorFeatureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationDetectorFeatureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationDetectorFeatureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationDetectorFeatureConfiguration)
