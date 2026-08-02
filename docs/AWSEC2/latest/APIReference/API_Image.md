---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Image.html
---

# Image
<a name="API_Image"></a>

Describes an image.

## Contents
<a name="API_Image_Contents"></a>

 ** architecture **
The architecture of the image.
Type: String
Valid Values: `i386 | x86_64 | arm64 | x86_64_mac | arm64_mac`
Required: No

 ** BlockDeviceMapping.N **
Any block device mapping entries.
Type: Array of [BlockDeviceMapping](API_BlockDeviceMapping.md) objects
Required: No

 ** bootMode **
The boot mode of the image. For more information, see [Instance launch behavior with Amazon EC2 boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `legacy-bios | uefi | uefi-preferred`
Required: No

 ** creationDate **
The date and time the image was created.
Type: String
Required: No

 ** deprecationTime **
The date and time to deprecate the AMI, in UTC, in the following format: *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z. If you specified a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.
Type: String
Required: No

 ** deregistrationProtection **
Indicates whether deregistration protection is enabled for the AMI.
Type: String
Required: No

 ** description **
The description of the AMI that was provided during image creation.
Type: String
Required: No

 ** enaSupport **
Specifies whether enhanced networking with ENA is enabled.
Type: Boolean
Required: No

 ** freeTierEligible **
Indicates whether the image is eligible for AWS Free Tier.
+ If `true`, the AMI is eligible for Free Tier and can be used to launch instances under the Free Tier limits.
+ If `false`, the AMI is not eligible for Free Tier.
Type: Boolean
Required: No

 ** hypervisor **
The hypervisor type of the image. Only `xen` is supported. `ovm` is not supported.
Type: String
Valid Values: `ovm | xen`
Required: No

 ** imageAllowed **
If `true`, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If `false` and Allowed AMIs is set to `enabled`, the AMI can't be discovered or used in the account. If `false` and Allowed AMIs is set to `audit-mode`, the AMI can be discovered and used in the account.
For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 ** imageId **
The ID of the AMI.
Type: String
Required: No

 ** imageLocation **
The location of the AMI.
Type: String
Required: No

 ** imageOwnerAlias **
The owner alias (`amazon` \| `aws-backup-vault` \| `aws-marketplace`).
Type: String
Required: No

 ** imageOwnerId **
The ID of the AWS account that owns the image.
Type: String
Required: No

 ** imageState **
The current state of the AMI. If the state is `available`, the image is successfully registered and can be used to launch an instance.
Type: String
Valid Values: `pending | available | invalid | deregistered | transient | failed | error | disabled`
Required: No

 ** imageType **
The type of image.
Type: String
Valid Values: `machine | kernel | ramdisk`
Required: No

 ** ImageWatermarkSet.N **
The watermarks attached to the AMI.
Type: Array of [ImageWatermark](API_ImageWatermark.md) objects
Required: No

 ** imdsSupport **
If `v2.0`, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2`. For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `v2.0`
Required: No

 ** isPublic **
Indicates whether the image has public launch permissions. The value is `true` if this image has public launch permissions or `false` if it has only implicit and explicit launch permissions.
Type: Boolean
Required: No

 ** kernelId **
The kernel associated with the image, if any. Only applicable for machine images.
Type: String
Required: No

 ** lastLaunchedTime **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.
 `lastLaunchedTime` data is available starting April 2017.
Type: String
Required: No

 ** name **
The name of the AMI that was provided during image creation.
Type: String
Required: No

 ** platform **
This value is set to `windows` for Windows AMIs; otherwise, it is blank.
Type: String
Valid Values: `Windows`
Required: No

 ** platformDetails **
The platform details associated with the billing code of the AMI. For more information, see [Understand AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** ProductCodes.N **
Any product codes associated with the AMI.
Type: Array of [ProductCode](API_ProductCode.md) objects
Required: No

 ** publicSsmParameterName **
The name of the public Systems Manager parameter that resolves to this AMI, under the `aws/service/` namespace.
Type: String
Required: No

 ** ramdiskId **
The RAM disk associated with the image, if any. Only applicable for machine images.
Type: String
Required: No

 ** rootDeviceName **
The device name of the root device volume (for example, `/dev/sda1`).
Type: String
Required: No

 ** rootDeviceType **
The type of root device used by the AMI. The AMI can use an Amazon EBS volume or an instance store volume.
Type: String
Valid Values: `ebs | instance-store`
Required: No

 ** sourceImageId **
The ID of the source AMI from which the AMI was created.
The ID only appears if the AMI was created using [CreateImage](API_CreateImage.md), [CopyImage](API_CopyImage.md), or [CreateRestoreImageTask](API_CreateRestoreImageTask.md). The ID does not appear if the AMI was created using any other API. For some older AMIs, the ID might not be available. For more information, see [Identify the source AMI used to create a new Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** sourceImageRegion **
The Region of the source AMI.
The Region only appears if the AMI was created using [CreateImage](API_CreateImage.md), [CopyImage](API_CopyImage.md), or [CreateRestoreImageTask](API_CreateRestoreImageTask.md). The Region does not appear if the AMI was created using any other API. For some older AMIs, the Region might not be available. For more information, see [Identify the source AMI used to create a new Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify-source-ami-used-to-create-new-ami.html) in the *Amazon EC2 User Guide*.
Type: String
Required: No

 ** sourceInstanceId **
The ID of the instance that the AMI was created from if the AMI was created using [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html). This field only appears if the AMI was created using CreateImage.
Type: String
Required: No

 ** sriovNetSupport **
Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.
Type: String
Required: No

 ** stateReason **
The reason for the state change.
Type: [StateReason](API_StateReason.md) object
Required: No

 ** TagSet.N **
Any tags assigned to the image.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** tpmSupport **
If the image is configured for NitroTPM support, the value is `v2.0`. For more information, see [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `v2.0`
Required: No

 ** usageOperation **
The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. `usageOperation` corresponds to the [lineitem/Operation](https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation) column on your AWS Cost and Usage Report and in the [AWS Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html). You can view these fields on the **Instances** or **AMIs** pages in the Amazon EC2 console, or in the responses that are returned by the [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html) command in the Amazon EC2 API, or the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command in the AWS CLI.
Type: String
Required: No

 ** virtualizationType **
The type of virtualization of the AMI.
Type: String
Valid Values: `hvm | paravirtual`
Required: No

## See Also
<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Image)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Image)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Image)
