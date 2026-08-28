---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ResponseInspectionJson.html
---

# ResponseInspectionJson
<a name="API_ResponseInspectionJson"></a>

Configures inspection of the response JSON. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response JSON. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Contents
<a name="API_ResponseInspectionJson_Contents"></a>

 ** FailureValues **   <a name="WAF-Type-ResponseInspectionJson-FailureValues"></a>
Values for the specified identifier in the response JSON that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON example: `"FailureValues": [ "False", "Failed" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

 ** Identifier **   <a name="WAF-Type-ResponseInspectionJson-Identifier"></a>
The identifier for the value to match against in the JSON. The identifier must be an exact match, including case.
JSON examples: `"Identifier": [ "/login/success" ]` and `"Identifier": [ "/sign-up/success" ]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: Yes

 ** SuccessValues **   <a name="WAF-Type-ResponseInspectionJson-SuccessValues"></a>
Values for the specified identifier in the response JSON that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON example: `"SuccessValues": [ "True", "Succeeded" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ResponseInspectionJson_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ResponseInspectionJson)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ResponseInspectionJson)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ResponseInspectionJson)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
