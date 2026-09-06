---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ConnectionHeaderParameter.html
---

# ConnectionHeaderParameter
<a name="API_ConnectionHeaderParameter"></a>

Additional parameter included in the header. You can include up to 100 additional header parameters per request. An event payload cannot exceed 64 KB.

## Contents
<a name="API_ConnectionHeaderParameter_Contents"></a>

 ** IsValueSecret **   <a name="eventbridge-Type-ConnectionHeaderParameter-IsValueSecret"></a>
Specifies whether the value is a secret.
Type: Boolean
Required: No

 ** Key **   <a name="eventbridge-Type-ConnectionHeaderParameter-Key"></a>
The key for the parameter.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^[!#$%&'*+-.^_`|~0-9a-zA-Z]+$`
Required: No

 ** Value **   <a name="eventbridge-Type-ConnectionHeaderParameter-Value"></a>
The value associated with the key.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^[ \t]*[\x20-\x7E]+([ \t]+[\x20-\x7E]+)*[ \t]*$`
Required: No

## See Also
<a name="API_ConnectionHeaderParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ConnectionHeaderParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ConnectionHeaderParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ConnectionHeaderParameter)
