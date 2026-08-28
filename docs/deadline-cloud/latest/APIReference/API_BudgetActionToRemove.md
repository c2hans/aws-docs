---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BudgetActionToRemove.html
---

# BudgetActionToRemove
<a name="API_BudgetActionToRemove"></a>

The budget action to remove.

## Contents
<a name="API_BudgetActionToRemove_Contents"></a>

 ** thresholdPercentage **   <a name="deadlinecloud-Type-BudgetActionToRemove-thresholdPercentage"></a>
The percentage threshold for the budget action to remove.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** type **   <a name="deadlinecloud-Type-BudgetActionToRemove-type"></a>
The type of budget action to remove.
Type: String
Valid Values: `STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`
Required: Yes

## See Also
<a name="API_BudgetActionToRemove_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BudgetActionToRemove)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BudgetActionToRemove)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BudgetActionToRemove)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
