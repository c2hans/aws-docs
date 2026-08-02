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
