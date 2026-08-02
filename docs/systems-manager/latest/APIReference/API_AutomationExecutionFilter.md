---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AutomationExecutionFilter.html
---

# AutomationExecutionFilter
<a name="API_AutomationExecutionFilter"></a>

A filter used to match specific automation executions. This is used to limit the scope of Automation execution information returned.

## Contents
<a name="API_AutomationExecutionFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-AutomationExecutionFilter-Key"></a>
One or more keys to limit the results.
Type: String
Valid Values: `DocumentNamePrefix | ExecutionStatus | ExecutionId | ParentExecutionId | CurrentAction | StartTimeBefore | StartTimeAfter | AutomationType | TagKey | TargetResourceGroup | AutomationSubtype | OpsItemId`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-AutomationExecutionFilter-Values"></a>
The values used to limit the execution information associated with the filter's key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: Yes

## See Also
<a name="API_AutomationExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AutomationExecutionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AutomationExecutionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AutomationExecutionFilter)
