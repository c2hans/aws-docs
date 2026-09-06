---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicleRequestItem.html
---

# CreateVehicleRequestItem
<a name="API_CreateVehicleRequestItem"></a>

Information about the vehicle to create.

## Contents
<a name="API_CreateVehicleRequestItem_Contents"></a>

 ** decoderManifestArn **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-decoderManifestArn"></a>
The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.
Type: String
Required: Yes

 ** modelManifestArn **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-modelManifestArn"></a>
The ARN of the vehicle model (model manifest) to create the vehicle from.
Type: String
Required: Yes

 ** vehicleName **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-vehicleName"></a>
The unique ID of the vehicle to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** associationBehavior **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-associationBehavior"></a>
An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.
Type: String
Valid Values: `CreateIotThing | ValidateIotThingExists`
Required: No

 ** attributes **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-attributes"></a>
Static information about a vehicle in a key-value pair. For example: `"engine Type"` : `"v6"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 150.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** stateTemplates **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-stateTemplates"></a>
Associate state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** tags **   <a name="iotfleetwise-Type-CreateVehicleRequestItem-tags"></a>
Metadata which can be used to manage the vehicle.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_CreateVehicleRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateVehicleRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateVehicleRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateVehicleRequestItem)
