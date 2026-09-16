---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateReplaceRootVolumeTask.html
---

# CreateReplaceRootVolumeTask
<a name="API_CreateReplaceRootVolumeTask"></a>

Replaces the EBS-backed root volume for a `running` instance with a new volume that is restored to the original root volume's launch state, that is restored to a specific snapshot taken from the original root volume, that is restored from an AMI that has the same key characteristics as that of the instance, or that is replaced by a specified volume.

For more information, see [Replace a root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateReplaceRootVolumeTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DeleteReplacedRootVolume**
Indicates whether to automatically delete the original root volume after the root volume replacement task completes. To delete the original root volume, specify `true`. If you choose to keep the original root volume after the replacement task completes, you must manually delete it when you no longer need it.
Type: Boolean
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI to use to restore the root volume. The specified AMI must have the same product code, billing information, architecture type, and virtualization type as that of the instance.
If you want to restore the replacement volume from a specific snapshot, if you want to restore it to its launch state, or if you want to replace the root volume with a specified volume, omit this parameter.
Type: String
Required: No

 **InstanceId**
The ID of the instance for which to replace the root volume.
Type: String
Required: Yes

 **SnapshotId**
The ID of the snapshot from which to restore the replacement root volume. The specified snapshot must be a snapshot that you previously created from the original root volume.
If you want to restore the replacement root volume to the initial launch state, if you want to restore the replacement root volume from an AMI, or if you want to replace the root volume with a specified volume, omit this parameter.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the root volume replacement task.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VolumeId**
The ID of the volume to use as the replacement root volume. The specified volume must be in the same Availability Zone as the instance, must be in the `available` state, and must not be attached to an instance. If the original root volume is encrypted, the specified volume must also be encrypted.
If you want to restore the replacement root volume from a specific snapshot, an AMI, or to its launch state, omit this parameter.
Type: String
Required: No

 **VolumeInitializationRate**
Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the replacement root volume. This is also known as *volume initialization*. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.
Omit this parameter if:
+ You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.
**Note**
If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.
+ You want to create a volume that is initialized at the default rate.
For more information, see [ Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EC2 User Guide*.
Valid range: 100 - 300 MiB/s
Type: Long
Required: No

## Response Elements
<a name="API_CreateReplaceRootVolumeTask_ResponseElements"></a>

The following elements are returned by the service.

 **replaceRootVolumeTask**
Information about the root volume replacement task.
Type: [ReplaceRootVolumeTask](API_ReplaceRootVolumeTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateReplaceRootVolumeTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateReplaceRootVolumeTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateReplaceRootVolumeTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateReplaceRootVolumeTask)
