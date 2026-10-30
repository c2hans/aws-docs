---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RLSPolicyResource.html
---

# RLSPolicyResource
<a name="API_RLSPolicyResource"></a>

A structure that identifies a row-level security policy as a resource, used when granting permissions on the policy.

## Contents
<a name="API_RLSPolicyResource_Contents"></a>

 ** Name **   <a name="lakeformation-Type-RLSPolicyResource-Name"></a>
The name of the row-level security policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-RLSPolicyResource-CatalogId"></a>
The identifier for the Data Catalog that contains the policy. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_RLSPolicyResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RLSPolicyResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RLSPolicyResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RLSPolicyResource)
