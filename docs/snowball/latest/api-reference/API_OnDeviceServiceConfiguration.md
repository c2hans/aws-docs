---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_OnDeviceServiceConfiguration.html
---

# OnDeviceServiceConfiguration
<a name="API_OnDeviceServiceConfiguration"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

An object that represents the metadata and configuration settings for services on an AWS Snowball Edge device.

## Contents
<a name="API_OnDeviceServiceConfiguration_Contents"></a>

 ** EKSOnDeviceService **   <a name="Snowball-Type-OnDeviceServiceConfiguration-EKSOnDeviceService"></a>
The configuration of EKS Anywhere on the Snowball Edge device.
Type: [EKSOnDeviceServiceConfiguration](API_EKSOnDeviceServiceConfiguration.md) object
Required: No

 ** NFSOnDeviceService **   <a name="Snowball-Type-OnDeviceServiceConfiguration-NFSOnDeviceService"></a>
Represents the NFS (Network File System) service on a Snowball Edge device.
Type: [NFSOnDeviceServiceConfiguration](API_NFSOnDeviceServiceConfiguration.md) object
Required: No

 ** S3OnDeviceService **   <a name="Snowball-Type-OnDeviceServiceConfiguration-S3OnDeviceService"></a>
Configuration for Amazon S3 compatible storage on Snowball Edge devices.
Type: [S3OnDeviceServiceConfiguration](API_S3OnDeviceServiceConfiguration.md) object
Required: No

 ** TGWOnDeviceService **   <a name="Snowball-Type-OnDeviceServiceConfiguration-TGWOnDeviceService"></a>
Represents the Storage Gateway service Tape Gateway type on a Snow Family device.
The Tape Gateway service is no longer available on Snowball Edge devices.
Type: [TGWOnDeviceServiceConfiguration](API_TGWOnDeviceServiceConfiguration.md) object
Required: No

## See Also
<a name="API_OnDeviceServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/OnDeviceServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/OnDeviceServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/OnDeviceServiceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
