---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ChallengeResponse.html
---

# ChallengeResponse
<a name="API_ChallengeResponse"></a>

The result from the inspection of the web request for a valid challenge token.

## Contents
<a name="API_ChallengeResponse_Contents"></a>

 ** FailureReason **   <a name="WAF-Type-ChallengeResponse-FailureReason"></a>
The reason for failure, populated when the evaluation of the token fails.
Type: String
Valid Values: `TOKEN_MISSING | TOKEN_EXPIRED | TOKEN_INVALID | TOKEN_DOMAIN_MISMATCH`
Required: No

 ** ResponseCode **   <a name="WAF-Type-ChallengeResponse-ResponseCode"></a>
The HTTP response code indicating the status of the challenge token in the web request. If the token is missing, invalid, or expired, this code is `202 Request Accepted`.
Type: Integer
Required: No

 ** SolveTimestamp **   <a name="WAF-Type-ChallengeResponse-SolveTimestamp"></a>
The time that the challenge was last solved for the supplied token.
Type: Long
Required: No

## See Also
<a name="API_ChallengeResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ChallengeResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ChallengeResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ChallengeResponse)
