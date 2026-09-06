---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ResponseInspectionBodyContains.html
---

# ResponseInspectionBodyContains
<a name="API_ResponseInspectionBodyContains"></a>

Configures inspection of the response body. AWS WAF can inspect the first 65,536 bytes (64 KB) of the response body. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Contents
<a name="API_ResponseInspectionBodyContains_Contents"></a>

 ** FailureStrings **   <a name="WAF-Type-ResponseInspectionBodyContains-FailureStrings"></a>
Strings in the body of the response that indicate a failed login or account creation attempt. To be counted as a failure, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings.
JSON example: `"FailureStrings": [ "Request failed" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

 ** SuccessStrings **   <a name="WAF-Type-ResponseInspectionBodyContains-SuccessStrings"></a>
Strings in the body of the response that indicate a successful login or account creation attempt. To be counted as a success, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings.
JSON examples: `"SuccessStrings": [ "Login successful" ]` and `"SuccessStrings": [ "Account creation successful", "Welcome to our site!" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ResponseInspectionBodyContains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ResponseInspectionBodyContains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ResponseInspectionBodyContains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ResponseInspectionBodyContains)
