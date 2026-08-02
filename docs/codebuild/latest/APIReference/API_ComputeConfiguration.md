---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ComputeConfiguration.html
---

# ComputeConfiguration
<a name="API_ComputeConfiguration"></a>

Contains compute attributes. These attributes only need be specified when your project's or fleet's `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` or `CUSTOM_INSTANCE_TYPE`.

## Contents
<a name="API_ComputeConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** disk **   <a name="CodeBuild-Type-ComputeConfiguration-disk"></a>
The amount of disk space of the instance type included in your fleet.
Type: Long
Required: No

 ** instanceType **   <a name="CodeBuild-Type-ComputeConfiguration-instanceType"></a>
The EC2 instance type to be launched in your fleet.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** machineType **   <a name="CodeBuild-Type-ComputeConfiguration-machineType"></a>
The machine type of the instance type included in your fleet.
Type: String
Valid Values: `GENERAL | NVME`
Required: No

 ** memory **   <a name="CodeBuild-Type-ComputeConfiguration-memory"></a>
The amount of memory of the instance type included in your fleet.
Type: Long
Required: No

 ** vCpu **   <a name="CodeBuild-Type-ComputeConfiguration-vCpu"></a>
The number of vCPUs of the instance type included in your fleet.
Type: Long
Required: No

## See Also
<a name="API_ComputeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ComputeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ComputeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ComputeConfiguration)
