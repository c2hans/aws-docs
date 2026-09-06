---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInterfaceAttachmentChanges.html
---

# NetworkInterfaceAttachmentChanges
<a name="API_NetworkInterfaceAttachmentChanges"></a>

Describes an attachment change.

## Contents
<a name="API_NetworkInterfaceAttachmentChanges_Contents"></a>

 ** AttachmentId **
The ID of the network interface attachment.
Type: String
Required: No

 ** DefaultEnaQueueCount **
The default number of the ENA queues.
Type: Boolean
Required: No

 ** DeleteOnTermination **
Indicates whether the network interface is deleted when the instance is terminated.
Type: Boolean
Required: No

 ** EnaQueueCount **
The number of ENA queues to be created with the instance.
Type: Integer
Required: No

## See Also
<a name="API_NetworkInterfaceAttachmentChanges_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInterfaceAttachmentChanges)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInterfaceAttachmentChanges)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInterfaceAttachmentChanges)
