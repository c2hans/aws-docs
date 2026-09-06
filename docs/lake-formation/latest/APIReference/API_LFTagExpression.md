---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTagExpression.html
---

# LFTagExpression
<a name="API_LFTagExpression"></a>

A structure consists LF-Tag expression name and catalog ID.

## Contents
<a name="API_LFTagExpression_Contents"></a>

 ** CatalogId **   <a name="lakeformation-Type-LFTagExpression-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Description **   <a name="lakeformation-Type-LFTagExpression-Description"></a>
A structure that contains information about the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Expression **   <a name="lakeformation-Type-LFTagExpression-Expression"></a>
A logical expression composed of one or more LF-Tags.
Type: Array of [LFTag](API_LFTag.md) objects
Required: No

 ** Name **   <a name="lakeformation-Type-LFTagExpression-Name"></a>
The name for saved the LF-Tag expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_LFTagExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTagExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTagExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTagExpression)
