---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageWatermarkFilterRequest.html
---

# ImageWatermarkFilterRequest
<a name="API_ImageWatermarkFilterRequest"></a>

The watermark filter criteria for an allowed image. Each entry can specify one or more fields. All specified fields must match the same watermark on the image.

## Contents
<a name="API_ImageWatermarkFilterRequest_Contents"></a>

 ** MaximumDaysSinceSourceImageCreated **
The maximum number of days that have elapsed since the source image was created.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Required: No

 ** MaximumDaysSinceWatermarkCreated **
The maximum number of days that have elapsed since the watermark was attached to the image.
Constraints: Minimum value of 0. Maximum value of 2147483647.
Type: Integer
Required: No

 ** SourceImageRegion **
The Region where the watermark was originally created. Supports wildcards (`*`, `?`).
Type: String
Required: No

 ** WatermarkKey **
The `accountId:name` of the watermark. Supports wildcards (`*`, `?`).
Type: String
Required: No

## See Also
<a name="API_ImageWatermarkFilterRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageWatermarkFilterRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageWatermarkFilterRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageWatermarkFilterRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
