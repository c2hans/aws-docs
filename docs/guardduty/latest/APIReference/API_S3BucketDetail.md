---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_S3BucketDetail.html
---

# S3BucketDetail
<a name="API_S3BucketDetail"></a>

Contains information on the S3 bucket.

## Contents
<a name="API_S3BucketDetail_Contents"></a>

 ** arn **   <a name="guardduty-Type-S3BucketDetail-arn"></a>
The Amazon Resource Name (ARN) of the S3 bucket.
Type: String
Required: No

 ** createdAt **   <a name="guardduty-Type-S3BucketDetail-createdAt"></a>
The date and time the bucket was created at.
Type: Timestamp
Required: No

 ** defaultServerSideEncryption **   <a name="guardduty-Type-S3BucketDetail-defaultServerSideEncryption"></a>
Describes the server side encryption method used in the S3 bucket.
Type: [DefaultServerSideEncryption](API_DefaultServerSideEncryption.md) object
Required: No

 ** name **   <a name="guardduty-Type-S3BucketDetail-name"></a>
The name of the S3 bucket.
Type: String
Required: No

 ** owner **   <a name="guardduty-Type-S3BucketDetail-owner"></a>
The owner of the S3 bucket.
Type: [Owner](API_Owner.md) object
Required: No

 ** publicAccess **   <a name="guardduty-Type-S3BucketDetail-publicAccess"></a>
Describes the public access policies that apply to the S3 bucket.
Type: [PublicAccess](API_PublicAccess.md) object
Required: No

 ** s3ObjectDetails **   <a name="guardduty-Type-S3BucketDetail-s3ObjectDetails"></a>
Information about the S3 object that was scanned.
Type: Array of [S3ObjectDetail](API_S3ObjectDetail.md) objects
Required: No

 ** tags **   <a name="guardduty-Type-S3BucketDetail-tags"></a>
All tags attached to the S3 bucket
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** type **   <a name="guardduty-Type-S3BucketDetail-type"></a>
Describes whether the bucket is a source or destination bucket.
Type: String
Required: No

## See Also
<a name="API_S3BucketDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/S3BucketDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/S3BucketDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/S3BucketDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
