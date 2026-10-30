---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ScheduleActionError.html
---

# ScheduleActionError
<a name="API_ScheduleActionError"></a>

Describes the cause of a schedule action failure, including the failure type and a description of what went wrong.

## Contents
<a name="API_ScheduleActionError_Contents"></a>

 ** errorCode **   <a name="elementalinference-Type-ScheduleActionError-errorCode"></a>
The type of failure. Valid values are the following:
INVALID\_ACTION\_TARGET
The action referred to something that didn't exist or wasn't valid at the scheduled time, for example an output that you deleted.
INTERNAL\_ERROR
An unexpected error prevented the action from completing.
Type: String
Valid Values: `INVALID_ACTION_TARGET | INTERNAL_ERROR`
Required: Yes

 ** errorMessage **   <a name="elementalinference-Type-ScheduleActionError-errorMessage"></a>
A description of the failure.
Type: String
Required: Yes

## See Also
<a name="API_ScheduleActionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ScheduleActionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ScheduleActionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ScheduleActionError)
