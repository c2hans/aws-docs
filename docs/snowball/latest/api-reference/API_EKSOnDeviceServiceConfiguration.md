---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_EKSOnDeviceServiceConfiguration.html
---

# EKSOnDeviceServiceConfiguration
<a name="API_EKSOnDeviceServiceConfiguration"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

An object representing the metadata and configuration settings of EKS Anywhere on the Snowball Edge device.

## Contents
<a name="API_EKSOnDeviceServiceConfiguration_Contents"></a>

 ** EKSAnywhereVersion **   <a name="Snowball-Type-EKSOnDeviceServiceConfiguration-EKSAnywhereVersion"></a>
The optional version of EKS Anywhere on the Snowball Edge device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** KubernetesVersion **   <a name="Snowball-Type-EKSOnDeviceServiceConfiguration-KubernetesVersion"></a>
The Kubernetes version for EKS Anywhere on the Snowball Edge device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_EKSOnDeviceServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/EKSOnDeviceServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/EKSOnDeviceServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/EKSOnDeviceServiceConfiguration)
