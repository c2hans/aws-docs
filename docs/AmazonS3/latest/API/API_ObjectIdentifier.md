---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectIdentifier.html
---

# ObjectIdentifier
<a name="API_ObjectIdentifier"></a>

Object Identifier is unique value to identify objects.

## Contents
<a name="API_ObjectIdentifier_Contents"></a>

 ** Key **   <a name="AmazonS3-Type-ObjectIdentifier-Key"></a>
Key name of the object.
Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see [ XML related object key constraints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints).
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** ETag **   <a name="AmazonS3-Type-ObjectIdentifier-ETag"></a>
An entity tag (ETag) is an identifier assigned by a web server to a specific version of a resource found at a URL. This header field makes the request method conditional on `ETags`.
Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings unique to the object.
Type: String
Required: No

 ** LastModifiedTime **   <a name="AmazonS3-Type-ObjectIdentifier-LastModifiedTime"></a>
If present, the objects are deleted only if its modification times matches the provided `Timestamp`.
This functionality is only supported for directory buckets.
Type: Timestamp
Required: No

 ** Size **   <a name="AmazonS3-Type-ObjectIdentifier-Size"></a>
If present, the objects are deleted only if its size matches the provided size in bytes.
This functionality is only supported for directory buckets.
Type: Long
Required: No

 ** VersionId **   <a name="AmazonS3-Type-ObjectIdentifier-VersionId"></a>
Version ID for the specific version of the object to delete.
This functionality is not supported for directory buckets.
Type: String
Required: No

## See Also
<a name="API_ObjectIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
