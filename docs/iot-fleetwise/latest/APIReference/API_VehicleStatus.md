---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_VehicleStatus.html
---

# VehicleStatus
<a name="API_VehicleStatus"></a>

Information about a campaign associated with a vehicle.

## Contents
<a name="API_VehicleStatus_Contents"></a>

 ** campaignName **   <a name="iotfleetwise-Type-VehicleStatus-campaignName"></a>
The name of a campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

 ** status **   <a name="iotfleetwise-Type-VehicleStatus-status"></a>
The status of a campaign, which can be one of the following:
+  `CREATED` - The campaign exists but is not yet approved.
+  `READY` - The campaign is approved but has not been deployed to the vehicle. Data has not arrived at the vehicle yet.
+  `HEALTHY` - The campaign is deployed to the vehicle.
+  `SUSPENDED` - The campaign is suspended and data collection is paused.
+  `DELETING` - The campaign is being removed from the vehicle.
+  `READY_FOR_CHECKIN` - The campaign is approved and waiting for vehicle check-in before deployment.
Type: String
Valid Values: `CREATED | READY | HEALTHY | SUSPENDED | DELETING | READY_FOR_CHECKIN`
Required: No

 ** vehicleName **   <a name="iotfleetwise-Type-VehicleStatus-vehicleName"></a>
The unique ID of the vehicle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

## See Also
<a name="API_VehicleStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/VehicleStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/VehicleStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/VehicleStatus)
