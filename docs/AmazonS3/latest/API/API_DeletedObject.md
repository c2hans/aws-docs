---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletedObject.html
---

# DeletedObject
<a name="API_DeletedObject"></a>

Information about the deleted object.

## Contents
<a name="API_DeletedObject_Contents"></a>

 ** DeleteMarker **   <a name="AmazonS3-Type-DeletedObject-DeleteMarker"></a>
Indicates whether the specified object version that was permanently deleted was (true) or was not (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not (false) the current version of the object is a delete marker. To learn more about delete markers, see [Working with delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).
This functionality is not supported for directory buckets.
Type: Boolean
Required: No

 ** DeleteMarkerVersionId **   <a name="AmazonS3-Type-DeletedObject-DeleteMarkerVersionId"></a>
The version ID of the delete marker created as a result of the DELETE operation. If you delete a specific object version, the value returned by this header is the version ID of the object version deleted.
This functionality is not supported for directory buckets.
Type: String
Required: No

 ** Key **   <a name="AmazonS3-Type-DeletedObject-Key"></a>
The name of the deleted object.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** VersionId **   <a name="AmazonS3-Type-DeletedObject-VersionId"></a>
The version ID of the deleted object.
This functionality is not supported for directory buckets.
Type: String
Required: No

## See Also
<a name="API_DeletedObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/DeletedObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/DeletedObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/DeletedObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
