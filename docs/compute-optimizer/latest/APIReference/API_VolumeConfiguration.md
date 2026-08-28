---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeConfiguration.html
---

# VolumeConfiguration
<a name="API_VolumeConfiguration"></a>

Describes the configuration of an Amazon Elastic Block Store (Amazon EBS) volume.

## Contents
<a name="API_VolumeConfiguration_Contents"></a>

 ** rootVolume **   <a name="computeoptimizer-Type-VolumeConfiguration-rootVolume"></a>
 Contains the image used to boot the instance during launch.
Type: Boolean
Required: No

 ** volumeBaselineIOPS **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeBaselineIOPS"></a>
The baseline IOPS of the volume.
Type: Integer
Required: No

 ** volumeBaselineThroughput **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeBaselineThroughput"></a>
The baseline throughput of the volume.
Type: Integer
Required: No

 ** volumeBurstIOPS **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeBurstIOPS"></a>
The burst IOPS of the volume.
Type: Integer
Required: No

 ** volumeBurstThroughput **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeBurstThroughput"></a>
The burst throughput of the volume.
Type: Integer
Required: No

 ** volumeSize **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeSize"></a>
The size of the volume, in GiB.
Type: Integer
Required: No

 ** volumeType **   <a name="computeoptimizer-Type-VolumeConfiguration-volumeType"></a>
The volume type.
The volume types can be the following:
+ General Purpose SSD `gp2` and `gp3`
+ Provisioned IOPS SSD `io1`, `io2`, and `io2 Block Express`
+ Throughput Optimized HDD `st1`
+ Cold HDD `sc1`
+ Magnetic volumes `standard`
Type: String
Required: No

## See Also
<a name="API_VolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/VolumeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/VolumeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/VolumeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
