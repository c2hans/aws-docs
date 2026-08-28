---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageWatermark.html
---

# ImageWatermark
<a name="API_ImageWatermark"></a>

Describes a watermark attached to an AMI.

## Contents
<a name="API_ImageWatermark_Contents"></a>

 ** sourceImageCreationTime **
The creation date of the source AMI, in the following format: *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*.*ssssss*\+*HH*:*MM*.
Type: Timestamp
Required: No

 ** sourceImageId **
The ID of the AMI to which the watermark was originally attached.
Type: String
Required: No

 ** sourceImageRegion **
The Region where the watermark was originally attached.
Type: String
Required: No

 ** watermarkCreationTime **
The date and time the watermark was attached to the AMI, in the following format: *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*.*ssssss*\+*HH*:*MM*.
Type: Timestamp
Required: No

 ** watermarkKey **
The watermark identifier, in `accountId:watermarkName` format (for example, `123456789012:approvedAmi`). The `accountId` portion is the AWS account ID of the watermark creator. The `watermarkName` portion is customer-provided.
Type: String
Required: No

## See Also
<a name="API_ImageWatermark_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageWatermark)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageWatermark)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageWatermark)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
