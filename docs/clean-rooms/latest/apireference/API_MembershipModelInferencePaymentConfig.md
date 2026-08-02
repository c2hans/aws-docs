---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipModelInferencePaymentConfig.html
---

# MembershipModelInferencePaymentConfig
<a name="API_MembershipModelInferencePaymentConfig"></a>

An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

## Contents
<a name="API_MembershipModelInferencePaymentConfig_Contents"></a>

 ** isResponsible **   <a name="API-Type-MembershipModelInferencePaymentConfig-isResponsible"></a>
Indicates whether the collaboration member has accepted to pay for model inference costs (`TRUE`) or has not accepted to pay for model inference costs (`FALSE`).
If the collaboration creator has not specified anyone to pay for model inference costs, then the member who can query is the default payer.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for model inference costs.
+ If you set the value to `TRUE` but you are not responsible to pay for model inference costs.
Type: Boolean
Required: Yes

## See Also
<a name="API_MembershipModelInferencePaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipModelInferencePaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipModelInferencePaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipModelInferencePaymentConfig)
