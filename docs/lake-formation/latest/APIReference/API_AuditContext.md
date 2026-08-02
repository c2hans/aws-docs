---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AuditContext.html
---

# AuditContext
<a name="API_AuditContext"></a>

A structure used to include auditing information on the privileged API.

## Contents
<a name="API_AuditContext_Contents"></a>

 ** AdditionalAuditContext **   <a name="lakeformation-Type-AuditContext-AdditionalAuditContext"></a>
The filter engine can populate the 'AdditionalAuditContext' information with the request ID for you to track. This information will be displayed in CloudTrail log in your account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_AuditContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/AuditContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/AuditContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/AuditContext)
