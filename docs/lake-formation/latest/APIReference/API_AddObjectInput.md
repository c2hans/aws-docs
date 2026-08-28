---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AddObjectInput.html
---

# AddObjectInput
<a name="API_AddObjectInput"></a>

A new object to add to the governed table.

## Contents
<a name="API_AddObjectInput_Contents"></a>

 ** ETag **   <a name="lakeformation-Type-AddObjectInput-ETag"></a>
The Amazon S3 ETag of the object. Returned by `GetTableObjects` for validation and used to identify changes to the underlying data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: Yes

 ** Size **   <a name="lakeformation-Type-AddObjectInput-Size"></a>
The size of the Amazon S3 object in bytes.
Type: Long
Required: Yes

 ** Uri **   <a name="lakeformation-Type-AddObjectInput-Uri"></a>
The Amazon S3 location of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** PartitionValues **   <a name="lakeformation-Type-AddObjectInput-PartitionValues"></a>
A list of partition values for the object. A value must be specified for each partition key associated with the table.
The supported data types are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss"), string and decimal.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_AddObjectInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/AddObjectInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/AddObjectInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/AddObjectInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
