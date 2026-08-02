---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2LaunchTemplateDataCpuOptionsDetails.html
---

# AwsEc2LaunchTemplateDataCpuOptionsDetails
<a name="API_AwsEc2LaunchTemplateDataCpuOptionsDetails"></a>

 Specifies the CPU options for an Amazon EC2 instance. For more information, see [Optimize CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Contents
<a name="API_AwsEc2LaunchTemplateDataCpuOptionsDetails_Contents"></a>

 ** CoreCount **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataCpuOptionsDetails-CoreCount"></a>
 The number of CPU cores for the instance.
Type: Integer
Required: No

 ** ThreadsPerCore **   <a name="securityhub-Type-AwsEc2LaunchTemplateDataCpuOptionsDetails-ThreadsPerCore"></a>
 The number of threads per CPU core. A value of `1` disables multithreading for the instance, The default value is `2`.
Type: Integer
Required: No

## See Also
<a name="API_AwsEc2LaunchTemplateDataCpuOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2LaunchTemplateDataCpuOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2LaunchTemplateDataCpuOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2LaunchTemplateDataCpuOptionsDetails)
