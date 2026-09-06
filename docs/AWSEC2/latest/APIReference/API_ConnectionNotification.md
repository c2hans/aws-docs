---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConnectionNotification.html
---

# ConnectionNotification
<a name="API_ConnectionNotification"></a>

Describes a connection notification for a VPC endpoint or VPC endpoint service.

## Contents
<a name="API_ConnectionNotification_Contents"></a>

 ** ConnectionEvents.N **
The events for the notification. Valid values are `Accept`, `Connect`, `Delete`, and `Reject`.
Type: Array of strings
Required: No

 ** connectionNotificationArn **
The ARN of the SNS topic for the notification.
Type: String
Required: No

 ** connectionNotificationId **
The ID of the notification.
Type: String
Required: No

 ** connectionNotificationState **
The state of the notification.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** connectionNotificationType **
The type of notification.
Type: String
Valid Values: `Topic`
Required: No

 ** serviceId **
The ID of the endpoint service.
Type: String
Required: No

 ** serviceRegion **
The Region for the endpoint service.
Type: String
Required: No

 ** vpcEndpointId **
The ID of the VPC endpoint.
Type: String
Required: No

## See Also
<a name="API_ConnectionNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ConnectionNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ConnectionNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ConnectionNotification)
