---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DetectionCoverage.html
---

# DetectionCoverage
<a name="API_DetectionCoverage"></a>

Contains information about your detection coverage, such as the status of protection plans and foundational data sources.

## Contents
<a name="API_DetectionCoverage_Contents"></a>

 ** coverageGaps **   <a name="guardduty-Type-DetectionCoverage-coverageGaps"></a>
A description of the gaps in detection coverage. A record doesn't include both `CoverageGaps` and `KeyObservation`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** foundationalDataSources **   <a name="guardduty-Type-DetectionCoverage-foundationalDataSources"></a>
The foundational data sources, such as `CLOUD_TRAIL`, `DNS_LOGS`, and `FLOW_LOGS`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Values: `CLOUD_TRAIL | DNS_LOGS | FLOW_LOGS | S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | EKS_RUNTIME_MONITORING | EKS_ADDON_MANAGEMENT | LAMBDA_NETWORK_LOGS | RUNTIME_MONITORING | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** keyObservation **   <a name="guardduty-Type-DetectionCoverage-keyObservation"></a>
A key observation about detection coverage.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** protectionPlans **   <a name="guardduty-Type-DetectionCoverage-protectionPlans"></a>
The protection plans and their status.
Type: Array of [ProtectionPlan](API_ProtectionPlan.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_DetectionCoverage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DetectionCoverage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DetectionCoverage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DetectionCoverage)
