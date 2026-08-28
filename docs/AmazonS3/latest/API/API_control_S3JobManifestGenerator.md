---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3JobManifestGenerator.html
---

# S3JobManifestGenerator
<a name="API_control_S3JobManifestGenerator"></a>

The container for the service that will create the S3 manifest.

## Contents
<a name="API_control_S3JobManifestGenerator_Contents"></a>

 ** EnableManifestOutput **   <a name="AmazonS3-Type-control_S3JobManifestGenerator-EnableManifestOutput"></a>
Determines whether or not to write the job's generated manifest to a bucket.
Type: Boolean
Required: Yes

 ** SourceBucket **   <a name="AmazonS3-Type-control_S3JobManifestGenerator-SourceBucket"></a>
The ARN of the source bucket used by the ManifestGenerator.
 **Directory buckets** - Directory buckets aren't supported as the source buckets used by `S3JobManifestGenerator` to generate the job manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[^:]+:s3:.*`
Required: Yes

 ** ExpectedBucketOwner **   <a name="AmazonS3-Type-control_S3JobManifestGenerator-ExpectedBucketOwner"></a>
The AWS account ID that owns the source bucket specified in `SourceBucket`. If provided, the manifest source bucket owner's AWS account ID must match this value, else the job fails.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: No

 ** Filter **   <a name="AmazonS3-Type-control_S3JobManifestGenerator-Filter"></a>
Specifies rules the S3JobManifestGenerator should use to decide whether an object in the source bucket should or should not be included in the generated job manifest.
Type: [JobManifestGeneratorFilter](API_control_JobManifestGeneratorFilter.md) data type
Required: No

 ** ManifestOutputLocation **   <a name="AmazonS3-Type-control_S3JobManifestGenerator-ManifestOutputLocation"></a>
Specifies the location the generated manifest will be written to. Manifests can't be written to directory buckets. For more information, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html).
Type: [S3ManifestOutputLocation](API_control_S3ManifestOutputLocation.md) data type
Required: No

## See Also
<a name="API_control_S3JobManifestGenerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3JobManifestGenerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3JobManifestGenerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3JobManifestGenerator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
