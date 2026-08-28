---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Notification.html
---

# Notification
<a name="API_budgets_Notification"></a>

A notification that's associated with a budget. A budget can have up to ten notifications.

Each notification must have at least one subscriber. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

For example, if you have a budget for 200 dollars and you want to be notified when you go over 160 dollars, create a notification with the following parameters:
+ A notificationType of `ACTUAL`
+ A `thresholdType` of `PERCENTAGE`
+ A `comparisonOperator` of `GREATER_THAN`
+ A notification `threshold` of `80`

## Contents
<a name="API_budgets_Notification_Contents"></a>

 ** ComparisonOperator **   <a name="awscostmanagement-Type-budgets_Notification-ComparisonOperator"></a>
The comparison that's used for this notification.
Type: String
Valid Values: `GREATER_THAN | LESS_THAN | EQUAL_TO`
Required: Yes

 ** NotificationType **   <a name="awscostmanagement-Type-budgets_Notification-NotificationType"></a>
Specifies whether the notification is for how much you have spent (`ACTUAL`) or for how much that you're forecasted to spend (`FORECASTED`).
Type: String
Valid Values: `ACTUAL | FORECASTED`
Required: Yes

 ** Threshold **   <a name="awscostmanagement-Type-budgets_Notification-Threshold"></a>
The threshold that's associated with a notification. Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 15000000000000.
Required: Yes

 ** NotificationState **   <a name="awscostmanagement-Type-budgets_Notification-NotificationState"></a>
Specifies whether this notification is in alarm. If a budget notification is in the `ALARM` state, you passed the set threshold for the budget.
Type: String
Valid Values: `OK | ALARM`
Required: No

 ** ThresholdType **   <a name="awscostmanagement-Type-budgets_Notification-ThresholdType"></a>
The type of threshold for a notification. For `ABSOLUTE_VALUE` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For `PERCENTAGE` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a `PERCENTAGE` threshold of 80%, AWS notifies you when you go over 160 dollars.
Type: String
Valid Values: `PERCENTAGE | ABSOLUTE_VALUE`
Required: No

## See Also
<a name="API_budgets_Notification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Notification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Notification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Notification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
