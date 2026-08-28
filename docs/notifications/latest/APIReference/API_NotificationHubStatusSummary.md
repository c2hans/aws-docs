---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationHubStatusSummary.html
---

# NotificationHubStatusSummary
<a name="API_NotificationHubStatusSummary"></a>

Provides additional information about the current `NotificationHub` status.

## Contents
<a name="API_NotificationHubStatusSummary_Contents"></a>

 ** reason **   <a name="Notifications-Type-NotificationHubStatusSummary-reason"></a>
An explanation for the current status.
Type: String
Required: Yes

 ** status **   <a name="Notifications-Type-NotificationHubStatusSummary-status"></a>
Status information about the `NotificationHub`.
+ Values:
  +  `ACTIVE`
    + Incoming `NotificationEvents` are replicated to this `NotificationHub`.
  +  `REGISTERING`
    + The `NotificationConfiguration` is initializing. A `NotificationConfiguration` with this status can't be deregistered.
  +  `DEREGISTERING`
    + The `NotificationConfiguration` is being deleted. You can't register additional `NotificationHubs` in the same Region as a `NotificationConfiguration` with this status.
Type: String
Valid Values: `ACTIVE | REGISTERING | DEREGISTERING | INACTIVE`
Required: Yes

## See Also
<a name="API_NotificationHubStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationHubStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationHubStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationHubStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
