---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_InstanceOnboardingJobStatus.html
---

# InstanceOnboardingJobStatus
<a name="API_connect-outbound-campaigns_InstanceOnboardingJobStatus"></a>

Contains information about the status of the workflow to onboard to outbound campaigns.

## Contents
<a name="API_connect-outbound-campaigns_InstanceOnboardingJobStatus_Contents"></a>

 ** connectInstanceId **   <a name="connect-Type-connect-outbound-campaigns_InstanceOnboardingJobStatus-connectInstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-_.a-zA-Z0-9]+`
Required: Yes

 ** status **   <a name="connect-Type-connect-outbound-campaigns_InstanceOnboardingJobStatus-status"></a>
The status of the workflow to onboard to outbound campaigns.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: Yes

 ** failureCode **   <a name="connect-Type-connect-outbound-campaigns_InstanceOnboardingJobStatus-failureCode"></a>
If the workflow is has failed, this is the failure code.
Type: String
Valid Values: `EVENT_BRIDGE_ACCESS_DENIED | EVENT_BRIDGE_MANAGED_RULE_LIMIT_EXCEEDED | IAM_ACCESS_DENIED | KMS_ACCESS_DENIED | KMS_KEY_NOT_FOUND | INTERNAL_FAILURE`
Required: No

## See Also
<a name="API_connect-outbound-campaigns_InstanceOnboardingJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/InstanceOnboardingJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/InstanceOnboardingJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/InstanceOnboardingJobStatus)
