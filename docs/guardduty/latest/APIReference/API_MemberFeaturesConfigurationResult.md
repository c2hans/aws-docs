---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberFeaturesConfigurationResult.html
---

# MemberFeaturesConfigurationResult
<a name="API_MemberFeaturesConfigurationResult"></a>

Contains information about the features for the member account.

## Contents
<a name="API_MemberFeaturesConfigurationResult_Contents"></a>

 ** additionalConfiguration **   <a name="guardduty-Type-MemberFeaturesConfigurationResult-additionalConfiguration"></a>
Indicates the additional configuration of the feature that is configured for the member account.
Type: Array of [MemberAdditionalConfigurationResult](API_MemberAdditionalConfigurationResult.md) objects
Required: No

 ** name **   <a name="guardduty-Type-MemberFeaturesConfigurationResult-name"></a>
Indicates the name of the feature that is enabled for the detector.
Type: String
Valid Values: `S3_DATA_EVENTS | EKS_AUDIT_LOGS | EBS_MALWARE_PROTECTION | RDS_LOGIN_EVENTS | LAMBDA_NETWORK_LOGS | EKS_RUNTIME_MONITORING | RUNTIME_MONITORING | AI_PROTECTION`
Required: No

 ** status **   <a name="guardduty-Type-MemberFeaturesConfigurationResult-status"></a>
Indicates the status of the feature that is enabled for the detector.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** updatedAt **   <a name="guardduty-Type-MemberFeaturesConfigurationResult-updatedAt"></a>
The timestamp at which the feature object was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_MemberFeaturesConfigurationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberFeaturesConfigurationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberFeaturesConfigurationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberFeaturesConfigurationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
