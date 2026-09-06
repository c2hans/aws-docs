---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketSummary.html
---

# TableBucketSummary
<a name="API_s3Buckets_TableBucketSummary"></a>

Contains details about a table bucket.

## Contents
<a name="API_s3Buckets_TableBucketSummary_Contents"></a>

 ** arn **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-arn"></a>
The Amazon Resource Name (ARN) of the table bucket.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** createdAt **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-createdAt"></a>
The date and time the table bucket was created at.
Type: Timestamp
Required: Yes

 ** name **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-name"></a>
The name of the table bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[0-9a-z-]*`
Required: Yes

 ** ownerAccountId **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-ownerAccountId"></a>
The ID of the account that owns the table bucket.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9].*`
Required: Yes

 ** tableBucketId **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-tableBucketId"></a>
The system-assigned unique identifier for the table bucket.
Type: String
Required: No

 ** type **   <a name="AmazonS3-Type-s3Buckets_TableBucketSummary-type"></a>
The type of the table bucket.
Type: String
Valid Values: `customer | aws`
Required: No

## See Also
<a name="API_s3Buckets_TableBucketSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableBucketSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableBucketSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableBucketSummary)
