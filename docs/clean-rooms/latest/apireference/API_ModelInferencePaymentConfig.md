---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ModelInferencePaymentConfig.html
---

# ModelInferencePaymentConfig
<a name="API_ModelInferencePaymentConfig"></a>

An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

## Contents
<a name="API_ModelInferencePaymentConfig_Contents"></a>

 ** isResponsible **   <a name="API-Type-ModelInferencePaymentConfig-isResponsible"></a>
Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs (`TRUE`) or has not configured the collaboration member to pay for model inference costs (`FALSE`).
One or more members can be configured as payer candidates for model inference costs.
If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer.
Type: Boolean
Required: Yes

## See Also
<a name="API_ModelInferencePaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ModelInferencePaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ModelInferencePaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ModelInferencePaymentConfig)
