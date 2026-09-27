---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_SubscriberSummary.html
---

# SubscriberSummary
<a name="API_SubscriberSummary"></a>

Summary of a subscriber, as returned by ListSubscribers.

## Contents
<a name="API_SubscriberSummary_Contents"></a>

 ** CreationTime **   <a name="eventbridgev2-Type-SubscriberSummary-CreationTime"></a>
The time the subscriber was created.
Type: Timestamp
Required: No

 ** EventBusArn **   <a name="eventbridgev2-Type-SubscriberSummary-EventBusArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: No

 ** LastModifiedTime **   <a name="eventbridgev2-Type-SubscriberSummary-LastModifiedTime"></a>
The time the subscriber was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridgev2-Type-SubscriberSummary-Name"></a>
Name of a subscriber. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][\.\-_A-Za-z0-9]*`
Required: No

 ** Revoked **   <a name="eventbridgev2-Type-SubscriberSummary-Revoked"></a>
True when the bus owner has revoked this subscriber. Present only when true, so a bus owner listing subscribers sees at a glance which ones they revoked. See DescribeSubscriberResponse$Revoked.
Type: Boolean
Required: No

 ** State **   <a name="eventbridgev2-Type-SubscriberSummary-State"></a>
Customer-controlled run state of a subscriber, set on create or update. Distinct from the bus lifecycle vocabulary, where ACTIVE means "provisioned and healthy". Delivery requires State RUNNING on a subscriber that is not revoked.
Type: String
Valid Values: `RUNNING | STOPPED`
Required: No

 ** SubscriberAccountId **   <a name="eventbridgev2-Type-SubscriberSummary-SubscriberAccountId"></a>
AWS Account Id.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** SubscriberArn **   <a name="eventbridgev2-Type-SubscriberSummary-SubscriberArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a subscriber.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):subscriber\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: No

 ** TargetArn **   <a name="eventbridgev2-Type-SubscriberSummary-TargetArn"></a>
ARN of the target a subscriber invokes. The resource grammar is service-neutral because target services use different separators and the USI form omits region and account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `arn:aws(-[a-z0-9]+)*:[^\s]+(?![\s\S]).*`
Required: No

 ** Type **   <a name="eventbridgev2-Type-SubscriberSummary-Type"></a>
Delivery ordering mode of a subscriber: FIFO delivers events in order within an event group; UNORDERED delivers without an ordering guarantee.
Type: String
Valid Values: `FIFO | UNORDERED`
Required: No

## See Also
<a name="API_SubscriberSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/SubscriberSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/SubscriberSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/SubscriberSummary)
