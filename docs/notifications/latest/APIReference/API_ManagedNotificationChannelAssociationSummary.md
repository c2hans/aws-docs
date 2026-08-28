---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChannelAssociationSummary.html
---

# ManagedNotificationChannelAssociationSummary
<a name="API_ManagedNotificationChannelAssociationSummary"></a>

Provides a summary of channel associations for a managed notification configuration.

## Contents
<a name="API_ManagedNotificationChannelAssociationSummary_Contents"></a>

 ** channelIdentifier **   <a name="Notifications-Type-ManagedNotificationChannelAssociationSummary-channelIdentifier"></a>
The unique identifier for the notification channel.
Type: String
Required: Yes

 ** channelType **   <a name="Notifications-Type-ManagedNotificationChannelAssociationSummary-channelType"></a>
The type of notification channel used for message delivery.
+ Values:
  +  `ACCOUNT_CONTACT`
    + Delivers notifications to Account Managed contacts through the User Notification Service.
  +  `MOBILE`
    + Delivers notifications through the AWS Console Mobile Application to mobile devices.
  +  `CHATBOT`
    + Delivers notifications through Amazon Q Developer in chat applications to collaboration platforms (Slack, Chime).
  +  `EMAIL`
    + Delivers notifications to email addresses.
Type: String
Valid Values: `MOBILE | CHATBOT | EMAIL | ACCOUNT_CONTACT`
Required: Yes

 ** overrideOption **   <a name="Notifications-Type-ManagedNotificationChannelAssociationSummary-overrideOption"></a>
Controls whether users can modify channel associations for a notification configuration.
+ Values:
  +  `ENABLED`
    + Users can associate or disassociate channels with the notification configuration.
  +  `DISABLED`
    + Users cannot associate or disassociate channels with the notification configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ManagedNotificationChannelAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationChannelAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationChannelAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationChannelAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
