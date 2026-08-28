---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVolume.html
---

# AttachVolume
<a name="API_AttachVolume"></a>

Attaches an Amazon EBS volume to a `running` or `stopped` instance, and exposes it to the instance with the specified device name.

**Note**
The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type. If you exceed the volume attachment limit for an instance type, the attachment request fails with the `AttachmentLimitExceeded` error. For more information, see [Instance volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html).

After you attach an EBS volume, you must make it available for use. For more information, see [Make an EBS volume available for use](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-using-volumes.html).

If a volume has an AWS Marketplace product code:
+ The volume can be attached only to a stopped instance.
+  AWS Marketplace product codes are copied from the volume to the instance.
+ You must be subscribed to the product.
+ The instance type and operating system of the instance must support the product. For example, you can't detach a volume from a Windows instance and attach it to a Linux instance.

For more information, see [Attach an Amazon EBS volume to an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_AttachVolume_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Device**
The device name (for example, `/dev/sdh` or `xvdh`).
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EbsCardIndex**
The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
Type: Integer
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **VolumeId**
The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
Type: String
Required: Yes

## Response Elements
<a name="API_AttachVolume_ResponseElements"></a>

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
<a name="API_AttachVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AttachVolume_Examples"></a>

### Example 1
<a name="API_AttachVolume_Example_1"></a>

This example request attaches the volume with the ID `vol-1234567890abcdef0` to the instance with the ID `i-1234567890abcdef0` and exposes it as `/dev/sdh`.

#### Sample Request
<a name="API_AttachVolume_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AttachVolume
&VolumeId=vol-1234567890abcdef0
&InstanceId=i-1234567890abcdef0
&Device=/dev/sdh
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachVolume_Example_1_Response"></a>

```
<AttachVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <volumeId>vol-1234567890abcdef0</volumeId>
  <instanceId>i-1234567890abcdef0</instanceId>
  <device>/dev/sdh</device>
  <status>attaching</status>
  <attachTime>YYYY-MM-DDTHH:MM:SS.000Z</attachTime>
</AttachVolumeResponse>
```

## See Also
<a name="API_AttachVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AttachVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AttachVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
