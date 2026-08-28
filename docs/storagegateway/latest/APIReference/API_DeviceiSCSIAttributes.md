---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DeviceiSCSIAttributes.html
---

# DeviceiSCSIAttributes
<a name="API_DeviceiSCSIAttributes"></a>

Lists iSCSI information about a VTL device.

## Contents
<a name="API_DeviceiSCSIAttributes_Contents"></a>

 ** ChapEnabled **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-ChapEnabled"></a>
Indicates whether mutual CHAP is enabled for the iSCSI target.
Type: Boolean
Required: No

 ** NetworkInterfaceId **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-NetworkInterfaceId"></a>
The network interface identifier of the VTL device.
Type: String
Required: No

 ** NetworkInterfacePort **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-NetworkInterfacePort"></a>
The port used to communicate with iSCSI VTL device targets.
Type: Integer
Required: No

 ** TargetARN **   <a name="StorageGateway-Type-DeviceiSCSIAttributes-TargetARN"></a>
Specifies the unique Amazon Resource Name (ARN) that encodes the iSCSI qualified name(iqn) of a tape drive or media changer target.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 800.
Required: No

## See Also
<a name="API_DeviceiSCSIAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeviceiSCSIAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeviceiSCSIAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeviceiSCSIAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
