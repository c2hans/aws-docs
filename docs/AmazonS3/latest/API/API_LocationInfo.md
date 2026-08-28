---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_LocationInfo.html
---

# LocationInfo
<a name="API_LocationInfo"></a>

Specifies the location where the bucket will be created.

For directory buckets, the location type is Availability Zone or Local Zone. For more information about directory buckets, see [Working with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*.

**Note**
This functionality is only supported by directory buckets.

## Contents
<a name="API_LocationInfo_Contents"></a>

 ** Name **   <a name="AmazonS3-Type-LocationInfo-Name"></a>
The name of the location where the bucket will be created.
For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is `usw2-az1`.
Type: String
Required: No

 ** Type **   <a name="AmazonS3-Type-LocationInfo-Type"></a>
The type of location where the bucket will be created.
Type: String
Valid Values: `AvailabilityZone | LocalZone`
Required: No

## See Also
<a name="API_LocationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LocationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LocationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LocationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
