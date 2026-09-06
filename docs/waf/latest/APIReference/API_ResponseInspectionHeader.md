---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ResponseInspectionHeader.html
---

# ResponseInspectionHeader
<a name="API_ResponseInspectionHeader"></a>

Configures inspection of the response header. This is part of the `ResponseInspection` configuration for `AWSManagedRulesATPRuleSet` and `AWSManagedRulesACFPRuleSet`.

**Note**
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.

## Contents
<a name="API_ResponseInspectionHeader_Contents"></a>

 ** FailureValues **   <a name="WAF-Type-ResponseInspectionHeader-FailureValues"></a>
Values in the response header with the specified name that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON examples: `"FailureValues": [ "LoginFailed", "Failed login" ]` and `"FailureValues": [ "AccountCreationFailed" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-ResponseInspectionHeader-Name"></a>
The name of the header to match against. The name must be an exact match, including case.
JSON example: `"Name": [ "RequestResult" ]`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*\S.*`
Required: Yes

 ** SuccessValues **   <a name="WAF-Type-ResponseInspectionHeader-SuccessValues"></a>
Values in the response header with the specified name that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values.
JSON examples: `"SuccessValues": [ "LoginPassed", "Successful login" ]` and `"SuccessValues": [ "AccountCreated", "Successful account creation" ]`
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ResponseInspectionHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ResponseInspectionHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ResponseInspectionHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ResponseInspectionHeader)
