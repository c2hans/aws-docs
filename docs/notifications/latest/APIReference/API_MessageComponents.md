---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_MessageComponents.html
---

# MessageComponents
<a name="API_MessageComponents"></a>

Describes the components of a notification message.

## Contents
<a name="API_MessageComponents_Contents"></a>

 ** completeDescription **   <a name="Notifications-Type-MessageComponents-completeDescription"></a>
A complete summary with all possible relevant information.
Type: String
Required: No

 ** dimensions **   <a name="Notifications-Type-MessageComponents-dimensions"></a>
A list of properties in key-value pairs. Pairs are shown in order of importance from most important to least important. Channels may limit the number of dimensions shown to the notification viewer.
Included dimensions, keys, and values are subject to change.
Type: Array of [Dimension](API_Dimension.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** headline **   <a name="Notifications-Type-MessageComponents-headline"></a>
A sentence long summary. For example, titles or an email subject line.
Type: String
Required: No

 ** paragraphSummary **   <a name="Notifications-Type-MessageComponents-paragraphSummary"></a>
A paragraph long or multiple sentence summary. For example, Amazon Q Developer in chat applications notifications.
Type: String
Required: No

## See Also
<a name="API_MessageComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/MessageComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/MessageComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/MessageComponents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
