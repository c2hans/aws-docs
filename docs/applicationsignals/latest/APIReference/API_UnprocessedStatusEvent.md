---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_UnprocessedStatusEvent.html
---

# UnprocessedStatusEvent
<a name="API_UnprocessedStatusEvent"></a>

A status event that could not be processed by the service.

## Contents
<a name="API_UnprocessedStatusEvent_Contents"></a>

 ** FailedReason **   <a name="applicationsignals-Type-UnprocessedStatusEvent-FailedReason"></a>
The reason why this status event could not be processed, such as throttling or validation errors.
Type: String
Valid Values: `THROTTLED | INTERNAL_ERROR | VALIDATION_ERROR`
Required: Yes

 ** InstrumentationType **   <a name="applicationsignals-Type-UnprocessedStatusEvent-InstrumentationType"></a>
The type of instrumentation configuration for the unprocessed status event.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** LocationHash **   <a name="applicationsignals-Type-UnprocessedStatusEvent-LocationHash"></a>
The stable hash of the instrumentation location for the unprocessed event.
Type: String
Length Constraints: Fixed length of 16.
Required: Yes

 ** SignalType **   <a name="applicationsignals-Type-UnprocessedStatusEvent-SignalType"></a>
The telemetry signal type for the unprocessed status event.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** Status **   <a name="applicationsignals-Type-UnprocessedStatusEvent-Status"></a>
The status that failed to be processed.
Type: String
Valid Values: `READY | ERROR | ACTIVE | DISABLED`
Required: Yes

 ** Time **   <a name="applicationsignals-Type-UnprocessedStatusEvent-Time"></a>
The timestamp of the status event that failed to be processed.
Type: Timestamp
Required: Yes

## See Also
<a name="API_UnprocessedStatusEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/UnprocessedStatusEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/UnprocessedStatusEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/UnprocessedStatusEvent)
