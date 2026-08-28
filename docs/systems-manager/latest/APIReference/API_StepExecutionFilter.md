---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StepExecutionFilter.html
---

# StepExecutionFilter
<a name="API_StepExecutionFilter"></a>

A filter to limit the amount of step execution information returned by the call.

## Contents
<a name="API_StepExecutionFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-StepExecutionFilter-Key"></a>
One or more keys to limit the results.
Type: String
Valid Values: `StartTimeBefore | StartTimeAfter | StepExecutionStatus | StepExecutionId | StepName | Action | ParentStepExecutionId | ParentStepIteration | ParentStepIteratorValue`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-StepExecutionFilter-Values"></a>
The values of the filter key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## See Also
<a name="API_StepExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StepExecutionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StepExecutionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StepExecutionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
