---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTagKeyResource.html
---

# LFTagKeyResource
<a name="API_LFTagKeyResource"></a>

A structure containing an LF-tag key and values for a resource.

## Contents
<a name="API_LFTagKeyResource_Contents"></a>

 ** TagKey **   <a name="lakeformation-Type-LFTagKeyResource-TagKey"></a>
The key-name for the LF-tag.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TagValues **   <a name="lakeformation-Type-LFTagKeyResource-TagValues"></a>
A list of possible values an attribute can take.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:\*\/=+\-@%]*)$`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-LFTagKeyResource-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your AWS Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_LFTagKeyResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTagKeyResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTagKeyResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTagKeyResource)
