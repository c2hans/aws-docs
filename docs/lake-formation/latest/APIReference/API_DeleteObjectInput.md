---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteObjectInput.html
---

# DeleteObjectInput
<a name="API_DeleteObjectInput"></a>

An object to delete from the governed table.

## Contents
<a name="API_DeleteObjectInput_Contents"></a>

 ** Uri **   <a name="lakeformation-Type-DeleteObjectInput-Uri"></a>
The Amazon S3 location of the object to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ETag **   <a name="lakeformation-Type-DeleteObjectInput-ETag"></a>
The Amazon S3 ETag of the object. Returned by `GetTableObjects` for validation and used to identify changes to the underlying data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

 ** PartitionValues **   <a name="lakeformation-Type-DeleteObjectInput-PartitionValues"></a>
A list of partition values for the object. A value must be specified for each partition key associated with the governed table.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_DeleteObjectInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeleteObjectInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeleteObjectInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeleteObjectInput)
