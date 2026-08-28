---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_budgets_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# AWS Budgets examples using Tools for PowerShell V4
<a name="powershell_budgets_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with AWS Budgets.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `New-BGTBudget`
<a name="budgets_CreateBudget_powershell_topic"></a>

The following code example shows how to use `New-BGTBudget`.

**Tools for PowerShell V4**
**Example 1: Creates a new budget with the specified budgetary and time constraints with email notifications.**

```
$notification = @{
    NotificationType = "ACTUAL"
    ComparisonOperator = "GREATER_THAN"
    Threshold = 80
}

$addressObject = @{
    Address = @("user@domain.com")
    SubscriptionType = "EMAIL"
}

$subscriber = New-Object Amazon.Budgets.Model.NotificationWithSubscribers
$subscriber.Notification = $notification
$subscriber.Subscribers.Add($addressObject)

$startDate = [datetime]::new(2017,09,25)
$endDate = [datetime]::new(2017,10,25)

New-BGTBudget -Budget_BudgetName "Tester" -Budget_BudgetType COST -CostTypes_IncludeTax $true -Budget_TimeUnit MONTHLY -BudgetLimit_Unit USD -TimePeriod_Start $startDate -TimePeriod_End $endDate -AccountId 123456789012 -BudgetLimit_Amount 200 -NotificationsWithSubscriber $subscriber
```
+  For API details, see [CreateBudget](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
