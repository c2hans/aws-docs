---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DiskImageDetail.html
---

# DiskImageDetail
<a name="API_DiskImageDetail"></a>

Describes a disk image.

## Contents
<a name="API_DiskImageDetail_Contents"></a>

 ** Bytes **
The size of the disk image, in GiB.
Type: Long
Required: Yes

 ** Format **
The disk image format.
Type: String
Valid Values: `VMDK | RAW | VHD`
Required: Yes

 ** ImportManifestUrl **
A presigned URL for the import manifest stored in Amazon S3 and presented here as an Amazon S3 presigned URL. For information about creating a presigned URL for an Amazon S3 object, read the "Query String Request Authentication Alternative" section of the [Authenticating REST Requests](https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) topic in the *Amazon Simple Storage Service Developer Guide*.
For information about the import manifest referenced by this API action, see [VM Import Manifest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html).
Type: String
Required: Yes

## See Also
<a name="API_DiskImageDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DiskImageDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DiskImageDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DiskImageDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
