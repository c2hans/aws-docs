---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannelStatus.html
---

# DeliveryChannelStatus
<a name="API_DeliveryChannelStatus"></a>

The status of a specified delivery channel.

Valid values: `Success` \| `Failure`

## Contents
<a name="API_DeliveryChannelStatus_Contents"></a>

 ** configHistoryDeliveryInfo **   <a name="config-Type-DeliveryChannelStatus-configHistoryDeliveryInfo"></a>
A list that contains the status of the delivery of the configuration history to the specified Amazon S3 bucket.
Type: [ConfigExportDeliveryInfo](API_ConfigExportDeliveryInfo.md) object
Required: No

 ** configSnapshotDeliveryInfo **   <a name="config-Type-DeliveryChannelStatus-configSnapshotDeliveryInfo"></a>
A list containing the status of the delivery of the snapshot to the specified Amazon S3 bucket.
Type: [ConfigExportDeliveryInfo](API_ConfigExportDeliveryInfo.md) object
Required: No

 ** configStreamDeliveryInfo **   <a name="config-Type-DeliveryChannelStatus-configStreamDeliveryInfo"></a>
A list containing the status of the delivery of the configuration stream notification to the specified Amazon SNS topic.
Type: [ConfigStreamDeliveryInfo](API_ConfigStreamDeliveryInfo.md) object
Required: No

 ** name **   <a name="config-Type-DeliveryChannelStatus-name"></a>
The name of the delivery channel.
Type: String
Required: No

## See Also
<a name="API_DeliveryChannelStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeliveryChannelStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeliveryChannelStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeliveryChannelStatus)
