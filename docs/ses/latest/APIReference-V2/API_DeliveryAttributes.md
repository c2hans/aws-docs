---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeliveryAttributes.html
---

# DeliveryAttributes

The delivery attributes that apply to your Amazon SES account in the current AWS Region.

## Contents
<a name="API_DeliveryAttributes_Contents"></a>

 ** SharedPoolDeliveryMode **   <a name="SES-Type-DeliveryAttributes-SharedPoolDeliveryMode"></a>
The shared pool delivery mode for your Amazon SES account in the current AWS Region. This mode applies to email that you send from shared IP addresses. Can be one of the following:
+  `GLOBAL` – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other AWS Regions within the same AWS partition.
+  `REGIONAL` – Amazon SES delivers your email only from shared IP addresses in your sending Region.
Accounts that start sending in a Region on or after the launch of Global Shared Delivery use `GLOBAL` in that Region.
Type: String
Valid Values: `GLOBAL | REGIONAL`
Required: No

## See Also
<a name="API_DeliveryAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeliveryAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeliveryAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeliveryAttributes)
