---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityNotificationAttributes.html
---

# IdentityNotificationAttributes
<a name="API_IdentityNotificationAttributes"></a>

Represents the notification attributes of an identity, including whether an identity has Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or delivery notifications, and whether feedback forwarding is enabled for bounce and complaint notifications.

## Contents
<a name="API_IdentityNotificationAttributes_Contents"></a>

 ** BounceTopic **
The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes bounce notifications.
Type: String
Required: Yes

 ** ComplaintTopic **
The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes complaint notifications.
Type: String
Required: Yes

 ** DeliveryTopic **
The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES publishes delivery notifications.
Type: String
Required: Yes

 ** ForwardingEnabled **
Describes whether Amazon SES forwards bounce and complaint notifications as email. `true` indicates that Amazon SES forwards bounce and complaint notifications as email, while `false` indicates that bounce and complaint notifications are published only to the specified bounce and complaint Amazon SNS topics.
Type: Boolean
Required: Yes

 ** HeadersInBounceNotificationsEnabled **
Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type `Bounce`. A value of `true` specifies that Amazon SES includes headers in bounce notifications, and a value of `false` specifies that Amazon SES does not include headers in bounce notifications.
Type: Boolean
Required: No

 ** HeadersInComplaintNotificationsEnabled **
Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type `Complaint`. A value of `true` specifies that Amazon SES includes headers in complaint notifications, and a value of `false` specifies that Amazon SES does not include headers in complaint notifications.
Type: Boolean
Required: No

 ** HeadersInDeliveryNotificationsEnabled **
Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type `Delivery`. A value of `true` specifies that Amazon SES includes headers in delivery notifications, and a value of `false` specifies that Amazon SES does not include headers in delivery notifications.
Type: Boolean
Required: No

## See Also
<a name="API_IdentityNotificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/IdentityNotificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/IdentityNotificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/IdentityNotificationAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
