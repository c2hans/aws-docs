---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_BucketInfo.html
---

# BucketInfo
<a name="API_BucketInfo"></a>

Specifies the information about the bucket that will be created. For more information about directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*.

**Note**
This functionality is only supported by directory buckets.

## Contents
<a name="API_BucketInfo_Contents"></a>

 ** DataRedundancy **   <a name="AmazonS3-Type-BucketInfo-DataRedundancy"></a>
The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.
Type: String
Valid Values: `SingleAvailabilityZone | SingleLocalZone`
Required: No

 ** Type **   <a name="AmazonS3-Type-BucketInfo-Type"></a>
The type of bucket.
Type: String
Valid Values: `Directory`
Required: No

## See Also
<a name="API_BucketInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/BucketInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/BucketInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/BucketInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
