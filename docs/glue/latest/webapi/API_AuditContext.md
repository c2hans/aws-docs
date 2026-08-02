---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html
---

# AuditContext
<a name="API_AuditContext"></a>

A structure containing the Lake Formation audit context.

## Contents
<a name="API_AuditContext_Contents"></a>

 ** AdditionalAuditContext **   <a name="Glue-Type-AuditContext-AdditionalAuditContext"></a>
A string containing the additional audit context information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** AllColumnsRequested **   <a name="Glue-Type-AuditContext-AllColumnsRequested"></a>
All columns request for audit.
Type: Boolean
Required: No

 ** RequestedColumns **   <a name="Glue-Type-AuditContext-RequestedColumns"></a>
The requested columns for audit.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_AuditContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AuditContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AuditContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AuditContext)
