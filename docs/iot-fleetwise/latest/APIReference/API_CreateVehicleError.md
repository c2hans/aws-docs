---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicleError.html
---

# CreateVehicleError
<a name="API_CreateVehicleError"></a>

An HTTP error resulting from creating a vehicle.

## Contents
<a name="API_CreateVehicleError_Contents"></a>

 ** code **   <a name="iotfleetwise-Type-CreateVehicleError-code"></a>
An HTTP error code.
Type: String
Required: No

 ** message **   <a name="iotfleetwise-Type-CreateVehicleError-message"></a>
A description of the HTTP error.
Type: String
Required: No

 ** vehicleName **   <a name="iotfleetwise-Type-CreateVehicleError-vehicleName"></a>
The ID of the vehicle with the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

## See Also
<a name="API_CreateVehicleError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateVehicleError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateVehicleError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateVehicleError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
