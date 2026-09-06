---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_RetrievedTrace.html
---

# RetrievedTrace
<a name="API_RetrievedTrace"></a>

 Retrieved collection of spans with matching trace IDs.

## Contents
<a name="API_RetrievedTrace_Contents"></a>

 ** Duration **   <a name="xray-Type-RetrievedTrace-Duration"></a>
 The length of time in seconds between the start time of the root span and the end time of the last span that completed.
Type: Double
Required: No

 ** Id **   <a name="xray-Type-RetrievedTrace-Id"></a>
 The unique identifier for the span.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: No

 ** Spans **   <a name="xray-Type-RetrievedTrace-Spans"></a>
 Spans that comprise the trace.
Type: Array of [Span](API_Span.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_RetrievedTrace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/RetrievedTrace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/RetrievedTrace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/RetrievedTrace)
