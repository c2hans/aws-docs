---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_AlarmStateChangeDetail.html
---

# AlarmStateChangeDetail
<a name="API_AlarmStateChangeDetail"></a>

Details about a CloudWatch alarm state change observed during a test run.

## Contents
<a name="API_AlarmStateChangeDetail_Contents"></a>

 ** state **   <a name="ngresiliencehub-Type-AlarmStateChangeDetail-state"></a>
The state the alarm transitioned to.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: Yes

 ** previousState **   <a name="ngresiliencehub-Type-AlarmStateChangeDetail-previousState"></a>
The state the alarm transitioned from. Absent on the initial event, which records the alarm's state when collection began.
Type: String
Valid Values: `OK | ALARM | INSUFFICIENT_DATA`
Required: No

 ** reason **   <a name="ngresiliencehub-Type-AlarmStateChangeDetail-reason"></a>
A human-readable explanation of the state change, as reported by CloudWatch.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

## See Also
<a name="API_AlarmStateChangeDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/AlarmStateChangeDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/AlarmStateChangeDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/AlarmStateChangeDetail)
