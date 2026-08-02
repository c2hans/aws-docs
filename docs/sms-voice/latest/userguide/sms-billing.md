---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing.html
---

# Understanding SMS billing and usage reports for AWS End User Messaging SMS
<a name="sms-billing"></a>

The AWS End User Messaging SMS channel generates a usage type that contains five fields in the following format: `{{Region code}}–{{MessagingType}}–{{ISO}}–{{RouteType}}–{{OriginationID}}–{{MessageCount/Fee}}`. For example, SMS messages sent from the Asia Pacific (Tokyo) Region to a Japanese phone number would appear as **APN1–OutboundSMS–JP–Standard–Senderid–MessageCount**.

RCS messaging has a separate pricing model that includes per-message fees and carrier pass-through charges, as well as registration fees for agent setup and maintenance. For detailed information about RCS pricing, see [RCS billing and pricing model](rcs-billing.md).

The following table displays the possible values and descriptions for the fields in the usage type. For more information about per SMS message, per MMS message, or origination identity pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com//end-user-messaging/pricing/).

****

| Field | Options | Description |
| --- | --- | --- |
| {{Region code}} |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing.html) | The AWS Region prefix that indicates where the SMS message was sent from. |
| {{MessagingType}} | OutboundSMS | This field lists the message type being sent. For Outbound SMS, it reads OutboundSMS. |
| {{ISO}} | See [Supported countries and regions for SMS messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md) for the list of ISO country codes supported by AWS End User Messaging SMS. | The two–digit ISO country code that the message was sent to. |
| {{RouteType}} | Standard | The route type that the message was sent through. Currently, all messages are sent through the Standard route type. |
| {{OrginationID}} | TollFree, 10DLC, Shortcode, Longcode, Senderid, Sharedroute | This field specifies the origination identity that was used to send the message. See [Choosing an origination identity](phone-number-types.md) for more information about supported origination identities. |
| {{MessageCount/Fee}} | MessageCount, MessageFees, CarrierFeeCount, CarrierFees | This field displays either the number of messages sent or the cost associated with sending those messages. [See the AWS documentation website for more details](http://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing.html)  |

Messages sent through AWS End User Messaging SMS for Outbound SMS generate 2 – 4 usage types per combination of ISO country and origination identity. View the following examples to better understand how the usage types appear on your bill.

## Example 1: Sending messages to the United Kingdom
<a name="sms-billing-example1"></a>

Suppose you sent 10 messages to the United Kingdom (ISO code GB) using a short code from USE1. Then you can expect the following two usage types in your bill:

```
  1. USE1-OutboundSMS-GB-Standard-Shortcode-MessageCount
  2. USE1-OutboundSMS-GB-Standard-Shortcode-MessageFee
```

## Example 2: Sending messages to the United States
<a name="sms-billing-example2"></a>

Suppose you sent 10 messages to the United States (ISO code US) using a 10DLC number from CAN1. Then you can expect the following four usage types in your bill:

```
  1. CAN1-OutboundSMS-US-Standard-10DLC-MessageCount
  2. CAN1-OutboundSMS-US-Standard-10DLC-MessageFee
  3. CAN1-OutboundSMS-US-Standard-10DLC-CarrierFeeCount
  4. CAN1-OutboundSMS-US-Standard-10DLC-CarrierFees
```
