---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormTrait.html
---

# RxNormTrait
<a name="API_RxNormTrait"></a>

The contextual information for the entity. InferRxNorm recognizes the trait `NEGATION`, which is any indication that the patient is not taking a medication.

## Contents
<a name="API_RxNormTrait_Contents"></a>

 ** Name **   <a name="comprehendmedical-Type-RxNormTrait-Name"></a>
Provides a name or contextual description about the trait.
Type: String
Valid Values: `NEGATION | PAST_HISTORY`
Required: No

 ** Score **   <a name="comprehendmedical-Type-RxNormTrait-Score"></a>
The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected trait.
Type: Float
Required: No

## See Also
<a name="API_RxNormTrait_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/RxNormTrait)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/RxNormTrait)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/RxNormTrait)
