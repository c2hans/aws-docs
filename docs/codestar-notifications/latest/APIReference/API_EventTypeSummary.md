---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_EventTypeSummary.html
---

# EventTypeSummary
<a name="API_EventTypeSummary"></a>

Returns information about an event that has triggered a notification rule.

## Contents
<a name="API_EventTypeSummary_Contents"></a>

 ** EventTypeId **   <a name="codestarnotifications-Type-EventTypeSummary-EventTypeId"></a>
The system-generated ID of the event. For a complete list of event types and IDs, see [Notification concepts](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api) in the *Developer Tools Console User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** EventTypeName **   <a name="codestarnotifications-Type-EventTypeSummary-EventTypeName"></a>
The name of the event.
Type: String
Required: No

 ** ResourceType **   <a name="codestarnotifications-Type-EventTypeSummary-ResourceType"></a>
The resource type of the event.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `^([a-zA-Z0-9-])+$`
Required: No

 ** ServiceName **   <a name="codestarnotifications-Type-EventTypeSummary-ServiceName"></a>
The name of the service for which the event applies.
Type: String
Required: No

## See Also
<a name="API_EventTypeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/EventTypeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/EventTypeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/EventTypeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
