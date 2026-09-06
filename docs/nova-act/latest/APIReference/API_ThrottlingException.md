---
source_url: https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ThrottlingException.html
---

# ThrottlingException
<a name="API_ThrottlingException"></a>

The request was throttled due to too many requests. Please try again later.

HTTP Status Code returned: 429

## Contents
<a name="API_ThrottlingException_Contents"></a>

 ** message **   <a name="novaact-Type-ThrottlingException-message"></a>
The request was denied due to request throttling.
Type: String
Pattern: `[\s\S]+`
Required: Yes

 ** quotaCode **   <a name="novaact-Type-ThrottlingException-quotaCode"></a>
The quota code related to the throttling.
Type: String
Pattern: `[\s\S]+`
Required: No

 ** Retry-After **   <a name="novaact-Type-ThrottlingException-retryAfterSeconds"></a>
The number of seconds to wait before retrying the throttled request.
Type: Integer
Required: No

 ** serviceCode **   <a name="novaact-Type-ThrottlingException-serviceCode"></a>
The service code where throttling occurred.
Type: String
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_ThrottlingException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/nova-act-2025-08-22/ThrottlingException)
