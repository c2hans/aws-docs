---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTagExpressionResource.html
---

# LFTagExpressionResource
<a name="API_LFTagExpressionResource"></a>

A structure containing a LF-Tag expression (keys and values).

## Contents
<a name="API_LFTagExpressionResource_Contents"></a>

 ** Name **   <a name="lakeformation-Type-LFTagExpressionResource-Name"></a>
The name of the LF-Tag expression to grant permissions on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-LFTagExpressionResource-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_LFTagExpressionResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTagExpressionResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTagExpressionResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTagExpressionResource)
