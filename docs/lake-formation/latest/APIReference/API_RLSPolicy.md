---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RLSPolicy.html
---

# RLSPolicy
<a name="API_RLSPolicy"></a>

A structure that describes a row-level security policy, including the columns its filter expression references and the filter expression itself.

## Contents
<a name="API_RLSPolicy_Contents"></a>

 ** AttachmentColumns **   <a name="lakeformation-Type-RLSPolicy-AttachmentColumns"></a>
The list of columns that the filter expression references.
Type: Array of [Column](API_Column.md) objects
Required: No

 ** CatalogId **   <a name="lakeformation-Type-RLSPolicy-CatalogId"></a>
The identifier for the Data Catalog that contains the policy. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** FilterExpression **   <a name="lakeformation-Type-RLSPolicy-FilterExpression"></a>
The filter predicate, written in a SQL-like syntax, that determines which rows are returned to the principal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Name **   <a name="lakeformation-Type-RLSPolicy-Name"></a>
The name of the row-level security policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_RLSPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RLSPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RLSPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RLSPolicy)
