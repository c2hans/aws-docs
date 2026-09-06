---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_VolumeiSCSIAttributes.html
---

# VolumeiSCSIAttributes
<a name="API_VolumeiSCSIAttributes"></a>

Lists iSCSI information about a volume.

## Contents
<a name="API_VolumeiSCSIAttributes_Contents"></a>

 ** ChapEnabled **   <a name="StorageGateway-Type-VolumeiSCSIAttributes-ChapEnabled"></a>
Indicates whether mutual CHAP is enabled for the iSCSI target.
Type: Boolean
Required: No

 ** LunNumber **   <a name="StorageGateway-Type-VolumeiSCSIAttributes-LunNumber"></a>
The logical disk number.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NetworkInterfaceId **   <a name="StorageGateway-Type-VolumeiSCSIAttributes-NetworkInterfaceId"></a>
The network interface identifier.
Type: String
Required: No

 ** NetworkInterfacePort **   <a name="StorageGateway-Type-VolumeiSCSIAttributes-NetworkInterfacePort"></a>
The port used to communicate with iSCSI targets.
Type: Integer
Required: No

 ** TargetARN **   <a name="StorageGateway-Type-VolumeiSCSIAttributes-TargetARN"></a>
The Amazon Resource Name (ARN) of the volume target.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 800.
Required: No

## See Also
<a name="API_VolumeiSCSIAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/VolumeiSCSIAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/VolumeiSCSIAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/VolumeiSCSIAttributes)
