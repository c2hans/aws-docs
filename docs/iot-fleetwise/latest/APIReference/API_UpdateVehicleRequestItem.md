---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateVehicleRequestItem.html
---

# UpdateVehicleRequestItem
<a name="API_UpdateVehicleRequestItem"></a>

Information about the vehicle to update.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_UpdateVehicleRequestItem_Contents"></a>

 ** vehicleName **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-vehicleName"></a>
The unique ID of the vehicle to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** attributes **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-attributes"></a>
Static information about a vehicle in a key-value pair. For example:
 `"engineType"` : `"1.3 L R2"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 150.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** attributeUpdateMode **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-attributeUpdateMode"></a>
The method the specified attributes will update the existing attributes on the vehicle. Use`Overwite` to replace the vehicle attributes with the specified attributes. Or use `Merge` to combine all attributes.
This is required if attributes are present in the input.
Type: String
Valid Values: `Overwrite | Merge`
Required: No

 ** decoderManifestArn **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-decoderManifestArn"></a>
The ARN of the signal decoder manifest associated with the vehicle to update.
Type: String
Required: No

 ** modelManifestArn **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-modelManifestArn"></a>
The ARN of the vehicle model (model manifest) associated with the vehicle to update.
Type: String
Required: No

 ** stateTemplatesToAdd **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-stateTemplatesToAdd"></a>
Associate additional state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** stateTemplatesToRemove **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-stateTemplatesToRemove"></a>
Remove existing state template associations from the vehicle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

 ** stateTemplatesToUpdate **   <a name="iotfleetwise-Type-UpdateVehicleRequestItem-stateTemplatesToUpdate"></a>
Change the `stateTemplateUpdateStrategy` of state templates already associated with the vehicle.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_UpdateVehicleRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateVehicleRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateVehicleRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateVehicleRequestItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
