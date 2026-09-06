---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_EbsVolumeConfiguration.html
---

# EbsVolumeConfiguration
<a name="API_automation_EbsVolumeConfiguration"></a>

Configuration details for an Amazon EBS volume.

## Contents
<a name="API_automation_EbsVolumeConfiguration_Contents"></a>

 ** iops **   <a name="computeoptimizer-Type-automation_EbsVolumeConfiguration-iops"></a>
The number of I/O operations per second (IOPS) provisioned for the volume.
Type: Integer
Required: No

 ** sizeInGib **   <a name="computeoptimizer-Type-automation_EbsVolumeConfiguration-sizeInGib"></a>
The size of the EBS volume in gibibytes (GiB).
Type: Integer
Required: No

 ** throughput **   <a name="computeoptimizer-Type-automation_EbsVolumeConfiguration-throughput"></a>
The throughput in MiB/s provisioned for the volume (applicable to gp3, io1, and io2bx volumes).
Type: Integer
Required: No

 ** type **   <a name="computeoptimizer-Type-automation_EbsVolumeConfiguration-type"></a>
The EBS volume type, such as gp2, gp3, io1, io2, st1, or sc1.
Type: String
Required: No

## See Also
<a name="API_automation_EbsVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/EbsVolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/EbsVolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/EbsVolumeConfiguration)
