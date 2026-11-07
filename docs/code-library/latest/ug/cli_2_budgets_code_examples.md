---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_budgets_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Budgets examples using AWS CLI
<a name="cli_2_budgets_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Budgets.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-budget`
<a name="budgets_CreateBudget_cli_2_topic"></a>

The following code example shows how to use `create-budget`.

**AWS CLI**
**To create a Cost and Usage budget**
The following `create-budget` example creates a Cost and Usage budget.

```
aws budgets create-budget \
    --account-id {{123456789012}} \
    --budget {{file://budget.json}} \
    --notifications-with-subscribers {{file://notifications-with-subscribers.json}}
```
Contents of `budget.json`:

```
{
    "BudgetLimit": {
        "Amount": "100",
        "Unit": "USD"
    },
    "BudgetName": "Example Tag Budget",
    "BudgetType": "COST",
    "CostFilters": {
        "TagKeyValue": [
            "user:Key$value1",
            "user:Key$value2"
        ]
    },
    "CostTypes": {
        "IncludeCredit": true,
        "IncludeDiscount": true,
        "IncludeOtherSubscription": true,
        "IncludeRecurring": true,
        "IncludeRefund": true,
        "IncludeSubscription": true,
        "IncludeSupport": true,
        "IncludeTax": true,
        "IncludeUpfront": true,
        "UseBlended": false
    },
    "TimePeriod": {
        "Start": 1477958399,
        "End": 3706473600
    },
    "TimeUnit": "MONTHLY"
}
```
This command produces no output.
Contents of `notifications-with-subscribers.json`:

```
[
    {
        "Notification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [
            {
                "Address": "example@example.com",
                "SubscriptionType": "EMAIL"
            }
        ]
    }
]
```
For more information, see [Creating a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) in the *AWS Cost Management User Guide*.
+  For API details, see [CreateBudget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-budget.html) in *AWS CLI Command Reference*.

### `create-notification`
<a name="budgets_CreateNotification_cli_2_topic"></a>

The following code example shows how to use `create-notification`.

**AWS CLI**
**To create a notification for the specified Cost and Usage budget**
The following `create-notification` example creates a notification for the specified Cost and Usage budget.

