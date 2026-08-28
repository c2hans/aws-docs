---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_EventRuleStatusSummary.html
---

# EventRuleStatusSummary
<a name="API_EventRuleStatusSummary"></a>

Provides additional information about the current `EventRule` status.

## Contents
<a name="API_EventRuleStatusSummary_Contents"></a>

 ** reason **   <a name="Notifications-Type-EventRuleStatusSummary-reason"></a>
A human-readable reason for `EventRuleStatus`.
Type: String
Required: Yes

 ** status **   <a name="Notifications-Type-EventRuleStatusSummary-status"></a>
The status of the `EventRule`.
+ Values:
  +  `ACTIVE`
    + The `EventRule` can process events.
  +  `INACTIVE`
    + The `EventRule` may be unable to process events.
  +  `CREATING`
    + The `EventRule` is being created.

      Only `GET` and `LIST` calls can be run.
  +  `UPDATING`
    + The `EventRule` is being updated.

      Only `GET` and `LIST` calls can be run.
  +  `DELETING`
    + The `EventRule` is being deleted.

      Only `GET` and `LIST` calls can be run.
Type: String
Valid Values: `ACTIVE | INACTIVE | CREATING | UPDATING | DELETING`
Required: Yes

## See Also
<a name="API_EventRuleStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/EventRuleStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/EventRuleStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/EventRuleStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
