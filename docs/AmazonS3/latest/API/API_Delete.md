---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Delete.html
---

# Delete
<a name="API_Delete"></a>

Container for the objects to delete.

## Contents
<a name="API_Delete_Contents"></a>

 ** Objects **   <a name="AmazonS3-Type-Delete-Objects"></a>
The object to delete.
 **Directory buckets** - For directory buckets, an object that's composed entirely of whitespace characters is not supported by the `DeleteObjects` API operation. The request will receive a `400 Bad Request` error and none of the objects in the request will be deleted.
Type: Array of [ObjectIdentifier](API_ObjectIdentifier.md) data types
Required: Yes

 ** Quiet **   <a name="AmazonS3-Type-Delete-Quiet"></a>
Element to enable quiet mode for the request. When you add this element, you must set its value to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_Delete_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Delete)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Delete)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Delete)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
