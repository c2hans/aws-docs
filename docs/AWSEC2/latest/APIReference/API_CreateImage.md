---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html
---

# CreateImage
<a name="API_CreateImage"></a>

Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.

If you customized your instance with instance store volumes or Amazon EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes.

The location of the source instance determines where you can create the snapshots of the AMI:
+ If the source instance is in a Region, you must create the snapshots in the same Region as the instance.
+ If the source instance is in a Local Zone, you can create the snapshots in the same Local Zone or in its parent Region.

For more information, see [Create an Amazon EBS-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Parameters
<a name="API_CreateImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **BlockDeviceMapping.N**
The block device mappings.
When using the CreateImage action:
+ You can't change the volume size using the VolumeSize parameter. If you want a different volume size, you must first change the volume size of the source instance.
+ You can't modify the encryption status of existing volumes or snapshots. To create an AMI with volumes or snapshots that have a different encryption status (for example, where the source volume and snapshots are unencrypted, and you want to create an AMI with encrypted volumes or snapshots), copy the image instead.
+ The only option that can be changed for existing mappings or snapshots is `DeleteOnTermination`.
Type: Array of [BlockDeviceMapping](API_BlockDeviceMapping.md) objects
Required: No

 **Description**
A description for the new image.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **Name**
A name for the new image.
Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(\_)
Type: String
Required: Yes

 **NoReboot**
Indicates whether or not the instance should be automatically rebooted before creating the image. Specify one of the following values:
+  `true` - The instance is not rebooted before creating the image. This creates crash-consistent snapshots that include only the data that has been written to the volumes at the time the snapshots are created. Buffered data and data in memory that has not yet been written to the volumes is not included in the snapshots.
+  `false` - The instance is rebooted before creating the image. This ensures that all buffered data and data in memory is written to the volumes before the snapshots are created.
Default: `false`
Type: Boolean
Required: No

 **SnapshotLocation**
Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter.
The Amazon S3 location where the snapshots will be stored.
+ To create local snapshots in the same Local Zone as the source instance, specify `local`.
+ To create regional snapshots in the parent Region of the Local Zone, specify `regional` or omit this parameter.
Default: `regional`
Type: String
Valid Values: `regional | local`
Required: No

 **TagSpecification.N**
The tags to apply to the AMI and snapshots on creation. You can tag the AMI, the snapshots, or both.
+ To tag the AMI, the value for `ResourceType` must be `image`.
+ To tag the snapshots that are created of the root volume and of other Amazon EBS volumes that are attached to the instance, the value for `ResourceType` must be `snapshot`. The same tag is applied to all of the snapshots that are created.
If you specify other values for `ResourceType`, the request fails.
To tag an AMI or snapshot after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateImage_ResponseElements"></a>

The following elements are returned by the service.

 **imageId**
The ID of the new AMI.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateImage_Examples"></a>

### Example 1
<a name="API_CreateImage_Example_1"></a>

This example request creates an AMI from the specified instance.

#### Sample Request
<a name="API_CreateImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateImage
&Description=Standard+Web+Server+v1.0
&InstanceId=i-1234567890abcdef0
&Name=standard-web-server-v1.0
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateImage_Example_1_Response"></a>

```
<CreateImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <imageId>ami-4fa54026</imageId>
</CreateImageResponse>
```

### Example 2
<a name="API_CreateImage_Example_2"></a>

This example request creates an AMI from the specified instance, and sets the NoReboot parameter to true (the instance is not rebooted before the image is created).

#### Sample Request
<a name="API_CreateImage_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateImage
&Description=Standard+Web+Server+v1.0
&InstanceId=i-1234567890abcdef0
&Name=standard-web-server-v1.0
&NoReboot=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateImage_Example_2_Response"></a>

```
<CreateImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <imageId>ami-4fa54026</imageId>
</CreateImageResponse>
```

### Example 3
<a name="API_CreateImage_Example_3"></a>

This example request creates an AMI from the specified instance, and tags on creation the AMI and the snapshots that are created of the root volume and of other Amazon EBS volumes that are attached to the instance. In this example, the tag that is applied to the AMI and the snapshots is the same, with a key of `purpose` and a value of `test`.

#### Sample Request
<a name="API_CreateImage_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateImage
&InstanceId=i-1234567890abcdef0
&TagSpecification.1.ResourceType=image
&TagSpecification.1.Tag.1.Key=purpose
&TagSpecification.1.Tag.1.Value=test
&TagSpecification.2.ResourceType=snapshot
&TagSpecification.2.Tag.1.Key=purpose
&TagSpecification.2.Tag.1.Value=test
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateImage_Example_3_Response"></a>

```
<CreateImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <imageId>ami-4fa54026</imageId>
</CreateImageResponse>
```

## See Also
<a name="API_CreateImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateImage)
