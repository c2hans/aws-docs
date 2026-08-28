---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_S3Resource.html
---

# S3Resource
<a name="API_S3Resource"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Each `S3Resource` object represents an Amazon S3 bucket that your transferred data will be exported from or imported into. For export jobs, this object can have an optional `KeyRange` value. The length of the range is defined at job creation, and has either an inclusive `BeginMarker`, an inclusive `EndMarker`, or both. Ranges are UTF-8 binary sorted.

## Contents
<a name="API_S3Resource_Contents"></a>

 ** BucketArn **   <a name="Snowball-Type-S3Resource-BucketArn"></a>
The Amazon Resource Name (ARN) of an Amazon S3 bucket.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `arn:aws.*:*`
Required: No

 ** KeyRange **   <a name="Snowball-Type-S3Resource-KeyRange"></a>
For export jobs, you can provide an optional `KeyRange` within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive `BeginMarker`, an inclusive `EndMarker`, or both. Ranges are UTF-8 binary sorted.
Type: [KeyRange](API_KeyRange.md) object
Required: No

 ** TargetOnDeviceServices **   <a name="Snowball-Type-S3Resource-TargetOnDeviceServices"></a>
Specifies the service or services on the Snowball Edge device that your transferred data will be exported from or imported into. AWS Snowball Edge supports Amazon S3 and NFS (Network File System).
Type: Array of [TargetOnDeviceService](API_TargetOnDeviceService.md) objects
Required: No

## See Also
<a name="API_S3Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/S3Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/S3Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/S3Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