```
aws budgets create-notification \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --subscribers {{SubscriptionType=EMAIL,Address=example@example.com}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [CreateNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-notification.html) in *AWS CLI Command Reference*.

### `create-subscriber`
<a name="budgets_CreateSubscriber_cli_2_topic"></a>

The following code example shows how to use `create-subscriber`.

**AWS CLI**
**To create a subscriber for a notification associated with a Cost and Usage budget**
The following `create-subscriber` example creates a subscriber for the specified notification.

```
aws budgets create-subscriber \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --subscriber {{SubscriptionType=EMAIL,Address=example@example.com}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [CreateSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/create-subscriber.html) in *AWS CLI Command Reference*.

### `delete-budget`
<a name="budgets_DeleteBudget_cli_2_topic"></a>

The following code example shows how to use `delete-budget`.

**AWS CLI**
**To delete a Cost and Usage budget**
The following `delete-budget` example deletes the specified Cost and Usage budget.

```
aws budgets delete-budget \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}}
```
This command produces no output.
For more information, see [Deleting a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-delete.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DeleteBudget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-budget.html) in *AWS CLI Command Reference*.

### `delete-notification`
<a name="budgets_DeleteNotification_cli_2_topic"></a>

The following code example shows how to use `delete-notification`.

**AWS CLI**
**To delete a notification from a budget**
The following `delete-notification` example deletes the specified notification from the specified budget.

```
aws budgets delete-notification \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DeleteNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-notification.html) in *AWS CLI Command Reference*.

### `delete-subscriber`
<a name="budgets_DeleteSubscriber_cli_2_topic"></a>

The following code example shows how to use `delete-subscriber`.

**AWS CLI**
**To delete a subscriber from a notification**
The following `delete-subscriber` example deletes the specified subscriber from the specified notification.

```
aws budgets delete-subscriber \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --subscriber {{SubscriptionType=EMAIL,Address=example@example.com}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DeleteSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/delete-subscriber.html) in *AWS CLI Command Reference*.

### `describe-budget`
<a name="budgets_DescribeBudget_cli_2_topic"></a>

The following code example shows how to use `describe-budget`.

**AWS CLI**
**To retrieve a budget associated with an account**
The following `describe-budget` example retrieves the specified Cost and Usage budget.

```
aws budgets describe-budget \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}}
```
Output:

```
{
    "Budget": {
        "CalculatedSpend": {
            "ForecastedSpend": {
                "Amount": "2641.54800000000022919266484677791595458984375",
                "Unit": "USD"
            },
            "ActualSpend": {
                "Amount": "604.4560000000000172803993336856365203857421875",
                "Unit": "USD"
            }
        },
        "BudgetType": "COST",
        "BudgetLimit": {
            "Amount": "100",
            "Unit": "USD"
        },
        "BudgetName": "Example Budget",
        "CostTypes": {
            "IncludeOtherSubscription": true,
            "IncludeUpfront": true,
            "IncludeRefund": true,
            "UseBlended": false,
            "IncludeDiscount": true,
            "UseAmortized": false,
            "IncludeTax": true,
            "IncludeCredit": true,
            "IncludeSupport": true,
            "IncludeRecurring": true,
            "IncludeSubscription": true
        },
        "TimeUnit": "MONTHLY",
        "TimePeriod": {
            "Start": 1477958399.0,
            "End": 3706473600.0
        },
        "CostFilters": {
            "AZ": [
                "us-west-2"
            ]
        }
    }
}
```
For more information, see [Viewing your budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-view.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DescribeBudget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budget.html) in *AWS CLI Command Reference*.

### `describe-budgets`
<a name="budgets_DescribeBudgets_cli_2_topic"></a>

The following code example shows how to use `describe-budgets`.

**AWS CLI**
**To retrieve the budgets associated with an account**
The following `describe-budgets` example retrieves the Cost and Usage budgets for an account.

```
aws budgets describe-budgets \
    --account-id {{123456789012}} \
    --max-results {{20}}
```
Output:

```
{
    "Budgets": [
        {
            "CalculatedSpend": {
                "ForecastedSpend": {
                    "Amount": "2641.54800000000022919266484677791595458984375",
                    "Unit": "USD"
                },
                "ActualSpend": {
                    "Amount": "604.4560000000000172803993336856365203857421875",
                    "Unit": "USD"
                }
            },
            "BudgetType": "COST",
            "BudgetLimit": {
                "Amount": "100",
                "Unit": "USD"
            },
            "BudgetName": "Example Budget",
            "CostTypes": {
                "IncludeOtherSubscription": true,
                "IncludeUpfront": true,
                "IncludeRefund": true,
                "UseBlended": false,
                "IncludeDiscount": true,
                "UseAmortized": false,
                "IncludeTax": true,
                "IncludeCredit": true,
                "IncludeSupport": true,
                "IncludeRecurring": true,
                "IncludeSubscription": true
            },
            "TimeUnit": "MONTHLY",
            "TimePeriod": {
                "Start": 1477958399.0,
                "End": 3706473600.0
            },
            "CostFilters": {
                "AZ": [
                    "us-west-2"
                ]
            }
        }
    ]
}
```
For more information, see [Viewing your budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-view.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DescribeBudgets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-budgets.html) in *AWS CLI Command Reference*.

### `describe-notifications-for-budget`
<a name="budgets_DescribeNotificationsForBudget_cli_2_topic"></a>

The following code example shows how to use `describe-notifications-for-budget`.

**AWS CLI**
**To retrieve the notifications for a budget**
The following `describe-notifications-for-budget` example retrieves the notifications for a Cost and Usage budget.

```
aws budgets describe-notifications-for-budget \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --max-results {{5}}
```
Output:

```
{
    "Notifications": [
        {
            "Threshold": 80.0,
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL"
        }
    ]
}
```
For more information, see [Viewing your budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-view.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DescribeNotificationsForBudget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-notifications-for-budget.html) in *AWS CLI Command Reference*.

### `describe-subscribers-for-notification`
<a name="budgets_DescribeSubscribersForNotification_cli_2_topic"></a>

The following code example shows how to use `describe-subscribers-for-notification`.

**AWS CLI**
**To retrieve the subscribers for a budget notification**
The following `describe-subscribers-for-notification` example retrieves the subscribers for a Cost and Usage budget notification.

```
aws budgets describe-subscribers-for-notification \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --max-results {{5}}
```
Output:

```
{
    "Subscribers": [
        {
            "SubscriptionType": "EMAIL",
            "Address": "example2@example.com"
        },
        {
            "SubscriptionType": "EMAIL",
            "Address": "example@example.com"
        }
    ]
}
```
For more information, see [Viewing your budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-view.html) in the *AWS Cost Management User Guide*.
+  For API details, see [DescribeSubscribersForNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/describe-subscribers-for-notification.html) in *AWS CLI Command Reference*.

### `update-budget`
<a name="budgets_UpdateBudget_cli_2_topic"></a>

The following code example shows how to use `update-budget`.

**AWS CLI**
**To replace a budget for a Cost and Usage budget**
The following `update-budget` example replaces a Cost and Usage budget with a new budget.

```
aws budgets update-budget \
    --account-id {{123456789012}} \
    --new-budget {{file://new-budget.json}}
```
Contents of `new-budget.json`:

```
{
    "BudgetLimit": {
        "Amount": "100",
        "Unit": "USD"
    },
    "BudgetName": "Example Budget",
    "BudgetType": "COST",
    "CostFilters": {
        "AZ": [
            "us-west-2"
        ]
    },
    "CostTypes": {
        "IncludeCredit": false,
        "IncludeDiscount": true,
        "IncludeOtherSubscription": true,
        "IncludeRecurring": true,
        "IncludeRefund": true,
        "IncludeSubscription": true,
        "IncludeSupport": true,
        "IncludeTax": true,
        "IncludeUpfront": true,
        "UseBlended": false,
        "UseAmortized": true
    },
    "TimePeriod": {
        "Start": 1477958399,
        "End": 3706473600
    },
    "TimeUnit": "MONTHLY"
}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [UpdateBudget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-budget.html) in *AWS CLI Command Reference*.

### `update-notification`
<a name="budgets_UpdateNotification_cli_2_topic"></a>

The following code example shows how to use `update-notification`.

**AWS CLI**
**To replace a notification for a Cost and Usage budget**
The following `update-notification` example replaces an 80% notification for a Cost and Usage budget with a 90% notification.

```
aws budgets update-notification \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --old-notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --new-notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=90,ThresholdType=PERCENTAGE}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [UpdateNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-notification.html) in *AWS CLI Command Reference*.

### `update-subscriber`
<a name="budgets_UpdateSubscriber_cli_2_topic"></a>

The following code example shows how to use `update-subscriber`.

**AWS CLI**
**To replace a subscriber for a Cost and Usage budget**
The following `update-subscriber` example replaces the subscriber for a Cost and Usage budget.

```
aws budgets update-subscriber \
    --account-id {{123456789012}} \
    --budget-name {{"Example Budget"}} \
    --notification {{NotificationType=ACTUAL,ComparisonOperator=GREATER_THAN,Threshold=80,ThresholdType=PERCENTAGE}} \
    --old-subscriber {{SubscriptionType=EMAIL,Address=example@example.com}} \
    --new-subscriber {{SubscriptionType=EMAIL,Address=example2@example.com}}
```
This command produces no output.
For more information, see [Editing a budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-edit.html) in the *AWS Cost Management User Guide*.
+  For API details, see [UpdateSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/budgets/update-subscriber.html) in *AWS CLI Command Reference*.
