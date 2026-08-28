---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Describes an Amazon S3 location that will receive the results of the restore request.

## Contents
<a name="API_S3Location_Contents"></a>

 ** BucketName **   <a name="AmazonS3-Type-S3Location-BucketName"></a>
The name of the bucket where the restore results will be placed.
Type: String
Required: Yes

 ** Prefix **   <a name="AmazonS3-Type-S3Location-Prefix"></a>
The prefix that is prepended to the restore results for this request.
Type: String
Required: Yes

 ** AccessControlList **   <a name="AmazonS3-Type-S3Location-AccessControlList"></a>
A list of grants that control access to the staged results.
Type: Array of [Grant](API_Grant.md) data types
Required: No

 ** CannedACL **   <a name="AmazonS3-Type-S3Location-CannedACL"></a>
The canned ACL to apply to the restore results.
Type: String
Valid Values: `private | public-read | public-read-write | authenticated-read | aws-exec-read | bucket-owner-read | bucket-owner-full-control`
Required: No

 ** Encryption **   <a name="AmazonS3-Type-S3Location-Encryption"></a>
Contains the type of server-side encryption used.
Type: [Encryption](API_Encryption.md) data type
Required: No

 ** StorageClass **   <a name="AmazonS3-Type-S3Location-StorageClass"></a>
The class of storage used to store the restore results.
Type: String
Valid Values: `STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | OUTPOSTS | GLACIER_IR | SNOW | EXPRESS_ONEZONE | FSX_OPENZFS | FSX_ONTAP`
Required: No

 ** Tagging **   <a name="AmazonS3-Type-S3Location-Tagging"></a>
The tag-set that is applied to the restore results.
Type: [Tagging](API_Tagging.md) data type
Required: No

 ** UserMetadata **   <a name="AmazonS3-Type-S3Location-UserMetadata"></a>
A list of metadata to store with the restore results in S3.
Type: Array of [MetadataEntry](API_MetadataEntry.md) data types
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/S3Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
