---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateVehicleError.html
---

# UpdateVehicleError
<a name="API_UpdateVehicleError"></a>

An HTTP error resulting from updating the description for a vehicle.

## Contents
<a name="API_UpdateVehicleError_Contents"></a>

 ** code **   <a name="iotfleetwise-Type-UpdateVehicleError-code"></a>
The relevant HTTP error code (400\+).
Type: Integer
Required: No

 ** message **   <a name="iotfleetwise-Type-UpdateVehicleError-message"></a>
A message associated with the error.
Type: String
Required: No

 ** vehicleName **   <a name="iotfleetwise-Type-UpdateVehicleError-vehicleName"></a>
The ID of the vehicle with the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

## See Also
<a name="API_UpdateVehicleError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateVehicleError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateVehicleError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateVehicleError)
