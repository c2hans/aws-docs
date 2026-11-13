---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ProtectionPlan.html
---

# ProtectionPlan
<a name="API_ProtectionPlan"></a>

Contains information about the status of a protection plan.

## Contents
<a name="API_ProtectionPlan_Contents"></a>

 ** name **   <a name="guardduty-Type-ProtectionPlan-name"></a>
The name of the protection plan. Possible values are `CLOUD_TRAIL`, `DNS_LOGS`, `FLOW_LOGS`, `S3_DATA_EVENTS`, `EKS_AUDIT_LOGS`, `EBS_MALWARE_PROTECTION`, `RDS_LOGIN_EVENTS`, `EKS_RUNTIME_MONITORING`, `EKS_ADDON_MANAGEMENT`, `LAMBDA_NETWORK_LOGS`, `RUNTIME_MONITORING`, `ECS_FARGATE_AGENT_MANAGEMENT`, and `EC2_AGENT_MANAGEMENT`.
Type: String
Valid Values: `CLOUD_TRAIL | DNS_LOGS | FLOW_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | EKS_RUNTIME_MONITORING | EKS_ADDON_MANAGEMENT | LAMBDA_NETWORK_LOGS | RUNTIME_MONITORING | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** status **   <a name="guardduty-Type-ProtectionPlan-status"></a>
The status of the protection plan. Possible values are `ENABLED` and `DISABLED`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ProtectionPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ProtectionPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ProtectionPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ProtectionPlan)
