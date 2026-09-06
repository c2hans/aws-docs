---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PaymentConfiguration.html
---

# PaymentConfiguration
<a name="API_PaymentConfiguration"></a>

An object representing the collaboration member's payment responsibilities set by the collaboration creator.

## Contents
<a name="API_PaymentConfiguration_Contents"></a>

 ** queryCompute **   <a name="API-Type-PaymentConfiguration-queryCompute"></a>
The collaboration member's payment responsibilities set by the collaboration creator for query compute costs.
Type: [QueryComputePaymentConfig](API_QueryComputePaymentConfig.md) object
Required: Yes

 ** jobCompute **   <a name="API-Type-PaymentConfiguration-jobCompute"></a>
 The compute configuration for the job.
Type: [JobComputePaymentConfig](API_JobComputePaymentConfig.md) object
Required: No

 ** machineLearning **   <a name="API-Type-PaymentConfiguration-machineLearning"></a>
An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.
Type: [MLPaymentConfig](API_MLPaymentConfig.md) object
Required: No

## See Also
<a name="API_PaymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PaymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PaymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PaymentConfiguration)
