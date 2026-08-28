---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipPaymentConfiguration.html
---

# MembershipPaymentConfiguration
<a name="API_MembershipPaymentConfiguration"></a>

An object representing the payment responsibilities accepted by the collaboration member.

## Contents
<a name="API_MembershipPaymentConfiguration_Contents"></a>

 ** queryCompute **   <a name="API-Type-MembershipPaymentConfiguration-queryCompute"></a>
The payment responsibilities accepted by the collaboration member for query compute costs.
Type: [MembershipQueryComputePaymentConfig](API_MembershipQueryComputePaymentConfig.md) object
Required: Yes

 ** jobCompute **   <a name="API-Type-MembershipPaymentConfiguration-jobCompute"></a>
The payment responsibilities accepted by the collaboration member for job compute costs.
Type: [MembershipJobComputePaymentConfig](API_MembershipJobComputePaymentConfig.md) object
Required: No

 ** machineLearning **   <a name="API-Type-MembershipPaymentConfiguration-machineLearning"></a>
The payment responsibilities accepted by the collaboration member for machine learning costs.
Type: [MembershipMLPaymentConfig](API_MembershipMLPaymentConfig.md) object
Required: No

## See Also
<a name="API_MembershipPaymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipPaymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipPaymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipPaymentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
