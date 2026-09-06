---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_RateLimitError.html
---

# RateLimitError
<a name="API_RateLimitError"></a>

The request was throttled because too many requests were sent in a short period of time. Wait a moment and retry the request. Consider implementing exponential backoff in your application.

HTTP Status Code returned: 429

## Contents
<a name="API_RateLimitError_Contents"></a>

 ** message **   <a name="wickr-Type-RateLimitError-message"></a>
A message indicating that the rate limit was exceeded and suggesting when to retry.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_RateLimitError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/RateLimitError)
