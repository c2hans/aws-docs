---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CampaignSummary.html
---

# CampaignSummary
<a name="API_CampaignSummary"></a>

Information about a campaign.

You can use the [ListCampaigns](API_ListCampaigns.md) API operation to return this information about multiple created campaigns.

## Contents
<a name="API_CampaignSummary_Contents"></a>

 ** creationTime **   <a name="iotfleetwise-Type-CampaignSummary-creationTime"></a>
The time the campaign was created.
Type: Timestamp
Required: Yes

 ** lastModificationTime **   <a name="iotfleetwise-Type-CampaignSummary-lastModificationTime"></a>
The last time the campaign was modified.
Type: Timestamp
Required: Yes

 ** arn **   <a name="iotfleetwise-Type-CampaignSummary-arn"></a>
The Amazon Resource Name (ARN) of a campaign.
Type: String
Pattern: `arn:aws:iotfleetwise:[a-z0-9-]+:[0-9]{12}:campaign/[a-zA-Z\d\-_:]{1,100}`
Required: No

 ** description **   <a name="iotfleetwise-Type-CampaignSummary-description"></a>
The description of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** name **   <a name="iotfleetwise-Type-CampaignSummary-name"></a>
The name of a campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

 ** signalCatalogArn **   <a name="iotfleetwise-Type-CampaignSummary-signalCatalogArn"></a>
The ARN of the signal catalog associated with the campaign.
Type: String
Required: No

 ** status **   <a name="iotfleetwise-Type-CampaignSummary-status"></a>
The state of a campaign. The status can be one of the following:
+  `CREATING` - AWS IoT FleetWise is processing your request to create the campaign.
+  `WAITING_FOR_APPROVAL` - After a campaign is created, it enters the `WAITING_FOR_APPROVAL` state. To allow AWS IoT FleetWise to deploy the campaign to the target vehicle or fleet, use the [UpdateCampaign](API_UpdateCampaign.md) API operation to approve the campaign.
+  `RUNNING` - The campaign is active.
+  `SUSPENDED` - The campaign is suspended. To resume the campaign, use the [UpdateCampaign](API_UpdateCampaign.md) API operation.
Type: String
Valid Values: `CREATING | WAITING_FOR_APPROVAL | RUNNING | SUSPENDED`
Required: No

 ** targetArn **   <a name="iotfleetwise-Type-CampaignSummary-targetArn"></a>
The ARN of a vehicle or fleet to which the campaign is deployed.
Type: String
Required: No

## See Also
<a name="API_CampaignSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CampaignSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CampaignSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CampaignSummary)
