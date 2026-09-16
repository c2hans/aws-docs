---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVolume.html
---

# DetachVolume
<a name="API_DetachVolume"></a>

Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becoming stuck in the `busy` state while detaching. If this happens, detachment can be delayed indefinitely until you unmount the volume, force detachment, reboot the instance, or all three. If an EBS volume is the root device of an instance, it can't be detached while the instance is running. To detach the root volume, stop the instance first.

When a volume with an AWS Marketplace product code is detached from an instance, the product code is no longer associated with the instance.

You can't detach or force detach volumes that are attached to AWS-managed resources. Attempting to do this results in the `UnsupportedOperationException` exception.

For more information, see [Detach an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_DetachVolume_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Device**
The device name.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance. If you are detaching a Multi-Attach enabled volume, you must specify an instance ID.
Type: String
Required: No

 **VolumeId**
The ID of the volume.
Type: String
Required: Yes

## Response Elements
<a name="API_DetachVolume_ResponseElements"></a>

The following elements are returned by the service.

 **associatedResource**
The ARN of the AWS-managed resource to which the volume is attached.
Type: String

 **attachTime**
The time stamp when the attachment initiated.
Type: Timestamp

 **deleteOnTermination**
Indicates whether the EBS volume is deleted on instance termination.
Type: Boolean

 **device**
The device name.
If the volume is attached to an AWS-managed resource, this parameter returns `null`.
Type: String

 **ebsCardIndex**
The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
Type: Integer

 **instanceId**
The ID of the instance.
If the volume is attached to an AWS-managed resource, this parameter returns `null`.
Type: String

 **instanceOwningService**
The service principal of the AWS service that owns the underlying resource to which the volume is attached.
This parameter is returned only for volumes that are attached to AWS-managed resources.
Type: String

 **requestId**
The ID of the request.
Type: String

 **status**
The attachment state of the volume.
Type: String
Valid Values: `attaching | attached | detaching | detached | busy`

 **volumeId**
The ID of the volume.
Type: String

## Errors
<a name="API_DetachVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DetachVolume_Examples"></a>

### Example
<a name="API_DetachVolume_Example_1"></a>

This example detaches volume `vol-1234567890abcdef0`.

#### Sample Request
<a name="API_DetachVolume_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DetachVolume
&VolumeId=vol-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DetachVolume_Example_1_Response"></a>

```
<DetachVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <volumeId>vol-1234567890abcdef0</volumeId>
   <instanceId>i-1234567890abcdef0</instanceId>
   <device>/dev/sdh</device>
   <status>detaching</status>
   <attachTime>YYYY-MM-DDTHH:MM:SS.000Z</attachTime>
</DetachVolumeResponse>
```

## See Also
<a name="API_DetachVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DetachVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DetachVolume)
