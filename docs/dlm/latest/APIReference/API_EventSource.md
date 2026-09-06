---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_EventSource.html
---

# EventSource
<a name="API_EventSource"></a>

 **[Event-based policies only]** Specifies an event that activates an event-based policy.

## Contents
<a name="API_EventSource_Contents"></a>

 ** Type **   <a name="dlm-Type-EventSource-Type"></a>
The source of the event. Currently only managed Amazon EventBridge (formerly known as Amazon CloudWatch) events are supported.
Type: String
Valid Values: `MANAGED_CWE`
Required: Yes

 ** Parameters **   <a name="dlm-Type-EventSource-Parameters"></a>
Information about the event.
Type: [EventParameters](API_EventParameters.md) object
Required: No

## See Also
<a name="API_EventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/EventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/EventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/EventSource)
