---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_CaptchaResponse.html
---

# CaptchaResponse
<a name="API_CaptchaResponse"></a>

The result from the inspection of the web request for a valid `CAPTCHA` token.

## Contents
<a name="API_CaptchaResponse_Contents"></a>

 ** FailureReason **   <a name="WAF-Type-CaptchaResponse-FailureReason"></a>
The reason for failure, populated when the evaluation of the token fails.
Type: String
Valid Values: `TOKEN_MISSING | TOKEN_EXPIRED | TOKEN_INVALID | TOKEN_DOMAIN_MISMATCH`
Required: No

 ** ResponseCode **   <a name="WAF-Type-CaptchaResponse-ResponseCode"></a>
The HTTP response code indicating the status of the `CAPTCHA` token in the web request. If the token is missing, invalid, or expired, this code is `405 Method Not Allowed`.
Type: Integer
Required: No

 ** SolveTimestamp **   <a name="WAF-Type-CaptchaResponse-SolveTimestamp"></a>
The time that the `CAPTCHA` was last solved for the supplied token.
Type: Long
Required: No

## See Also
<a name="API_CaptchaResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/CaptchaResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/CaptchaResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/CaptchaResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
