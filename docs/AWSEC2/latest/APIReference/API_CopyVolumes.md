---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyVolumes.html
---

# CopyVolumes
<a name="API_CopyVolumes"></a>

Creates a crash-consistent, point-in-time copy of an existing Amazon EBS volume within the same Availability Zone. The volume copy can be attached to an Amazon EC2 instance once it reaches the `available` state. For more information, see [Copy an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copying-volume.html).

## Request Parameters
<a name="API_CopyVolumes_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [ Ensure Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Iops**
The number of I/O operations per second (IOPS) to provision for the volume copy. Required for `io1` and `io2` volumes. Optional for `gp3` volumes. Omit for all other volume types. Full provisioned IOPS performance can be achieved only once the volume copy is fully initialized.
Valid ranges:
+ gp3: `3,000 `(*default*)` - 80,000` IOPS
+ io1: `100 - 64,000` IOPS
+ io2: `100 - 256,000` IOPS
 [ Instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.
Type: Integer
Required: No

 **MultiAttachEnabled**
Indicates whether to enable Amazon EBS Multi-Attach for the volume copy. If you enable Multi-Attach, you can attach the volume to up to 16 Nitro instances in the same Availability Zone simultaneously. Supported with `io1` and `io2` volumes only. For more information, see [ Amazon EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html).
Type: Boolean
Required: No

 **Size**
The size of the volume copy, in GiBs. The size must be equal to or greater than the size of the source volume. If not specified, the size defaults to the size of the source volume.
Maximum supported sizes:
+ gp2: `16,384` GiB
+ gp3: `65,536` GiB
+ io1: `16,384` GiB
+ io2: `65,536` GiB
+ st1 and sc1: `16,384` GiB
+ standard: `1024` GiB
Type: Integer
Required: No

 **SourceVolumeId**
The ID of the source EBS volume to copy.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the volume copy during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Throughput**
The throughput to provision for the volume copy, in MiB/s. Supported for `gp3` volumes only. Omit for all other volume types. Full provisioned throughput performance can be achieved only once the volume copy is fully initialized.
Valid Range: `125 - 2000` MiB/s

Type: Integer
Required: No

 **VolumeType**
The volume type for the volume copy. If not specified, the volume type defaults to `gp2`.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Elements
<a name="API_CopyVolumes_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **volumeSet**
Information about the volume copy.
Type: Array of [Volume](API_Volume.md) objects

## Errors
<a name="API_CopyVolumes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CopyVolumes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CopyVolumes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CopyVolumes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
