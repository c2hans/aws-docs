---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_InstrumentationStatusEvent.html
---

# InstrumentationStatusEvent
<a name="API_InstrumentationStatusEvent"></a>

A status event for an instrumentation configuration returned by `GetInstrumentationConfigurationStatus`. Events include the timestamp and, for errors, an error cause.

## Contents
<a name="API_InstrumentationStatusEvent_Contents"></a>

 ** Time **   <a name="applicationsignals-Type-InstrumentationStatusEvent-Time"></a>
The time when the status was reported, rounded to the nearest minute.
Type: Timestamp
Required: Yes

 ** ErrorCause **   <a name="applicationsignals-Type-InstrumentationStatusEvent-ErrorCause"></a>
The error cause when the status is `ERROR`.
Type: String
Valid Values: `FILE_NOT_FOUND | METHOD_NOT_FOUND | LINE_NOT_EXECUTABLE | OVERLOADED_METHODS | LANGUAGE_MISMATCH | RUNTIME_ERROR`
Required: No

## See Also
<a name="API_InstrumentationStatusEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/InstrumentationStatusEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/InstrumentationStatusEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/InstrumentationStatusEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
