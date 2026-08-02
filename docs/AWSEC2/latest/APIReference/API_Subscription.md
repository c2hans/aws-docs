---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

Describes an Infrastructure Performance subscription.

## Contents
<a name="API_Subscription_Contents"></a>

 ** destination **
The Region or Availability Zone that's the target for the subscription. For example, `eu-west-1`.
Type: String
Required: No

 ** metric **
The metric used for the subscription.
Type: String
Valid Values: `aggregate-latency`
Required: No

 ** period **
The data aggregation time for the subscription.
Type: String
Valid Values: `five-minutes | fifteen-minutes | one-hour | three-hours | one-day | one-week`
Required: No

 ** source **
The Region or Availability Zone that's the source for the subscription. For example, `us-east-1`.
Type: String
Required: No

 ** statistic **
The statistic used for the subscription.
Type: String
Valid Values: `p50`
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Subscription)
