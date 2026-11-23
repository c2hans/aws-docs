---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DeliveryOptions.html
---

# DeliveryOptions

Used to associate a configuration set with a dedicated IP pool.

## Contents
<a name="API_DeliveryOptions_Contents"></a>

 ** MaxDeliverySeconds **   <a name="SES-Type-DeliveryOptions-MaxDeliverySeconds"></a>
The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes).
Type: Long
Valid Range: Minimum value of 300. Maximum value of 50400.
Required: No

 ** SendingPoolName **   <a name="SES-Type-DeliveryOptions-SendingPoolName"></a>
The name of the dedicated IP pool to associate with the configuration set.
Type: String
Required: No

 ** SharedPoolDeliveryMode **   <a name="SES-Type-DeliveryOptions-SharedPoolDeliveryMode"></a>
The shared pool delivery mode for email that you send with the configuration set from shared IP addresses. This setting overrides the shared pool delivery mode of your account. Can be one of the following:
+  `GLOBAL` – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other AWS Regions within the same AWS partition.
+  `REGIONAL` – Amazon SES delivers your email only from shared IP addresses in your sending Region.
+  `ACCOUNT` – The configuration set uses the shared pool delivery mode of your account.
If you don't specify a value, the configuration set uses the shared pool delivery mode of your account.
Type: String
Valid Values: `GLOBAL | REGIONAL | ACCOUNT`
Required: No

 ** TlsPolicy **   <a name="SES-Type-DeliveryOptions-TlsPolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `REQUIRE`, messages are only delivered if a TLS connection can be established. If the value is `OPTIONAL`, messages can be delivered in plain text if a TLS connection can't be established.
Type: String
Valid Values: `REQUIRE | OPTIONAL`
Required: No

## See Also
<a name="API_DeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeliveryOptions)
