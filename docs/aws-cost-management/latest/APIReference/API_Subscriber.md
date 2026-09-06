---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Subscriber.html
---

# Subscriber
<a name="API_Subscriber"></a>

The recipient of `AnomalySubscription` notifications.

## Contents
<a name="API_Subscriber_Contents"></a>

 ** Address **   <a name="awscostmanagement-Type-Subscriber-Address"></a>
The email address or SNS Amazon Resource Name (ARN). This depends on the `Type`.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 302.
Pattern: `(^[a-zA-Z0-9.!#$%&'*+=?^_‘{|}~-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$)|(^arn:(aws[a-zA-Z-]*):sns:[a-zA-Z0-9-]+:[0-9]{12}:[a-zA-Z0-9_-]+(\.fifo)?$)`
Required: No

 ** Status **   <a name="awscostmanagement-Type-Subscriber-Status"></a>
Indicates if the subscriber accepts the notifications.
Type: String
Valid Values: `CONFIRMED | DECLINED`
Required: No

 ** Type **   <a name="awscostmanagement-Type-Subscriber-Type"></a>
The notification delivery channel.
Type: String
Valid Values: `EMAIL | SNS`
Required: No

## See Also
<a name="API_Subscriber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/Subscriber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/Subscriber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/Subscriber)
