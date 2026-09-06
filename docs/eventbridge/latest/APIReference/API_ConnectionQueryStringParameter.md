---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionQueryStringParameter.html
---

# ConnectionQueryStringParameter
<a name="API_ConnectionQueryStringParameter"></a>

Any additional query string parameter for the connection. You can include up to 100 additional query string parameters per request. Each additional parameter counts towards the event payload size, which cannot exceed 64 KB.

## Contents
<a name="API_ConnectionQueryStringParameter_Contents"></a>

 ** IsValueSecret **   <a name="eventbridge-Type-ConnectionQueryStringParameter-IsValueSecret"></a>
Specifies whether the value is secret.
Type: Boolean
Required: No

 ** Key **   <a name="eventbridge-Type-ConnectionQueryStringParameter-Key"></a>
The key for a query string parameter.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[^\x00-\x1F\x7F]+`
Required: No

 ** Value **   <a name="eventbridge-Type-ConnectionQueryStringParameter-Value"></a>
The value associated with the key for the query string parameter.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[^\x00-\x09\x0B\x0C\x0E-\x1F\x7F]+`
Required: No

## See Also
<a name="API_ConnectionQueryStringParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionQueryStringParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionQueryStringParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionQueryStringParameter)
