---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-scheduling_TimeOffValidationResult.html
---

# TimeOffValidationResult
<a name="API_connect-scheduling_TimeOffValidationResult"></a>

A warning or failure produced while processing the time off request.

## Contents
<a name="API_connect-scheduling_TimeOffValidationResult_Contents"></a>

 ** Code **   <a name="connect-Type-connect-scheduling_TimeOffValidationResult-Code"></a>
The specific reason for the validation result. New values may be added, so treat an unrecognized value as a generic failure of the reported severity.
+  `INSUFFICIENT_USER_TIME_OFF_BALANCE`: the user's time off balance for the activity is less than the time this request deducts. Connect Customer deducts only working time in the window. For details, see [How the system calculates time off deductions](https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html#how-system-calculates-time-off-deductions) in the *Connect Customer Administrator Guide*.
+  `INSUFFICIENT_GROUP_TIME_OFF_ALLOWANCE`: the time off allowance of the user's forecast group or demand group for the activity is too low for this request.
+  `INSUFFICIENT_STAFFING_GROUP_TIME_OFF_ALLOWANCE`: the daily time off allowance of the user's staffing group for the activity is too low for this request.
+  `CONFLICTING_TIME_OFF_REQUEST`: the request overlaps another time off request for the user that is `APPROVED` or being approved. Requests in `AWAITING_APPROVAL` don't count. For `CreateTimeOff` with `AUTOMATIC`, overlapping overtime and voluntary time off also count.
Type: String
Valid Values: `INSUFFICIENT_USER_TIME_OFF_BALANCE | INSUFFICIENT_GROUP_TIME_OFF_ALLOWANCE | INSUFFICIENT_STAFFING_GROUP_TIME_OFF_ALLOWANCE | CONFLICTING_TIME_OFF_REQUEST`
Required: Yes

 ** Severity **   <a name="connect-Type-connect-scheduling_TimeOffValidationResult-Severity"></a>
The severity of the validation result. `WARNING` is a breach of the configured rules that is not enough to reject the request, either because of the rules configuration or because the caller sent `RuleFailureAction` `OVERRIDE`. `ERROR` is a reason the request was rejected.
Type: String
Valid Values: `WARNING | ERROR`
Required: Yes

## See Also
<a name="API_connect-scheduling_TimeOffValidationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectscheduling-2026-07-16/TimeOffValidationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectscheduling-2026-07-16/TimeOffValidationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectscheduling-2026-07-16/TimeOffValidationResult)
