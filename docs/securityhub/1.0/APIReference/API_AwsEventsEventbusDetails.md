---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEventsEventbusDetails.html
---

# AwsEventsEventbusDetails
<a name="API_AwsEventsEventbusDetails"></a>

 Provides details about Amazon EventBridge event bus. An event bus is a router that receives events and delivers them to zero or more destinations, or targets. This can be a custom event bus which you can use to receive events from your custom applications and services, or it can be a partner event bus which can be matched to a partner event source.

## Contents
<a name="API_AwsEventsEventbusDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsEventsEventbusDetails-Arn"></a>
 The Amazon Resource Name (ARN) of the account permitted to write events to the current account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsEventsEventbusDetails-Name"></a>
 The name of the event bus.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Policy **   <a name="securityhub-Type-AwsEventsEventbusDetails-Policy"></a>
 The policy that enables the external account to send events to your account.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEventsEventbusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEventsEventbusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEventsEventbusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEventsEventbusDetails)
