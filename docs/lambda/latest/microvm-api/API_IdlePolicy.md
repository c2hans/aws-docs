---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_IdlePolicy.html
---

# IdlePolicy
<a name="API_IdlePolicy"></a>

Configuration that controls MicroVM auto-suspend and auto-resume behavior. Idle time is measured by inbound traffic through the MicroVM proxy endpoint — if no requests arrive within the configured duration, the MicroVM is suspended.

## Contents
<a name="API_IdlePolicy_Contents"></a>

 ** autoResumeEnabled **   <a name="lambdamicrovm-Type-IdlePolicy-autoResumeEnabled"></a>
Indicates whether the MicroVM automatically resumes when it receives a request while suspended.
Type: Boolean
Required: Yes

 ** maxIdleDurationSeconds **   <a name="lambdamicrovm-Type-IdlePolicy-maxIdleDurationSeconds"></a>
The maximum time in seconds that a MicroVM can remain idle before it is automatically suspended.
Type: Integer
Valid Range: Minimum value of 60.
Required: Yes

 ** suspendedDurationSeconds **   <a name="lambdamicrovm-Type-IdlePolicy-suspendedDurationSeconds"></a>
The maximum time in seconds that a MicroVM can remain suspended before it is automatically terminated.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_IdlePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/IdlePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/IdlePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/IdlePolicy)
