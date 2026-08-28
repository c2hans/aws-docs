---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_VirtualObject.html
---

# VirtualObject
<a name="API_VirtualObject"></a>

An object that defines an Amazon S3 object to be deleted if a transaction cancels, provided that `VirtualPut` was called before writing the object.

## Contents
<a name="API_VirtualObject_Contents"></a>

 ** Uri **   <a name="lakeformation-Type-VirtualObject-Uri"></a>
The path to the Amazon S3 object. Must start with s3://
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ETag **   <a name="lakeformation-Type-VirtualObject-ETag"></a>
The ETag of the Amazon S3 object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## See Also
<a name="API_VirtualObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/VirtualObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/VirtualObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/VirtualObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
