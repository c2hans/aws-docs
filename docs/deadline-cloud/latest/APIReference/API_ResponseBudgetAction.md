---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ResponseBudgetAction.html
---

# ResponseBudgetAction
<a name="API_ResponseBudgetAction"></a>

The details of a budget action.

## Contents
<a name="API_ResponseBudgetAction_Contents"></a>

 ** thresholdPercentage **   <a name="deadlinecloud-Type-ResponseBudgetAction-thresholdPercentage"></a>
The percentage threshold for the budget.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** type **   <a name="deadlinecloud-Type-ResponseBudgetAction-type"></a>
The action taken on the budget once scheduling stops.
Type: String
Valid Values: `STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`
Required: Yes

 ** description **   <a name="deadlinecloud-Type-ResponseBudgetAction-description"></a>
The budget action description.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_ResponseBudgetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ResponseBudgetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ResponseBudgetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ResponseBudgetAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
