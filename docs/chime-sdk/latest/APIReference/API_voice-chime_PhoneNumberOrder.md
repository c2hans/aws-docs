---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberOrder.html
---

# PhoneNumberOrder
<a name="API_voice-chime_PhoneNumberOrder"></a>

The details of an Amazon Chime SDK phone number order.

## Contents
<a name="API_voice-chime_PhoneNumberOrder_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-CreatedTimestamp"></a>
The phone number order creation time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** FocDate **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-FocDate"></a>
The Firm Order Commitment (FOC) date for phone number porting orders. This field is null if a phone number order is not a porting order.
Type: Timestamp
Required: No

 ** OrderedPhoneNumbers **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-OrderedPhoneNumbers"></a>
The ordered phone number details, such as the phone number in E.164 format and the phone number status.
Type: Array of [OrderedPhoneNumber](API_voice-chime_OrderedPhoneNumber.md) objects
Required: No

 ** OrderType **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-OrderType"></a>
The type of phone number being ordered, local or toll-free.
Type: String
Valid Values: `New | Porting`
Required: No

 ** PhoneNumberOrderId **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-PhoneNumberOrderId"></a>
The ID of the phone order.
Type: String
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** ProductType **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-ProductType"></a>
The phone number order product type.
Type: String
Valid Values: `VoiceConnector | SipMediaApplicationDialIn`
Required: No

 ** Status **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-Status"></a>
The status of the phone number order.
Type: String
Valid Values: `Processing | Successful | Failed | Partial | PendingDocuments | Submitted | FOC | ChangeRequested | Exception | CancelRequested | Cancelled`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_PhoneNumberOrder-UpdatedTimestamp"></a>
The updated phone number order time stamp, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_voice-chime_PhoneNumberOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PhoneNumberOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PhoneNumberOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PhoneNumberOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
