---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AccessBudget.html
---

# AccessBudget
<a name="API_AccessBudget"></a>

Controls and tracks usage limits for associated configured tables within a collaboration across queries and job. Supports both period-based budgets that can renew (daily, weekly, or monthly) and fixed lifetime budgets. Contains the resource ARN, remaining budget information, and up to two budget configurations (period-based and lifetime). By default, table usage is unlimited unless a budget is configured.

## Contents
<a name="API_AccessBudget_Contents"></a>

 ** aggregateRemainingBudget **   <a name="API-Type-AccessBudget-aggregateRemainingBudget"></a>
The total remaining budget across all budget parameters, showing the lower value between the per-period budget and lifetime budget for this access budget. For individual parameter budgets, see `remainingBudget`.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** details **   <a name="API-Type-AccessBudget-details"></a>
Detailed budget information including time bounds, remaining budget, and refresh settings.
Type: Array of [AccessBudgetDetails](API_AccessBudgetDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** resourceArn **   <a name="API-Type-AccessBudget-resourceArn"></a>
The Amazon Resource Name (ARN) of the access budget resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/(configuredtableassociation|intermediatetable)/[\d\w-]+`
Required: Yes

## See Also
<a name="API_AccessBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AccessBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AccessBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AccessBudget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
