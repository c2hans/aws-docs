---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_PhoneNumberOrder.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# PhoneNumberOrder
<a name="API_PhoneNumberOrder"></a>

The details of a phone number order created for Amazon Chime.

## Contents
<a name="API_PhoneNumberOrder_Contents"></a>

 ** CreatedTimestamp **   <a name="chime-Type-PhoneNumberOrder-CreatedTimestamp"></a>
The phone number order creation time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** OrderedPhoneNumbers **   <a name="chime-Type-PhoneNumberOrder-OrderedPhoneNumbers"></a>
The ordered phone number details, such as the phone number in E.164 format and the phone number status.
Type: Array of [OrderedPhoneNumber](API_OrderedPhoneNumber.md) objects
Required: No

 ** PhoneNumberOrderId **   <a name="chime-Type-PhoneNumberOrder-PhoneNumberOrderId"></a>
The phone number order ID.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** ProductType **   <a name="chime-Type-PhoneNumberOrder-ProductType"></a>
The phone number order product type.
Type: String
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`
Required: No

 ** Status **   <a name="chime-Type-PhoneNumberOrder-Status"></a>
The status of the phone number order.
Type: String
Valid Values: `Processing | Successful | Failed | Partial`
Required: No

 ** UpdatedTimestamp **   <a name="chime-Type-PhoneNumberOrder-UpdatedTimestamp"></a>
The updated phone number order time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_PhoneNumberOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/PhoneNumberOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/PhoneNumberOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/PhoneNumberOrder)
