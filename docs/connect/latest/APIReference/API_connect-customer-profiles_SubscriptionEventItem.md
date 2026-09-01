---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_SubscriptionEventItem.html
---

# SubscriptionEventItem
<a name="API_connect-customer-profiles_SubscriptionEventItem"></a>

Represents a single segment membership event.

## Contents
<a name="API_connect-customer-profiles_SubscriptionEventItem_Contents"></a>

 ** Event **   <a name="connect-Type-connect-customer-profiles_SubscriptionEventItem-Event"></a>
Whether the profile joined or left the segment. The following are valid values:
+  **JOINED**: The profile joined the segment.
+  **LEFT**: The profile left the segment.
Type: String
Valid Values: `JOINED | LEFT`
Required: No

 ** EventType **   <a name="connect-Type-connect-customer-profiles_SubscriptionEventItem-EventType"></a>
The type of event that triggered the membership change. The following are valid values:
+  **LIVE**: Real-time event triggered by a profile or calculated attribute change (Classic segments only).
+  **SCHEDULE**: Event generated during a scheduled execution.
Type: String
Valid Values: `LIVE | SCHEDULE`
Required: No

 ** ProfileId **   <a name="connect-Type-connect-customer-profiles_SubscriptionEventItem-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`
Required: No

 ** UpdatedAt **   <a name="connect-Type-connect-customer-profiles_SubscriptionEventItem-UpdatedAt"></a>
The timestamp of when the membership change was detected.
Type: Timestamp
Required: No

## See Also
<a name="API_connect-customer-profiles_SubscriptionEventItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SubscriptionEventItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SubscriptionEventItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SubscriptionEventItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
