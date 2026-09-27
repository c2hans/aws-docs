---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_StepFunctionsParameters.html
---

# StepFunctionsParameters
<a name="API_StepFunctionsParameters"></a>

Step Functions invocation parameters for subscribers. Values are forwarded to the Step Functions StartExecution or StartSyncExecution API. Every string member accepts a literal or a JSONata expression (e.g. "{% $events.Data.executionName %}").

## Contents
<a name="API_StepFunctionsParameters_Contents"></a>

 ** InvocationTimeoutSeconds **   <a name="eventbridgev2-Type-StepFunctionsParameters-InvocationTimeoutSeconds"></a>
Timeout in seconds for each invocation of the target (1-30). String-typed (not integer) so the value may be a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** InvocationType **   <a name="eventbridgev2-Type-StepFunctionsParameters-InvocationType"></a>
Selects StartExecution (EVENT) or StartSyncExecution (REQUEST\_RESPONSE) at delivery.
Type: String
Valid Values: `EVENT | REQUEST_RESPONSE`
Required: No

 ** Name **   <a name="eventbridgev2-Type-StepFunctionsParameters-Name"></a>
Name for the execution. Must be unique per account/region/state machine. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** TraceHeader **   <a name="eventbridgev2-Type-StepFunctionsParameters-TraceHeader"></a>
X-Ray trace header for distributed tracing. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_StepFunctionsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/StepFunctionsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/StepFunctionsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/StepFunctionsParameters)
