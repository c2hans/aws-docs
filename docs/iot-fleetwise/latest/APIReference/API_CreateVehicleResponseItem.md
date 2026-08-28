---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicleResponseItem.html
---

# CreateVehicleResponseItem
<a name="API_CreateVehicleResponseItem"></a>

Information about a created vehicle.

## Contents
<a name="API_CreateVehicleResponseItem_Contents"></a>

 ** arn **   <a name="iotfleetwise-Type-CreateVehicleResponseItem-arn"></a>
The ARN of the created vehicle.
Type: String
Required: No

 ** thingArn **   <a name="iotfleetwise-Type-CreateVehicleResponseItem-thingArn"></a>
The ARN of a created or validated AWS IoT thing.
Type: String
Required: No

 ** vehicleName **   <a name="iotfleetwise-Type-CreateVehicleResponseItem-vehicleName"></a>
The unique ID of the vehicle to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

## See Also
<a name="API_CreateVehicleResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateVehicleResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateVehicleResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateVehicleResponseItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
