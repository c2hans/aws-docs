---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVolume.html
---

# ModifyVolume
<a name="API_ModifyVolume"></a>

You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you might be able to apply these changes without stopping the instance or detaching the volume from it. For more information about modifying EBS volumes, see [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html) in the *Amazon EBS User Guide*.

When you complete a resize operation on your volume, you need to extend the volume's file-system size to take advantage of the new storage capacity. For more information, see [Extend the file system](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html).

For more information, see [Monitor the progress of volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-modifications.html) in the *Amazon EBS User Guide*.

With previous-generation instance types, resizing an EBS volume might require detaching and reattaching the volume or stopping and restarting the instance.

After you initiate a volume modification, you must wait for that modification to reach the `completed` state before you can initiate another modification for the same volume. You can modify a volume up to four times within a rolling 24-hour period, as long as the volume is in the `in-use` or `available` state, and all previous modifications for that volume are `completed`. If you exceed this limit, you get an error message that indicates when you can perform your next modification.

## Request Parameters
<a name="API_ModifyVolume_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Iops**
The target IOPS rate of the volume. This parameter is valid only for `gp3`, `io1`, and `io2` volumes.
The following are the supported values for each volume type:
+  `gp3`: 3,000 - 80,000 IOPS
+  `io1`: 100 - 64,000 IOPS
+  `io2`: 100 - 256,000 IOPS
 [ Instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.
Default: The existing value is retained if you keep the same volume type. If you change the volume type to `io1`, `io2`, or `gp3`, the default is 3,000.
Type: Integer
Required: No

 **MultiAttachEnabled**
Specifies whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 [ Nitro-based instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) in the same Availability Zone. This parameter is supported with `io1` and `io2` volumes only. For more information, see [ Amazon EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html) in the *Amazon EBS User Guide*.
Type: Boolean
Required: No

 **Size**
The target size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the volume.
The following are the supported volumes sizes for each volume type:
+  `gp2`: 1 - 16,384 GiB
+  `gp3`: 1 - 65,536 GiB
+  `io1`: 4 - 16,384 GiB
+  `io2`: 4 - 65,536 GiB
+  `st1` and `sc1`: 125 - 16,384 GiB
+  `standard`: 1 - 1024 GiB
Default: The existing size is retained.
Type: Integer
Required: No

 **Throughput**
The target throughput of the volume, in MiB/s. This parameter is valid only for `gp3` volumes. The maximum value is 2,000.
Default: The existing value is retained if the source and target volume type is `gp3`. Otherwise, the default value is 125.
Valid Range: Minimum value of 125. Maximum value of 2,000.
Type: Integer
Required: No

 **VolumeId**
The ID of the volume.
Type: String
Required: Yes

 **VolumeType**
The target EBS volume type of the volume. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
Default: The existing type is retained.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Elements
<a name="API_ModifyVolume_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **volumeModification**
Information about the volume modification.
Type: [VolumeModification](API_VolumeModification.md) object

## Errors
<a name="API_ModifyVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVolume_Examples"></a>

### Modify size, type, and IOPS provisioning of a volume
<a name="API_ModifyVolume_Example_1"></a>

This example illustrates one usage of ModifyVolume.

#### Sample Request
<a name="API_ModifyVolume_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVolume
&VolumeId=vol-1234567890EXAMPLE
&VolumeType=io1
&Iops=10000
&Size=200
&Version=2016-11-15
```

#### Sample Response
<a name="API_ModifyVolume_Example_1_Response"></a>

```
<ModifyVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
    <volumeModification>
        <targetIops>10000</targetIops>
        <originalIops>300</originalIops>
        <modificationState>modifying</modificationState>
        <targetSize>200</targetSize>
        <targetVolumeType>io1</targetVolumeType>
        <targetMultiAttachEnabled>false</targetMultiAttachEnabled>
        <volumeId>vol-1234567890EXAMPLE</volumeId>
        <progress>0</progress>
        <startTime>2017-01-19T23:58:04.922Z</startTime>
        <originalSize>100</originalSize>
        <originalVolumeType>gp2</originalVolumeType>
        <originalMultiAttachEnabled>false</originalMultiAttachEnabled>
    </volumeModification>
</ModifyVolumeResponse>
```

### Modify Multi-Attach support
<a name="API_ModifyVolume_Example_2"></a>

This example illustrates one usage of ModifyVolume.

#### Sample Request
<a name="API_ModifyVolume_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVolume
&VolumeId=vol-1234567890EXAMPLE
&MultiAttachEnabled=true
&Version=2016-11-15
```

#### Sample Response
<a name="API_ModifyVolume_Example_2_Response"></a>

```
<ModifyVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5jkdf074-37ed-4004-8671-a78ee82bf1cbEXAMPLE</requestId>
    <volumeModification>
        <originalMultiAttachEnabled>false</originalMultiAttachEnabled>
        <targetMultiAttachEnabled>true</targetMultiAttachEnabled>
    </volumeModification>
</ModifyVolumeResponse>
```

## See Also
<a name="API_ModifyVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
