---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateMembershipPaymentConfiguration.html
---

# UpdateMembershipPaymentConfiguration
<a name="API_UpdateMembershipPaymentConfiguration"></a>

An object representing the payment responsibilities to update for the membership.

## Contents
<a name="API_UpdateMembershipPaymentConfiguration_Contents"></a>

 ** jobCompute **   <a name="API-Type-UpdateMembershipPaymentConfiguration-jobCompute"></a>
An object representing the payment responsibilities accepted by the collaboration member for query and job compute costs.
Type: [MembershipJobComputePaymentConfig](API_MembershipJobComputePaymentConfig.md) object
Required: No

 ** machineLearning **   <a name="API-Type-UpdateMembershipPaymentConfiguration-machineLearning"></a>
An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.
Type: [MembershipMLPaymentConfig](API_MembershipMLPaymentConfig.md) object
Required: No

 ** queryCompute **   <a name="API-Type-UpdateMembershipPaymentConfiguration-queryCompute"></a>
An object representing the payment responsibilities accepted by the collaboration member for query compute costs.
Type: [MembershipQueryComputePaymentConfig](API_MembershipQueryComputePaymentConfig.md) object
Required: No

## See Also
<a name="API_UpdateMembershipPaymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateMembershipPaymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateMembershipPaymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateMembershipPaymentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
