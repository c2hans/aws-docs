---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_InstrumentationConfigurationStatusReport.html
---

# InstrumentationConfigurationStatusReport
<a name="API_InstrumentationConfigurationStatusReport"></a>

The status of a single instrumentation configuration reported by an SDK instance.

## Contents
<a name="API_InstrumentationConfigurationStatusReport_Contents"></a>

 ** InstrumentationType **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-InstrumentationType"></a>
The type of instrumentation configuration being reported.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** LocationHash **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-LocationHash"></a>
The stable hash of the instrumentation location that identifies the configuration being reported.
Type: String
Length Constraints: Fixed length of 16.
Required: Yes

 ** SignalType **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-SignalType"></a>
The telemetry signal type for this instrumentation configuration.
Type: String
Valid Values: `SNAPSHOT`
Required: Yes

 ** Status **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-Status"></a>
The status of the instrumentation configuration: `READY`, `ERROR`, `ACTIVE`, or `DISABLED`.
Type: String
Valid Values: `READY | ERROR | ACTIVE | DISABLED`
Required: Yes

 ** Time **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-Time"></a>
The timestamp when the status event occurred.
Type: Timestamp
Required: Yes

 ** ErrorCause **   <a name="applicationsignals-Type-InstrumentationConfigurationStatusReport-ErrorCause"></a>
The error cause when the status is `ERROR`, such as the file or method not being found.
Type: String
Valid Values: `FILE_NOT_FOUND | METHOD_NOT_FOUND | LINE_NOT_EXECUTABLE | OVERLOADED_METHODS | LANGUAGE_MISMATCH | RUNTIME_ERROR`
Required: No

## See Also
<a name="API_InstrumentationConfigurationStatusReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/InstrumentationConfigurationStatusReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/InstrumentationConfigurationStatusReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/InstrumentationConfigurationStatusReport)
