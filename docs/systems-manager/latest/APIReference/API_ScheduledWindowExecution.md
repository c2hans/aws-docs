---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ScheduledWindowExecution.html
---

# ScheduledWindowExecution
<a name="API_ScheduledWindowExecution"></a>

Information about a scheduled execution for a maintenance window.

## Contents
<a name="API_ScheduledWindowExecution_Contents"></a>

 ** ExecutionTime **   <a name="systemsmanager-Type-ScheduledWindowExecution-ExecutionTime"></a>
The time, in ISO-8601 Extended format, that the maintenance window is scheduled to be run.
Type: String
Required: No

 ** Name **   <a name="systemsmanager-Type-ScheduledWindowExecution-Name"></a>
The name of the maintenance window to be run.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** WindowId **   <a name="systemsmanager-Type-ScheduledWindowExecution-WindowId"></a>
The ID of the maintenance window to be run.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

## See Also
<a name="API_ScheduledWindowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ScheduledWindowExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ScheduledWindowExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ScheduledWindowExecution)
