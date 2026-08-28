---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage.html
---

# RegisterImage
<a name="API_RegisterImage"></a>

Registers an AMI. When you're creating an instance-store backed AMI, registering the AMI is the final step in the creation process. For more information about creating AMIs, see [Create an AMI from a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#creating-launching-ami-from-snapshot) and [Create an instance-store backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-instance-store.html) in the *Amazon EC2 User Guide*.

**Note**
For Amazon EBS-backed instances, [CreateImage](API_CreateImage.md) creates and registers the AMI in a single request, so you don't have to register the AMI yourself. We recommend that you always use [CreateImage](API_CreateImage.md) unless you have a specific reason to use RegisterImage.

If needed, you can deregister an AMI at any time. Any modifications you make to an AMI backed by an instance store volume invalidates its registration. If you make changes to an image, deregister the previous image and register the new image.

 **Register a snapshot of a root device volume**

You can use `RegisterImage` to create an Amazon EBS-backed Linux AMI from a snapshot of a root device volume. You specify the snapshot using a block device mapping. You can't set the encryption state of the volume using the block device mapping. If the snapshot is encrypted, or encryption by default is enabled, the root volume of an instance launched from the AMI is encrypted.

For more information, see [Create an AMI from a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#creating-launching-ami-from-snapshot) and [Use encryption with EBS-backed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html) in the *Amazon EC2 User Guide*.

 ** AWS Marketplace product codes**

If any snapshots have AWS Marketplace product codes, they are copied to the new AMI.

In most cases, AMIs for Windows, RedHat, SUSE, and SQL Server require correct licensing information to be present on the AMI. For more information, see [Understand AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html) in the *Amazon EC2 User Guide*. When creating an AMI from a snapshot, the `RegisterImage` operation derives the correct billing information from the snapshot's metadata, but this requires the appropriate metadata to be present. To verify if the correct billing information was applied, check the `PlatformDetails` field on the new AMI. If the field is empty or doesn't match the expected operating system code (for example, Windows, RedHat, SUSE, or SQL), the AMI creation was unsuccessful, and you should discard the AMI and instead create the AMI from an instance. For more information, see [Create an AMI from an instance ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#how-to-create-ebs-ami) in the *Amazon EC2 User Guide*.

If you purchase a Reserved Instance to apply to an On-Demand Instance that was launched from an AMI with a billing product code, make sure that the Reserved Instance has the matching billing product code. If you purchase a Reserved Instance without the matching billing product code, the Reserved Instance is not applied to the On-Demand Instance. For information about how to obtain the platform details and billing information of an AMI, see [Understand AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_RegisterImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Architecture**
The architecture of the AMI.
Default: For Amazon EBS-backed AMIs, `i386`. For instance store-backed AMIs, the architecture specified in the manifest file.
Type: String
Valid Values: `i386 | x86_64 | arm64 | x86_64_mac | arm64_mac`
Required: No

 **BillingProduct.N**
The billing product codes. Your account must be authorized to specify billing product codes.
If your account is not authorized to specify billing product codes, you can publish AMIs that include billable software and list them on the AWS Marketplace. You must first register as a seller on the AWS Marketplace. For more information, see [Getting started as an AWS Marketplace seller](https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html) and [AMI-based products in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-products.html) in the * AWS Marketplace Seller Guide*.
Type: Array of strings
Required: No

 **BlockDeviceMapping.N**
The block device mapping entries.
If you specify an Amazon EBS volume using the ID of an Amazon EBS snapshot, you can't specify the encryption state of the volume.
If you create an AMI on an Outpost, then all backing snapshots must be on the same Outpost or in the Region of that Outpost. AMIs on an Outpost that include local snapshots can be used to launch instances on the same Outpost only. For more information, [Create AMIs from local snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#ami) in the *Amazon EBS User Guide*.
Type: Array of [BlockDeviceMapping](API_BlockDeviceMapping.md) objects
Required: No

 **BootMode**
The boot mode of the AMI. A value of `uefi-preferred` indicates that the AMI supports both UEFI and Legacy BIOS.
The operating system contained in the AMI must be configured to support the specified boot mode.
For more information, see [Instance launch behavior with Amazon EC2 boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `legacy-bios | uefi | uefi-preferred`
Required: No

 **Description**
A description for your AMI.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EnaSupport**
Set to `true` to enable enhanced networking with ENA for the AMI and any instances that you launch from the AMI.
This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
Type: Boolean
Required: No

 **ImageLocation**
The full path to your AMI manifest in Amazon S3 storage. The specified bucket must have the `aws-exec-read` canned access control list (ACL) to ensure that it can be accessed by Amazon EC2. For more information, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the *Amazon S3 Service Developer Guide*.
Type: String
Required: No

 **ImdsSupport**
Set to `v2.0` to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2`. For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.
If you set the value to `v2.0`, make sure that your AMI software can support IMDSv2.
Type: String
Valid Values: `v2.0`
Required: No

 **KernelId**
The ID of the kernel.
Type: String
Required: No

 **Name**
A name for your AMI.
Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(\_)
Type: String
Required: Yes

 **RamdiskId**
The ID of the RAM disk.
Type: String
Required: No

 **RootDeviceName**
The device name of the root device volume (for example, `/dev/sda1`).
Type: String
Required: No

 **SriovNetSupport**
Set to `simple` to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI.
There is no way to disable `sriovNetSupport` at this time.
This option is supported only for HVM AMIs. Specifying this option with a PV AMI can make instances launched from the AMI unreachable.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the AMI.
To tag the AMI, the value for `ResourceType` must be `image`. If you specify another value for `ResourceType`, the request fails.
To tag an AMI after it has been registered, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TpmSupport**
Set to `v2.0` to enable Trusted Platform Module (TPM) support. For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `v2.0`
Required: No

 **UefiData**
Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the [GetInstanceUefiData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData) command. You can inspect and modify the UEFI data by using the [python-uefivars tool](https://github.com/awslabs/python-uefivars) on GitHub. For more information, see [UEFI Secure Boot for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html) in the *Amazon EC2 User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64000.
Required: No

 **VirtualizationType**
The type of virtualization (`hvm` \| `paravirtual`).
Default: `paravirtual`
Type: String
Required: No

## Response Elements
<a name="API_RegisterImage_ResponseElements"></a>

The following elements are returned by the service.

 **imageId**
The ID of the newly registered AMI.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_RegisterImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RegisterImage_Examples"></a>

### Example 1
<a name="API_RegisterImage_Example_1"></a>

This example registers the AMI specified in the `my-new-image.manifest.xml` manifest file, located in the bucket called `myawsbucket`.

#### Sample Request
<a name="API_RegisterImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RegisterImage
&ImageLocation=myawsbucket/my-new-image.manifest.xml
&AUTHPARAMS
```

#### Sample Response
<a name="API_RegisterImage_Example_1_Response"></a>

```
<RegisterImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <imageId>ami-1a2b3c4d</imageId>
</RegisterImageResponse>
```

### Example 2
<a name="API_RegisterImage_Example_2"></a>

This example specifies a snapshot for the root device of an Amazon EBS-backed AMI.

#### Sample Request
<a name="API_RegisterImage_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=RegisterImage
&RootDeviceName=/dev/sda1
&BlockDeviceMapping.1.DeviceName=/dev/sda1
&BlockDeviceMapping.1.Ebs.SnapshotId=snap-1234567890abcdef0
&Name=MyImage
&AUTHPARAMS
```

#### Sample Response
<a name="API_RegisterImage_Example_2_Response"></a>

```
<RegisterImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <imageId>ami-1a2b3c4d</imageId>
</RegisterImageResponse>
```

### Example 3
<a name="API_RegisterImage_Example_3"></a>

This example registers an AMI with a block device mapping for three Amazon EBS volumes. The first volume is the root device volume based on an Amazon EBS snapshot. The second volume is based on another snapshot. The third volume is an empty 100 GiB Amazon EBS volume.

#### Sample Request
<a name="API_RegisterImage_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=RegisterImage
&RootDeviceName=/dev/sda1
&BlockDeviceMapping.1.DeviceName=/dev/sda1
&BlockDeviceMapping.1.Ebs.SnapshotId=snap-1234567890abcdef0
&BlockDeviceMapping.2.DeviceName=/dev/sdb
&BlockDeviceMapping.2.Ebs.SnapshotId=snap-1234567890abcdef1
&BlockDeviceMapping.3.DeviceName=/dev/sdc
&BlockDeviceMapping.3.Ebs.VolumeSize=100
&Name=MyImage
&AUTHPARAMS
```

#### Sample Response
<a name="API_RegisterImage_Example_3_Response"></a>

```
<RegisterImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <imageId>ami-1a2b3c4d</imageId>
</RegisterImageResponse>
```

## See Also
<a name="API_RegisterImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RegisterImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RegisterImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
