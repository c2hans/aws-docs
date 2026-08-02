---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_TableObject.html
---

# TableObject
<a name="API_TableObject"></a>

Specifies the details of a governed table.

## Contents
<a name="API_TableObject_Contents"></a>

 ** ETag **   <a name="lakeformation-Type-TableObject-ETag"></a>
The Amazon S3 ETag of the object. Returned by `GetTableObjects` for validation and used to identify changes to the underlying data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

 ** Size **   <a name="lakeformation-Type-TableObject-Size"></a>
The size of the Amazon S3 object in bytes.
Type: Long
Required: No

 ** Uri **   <a name="lakeformation-Type-TableObject-Uri"></a>
The Amazon S3 location of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_TableObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/TableObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/TableObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/TableObject)
