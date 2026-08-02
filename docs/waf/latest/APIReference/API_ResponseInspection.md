---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ResponseInspection.html
---

# ResponseInspection
<a name="API_ResponseInspection"></a>

The criteria for inspecting responses to login requests and account creation requests, used by the ATP and ACFP rule groups to track login and account creation success and failure rates.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

The rule groups evaluates the responses that your protected resources send back to client login and account creation attempts, keeping count of successful and failed attempts from each IP address and client session. Using this information, the rule group labels and mitigates requests from client sessions and IP addresses with too much suspicious activity in a short amount of time.

This is part of the `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet` configurations in `ManagedRuleGroupConfig`.

Enable response inspection by configuring exactly one component of the response to inspect, for example, `Header` or `StatusCode`. You can't configure more than one component for inspection. If you don't configure any of the response inspection options, response inspection is disabled.

## Contents
<a name="API_ResponseInspection_Contents"></a>

 ** BodyContains **   <a name="WAF-Type-ResponseInspection-BodyContains"></a>
Configures inspection of the response body for success and failure indicators. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response body.
Type: [ResponseInspectionBodyContains](API_ResponseInspectionBodyContains.md) object
Required: No

 ** Header **   <a name="WAF-Type-ResponseInspection-Header"></a>
Configures inspection of the response header for success and failure indicators.
Type: [ResponseInspectionHeader](API_ResponseInspectionHeader.md) object
Required: No

 ** Json **   <a name="WAF-Type-ResponseInspection-Json"></a>
Configures inspection of the response JSON for success and failure indicators. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response JSON.
Type: [ResponseInspectionJson](API_ResponseInspectionJson.md) object
Required: No

 ** StatusCode **   <a name="WAF-Type-ResponseInspection-StatusCode"></a>
Configures inspection of the response status code for success and failure indicators.
Type: [ResponseInspectionStatusCode](API_ResponseInspectionStatusCode.md) object
Required: No

## See Also
<a name="API_ResponseInspection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ResponseInspection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ResponseInspection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ResponseInspection)
