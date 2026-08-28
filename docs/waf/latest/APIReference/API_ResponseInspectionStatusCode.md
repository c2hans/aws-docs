---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ResponseInspectionStatusCode.html
---

# ResponseInspectionStatusCode
<a name="API_ResponseInspectionStatusCode"></a>

Configures inspection of the response status code. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Contents
<a name="API_ResponseInspectionStatusCode_Contents"></a>

 ** FailureCodes **   <a name="WAF-Type-ResponseInspectionStatusCode-FailureCodes"></a>
Status codes in the response that indicate a failed login or account creation attempt. To be counted as a failure, the response status code must match one of these. Each code must be unique among the success and failure status codes.
JSON example: `"FailureCodes": [ 400, 404 ]`
Type: Array of integers
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

 ** SuccessCodes **   <a name="WAF-Type-ResponseInspectionStatusCode-SuccessCodes"></a>
Status codes in the response that indicate a successful login or account creation attempt. To be counted as a success, the response status code must match one of these. Each code must be unique among the success and failure status codes.
JSON example: `"SuccessCodes": [ 200, 201 ]`
Type: Array of integers
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Range: Minimum value of 0. Maximum value of 999.
Required: Yes

## See Also
<a name="API_ResponseInspectionStatusCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ResponseInspectionStatusCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ResponseInspectionStatusCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ResponseInspectionStatusCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
