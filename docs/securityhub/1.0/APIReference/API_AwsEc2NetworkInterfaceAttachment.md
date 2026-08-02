---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2NetworkInterfaceAttachment.html
---

# AwsEc2NetworkInterfaceAttachment
<a name="API_AwsEc2NetworkInterfaceAttachment"></a>

Information about the network interface attachment.

## Contents
<a name="API_AwsEc2NetworkInterfaceAttachment_Contents"></a>

 ** AttachmentId **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-AttachmentId"></a>
The identifier of the network interface attachment
Type: String
Pattern: `.*\S.*`
Required: No

 ** AttachTime **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-AttachTime"></a>
Indicates when the attachment initiated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeleteOnTermination **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-DeleteOnTermination"></a>
Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** DeviceIndex **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-DeviceIndex"></a>
The device index of the network interface attachment on the instance.
Type: Integer
Required: No

 ** InstanceId **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-InstanceId"></a>
The ID of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InstanceOwnerId **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-InstanceOwnerId"></a>
The AWS account ID of the owner of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2NetworkInterfaceAttachment-Status"></a>
The attachment state.
Valid values: `attaching` \| `attached` \| `detaching` \| `detached`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2NetworkInterfaceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2NetworkInterfaceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2NetworkInterfaceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2NetworkInterfaceAttachment)
