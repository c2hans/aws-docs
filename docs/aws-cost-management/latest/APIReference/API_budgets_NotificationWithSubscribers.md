---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_NotificationWithSubscribers.html
---

# NotificationWithSubscribers
<a name="API_budgets_NotificationWithSubscribers"></a>

A notification with subscribers. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

## Contents
<a name="API_budgets_NotificationWithSubscribers_Contents"></a>

 ** Notification **   <a name="awscostmanagement-Type-budgets_NotificationWithSubscribers-Notification"></a>
The notification that's associated with a budget.
Type: [Notification](API_budgets_Notification.md) object
Required: Yes

 ** Subscribers **   <a name="awscostmanagement-Type-budgets_NotificationWithSubscribers-Subscribers"></a>
A list of subscribers who are subscribed to this notification.
Type: Array of [Subscriber](API_budgets_Subscriber.md) objects
Array Members: Minimum number of 1 item. Maximum number of 11 items.
Required: Yes

## See Also
<a name="API_budgets_NotificationWithSubscribers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/NotificationWithSubscribers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/NotificationWithSubscribers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/NotificationWithSubscribers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
