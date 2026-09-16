---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_BatchUpdateVehicle.html
---

# BatchUpdateVehicle
<a name="API_BatchUpdateVehicle"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Updates a group, or batch, of vehicles.

**Note**
 You must specify a decoder manifest and a vehicle model (model manifest) for each vehicle.

For more information, see [Update multiple vehicles (AWS CLI)](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html) in the * AWS IoT FleetWise Developer Guide*.

## Request Syntax
<a name="API_BatchUpdateVehicle_RequestSyntax"></a>

```
{
   "vehicles": [
      {
         "attributes": {
            "{{string}}" : "{{string}}"
         },
         "attributeUpdateMode": "{{string}}",
         "decoderManifestArn": "{{string}}",
         "modelManifestArn": "{{string}}",
         "stateTemplatesToAdd": [
            {
               "identifier": "{{string}}",
               "stateTemplateUpdateStrategy": { ... }
            }
         ],
         "stateTemplatesToRemove": [ "{{string}}" ],
         "stateTemplatesToUpdate": [
            {
               "identifier": "{{string}}",
               "stateTemplateUpdateStrategy": { ... }
            }
         ],
         "vehicleName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BatchUpdateVehicle_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [vehicles](#API_BatchUpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-BatchUpdateVehicle-request-vehicles"></a>
 A list of information about the vehicles to update. For more information, see the [UpdateVehicleRequestItem](API_UpdateVehicleRequestItem.md) API data type.
Type: Array of [UpdateVehicleRequestItem](API_UpdateVehicleRequestItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_BatchUpdateVehicle_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": number,
         "message": "string",
         "vehicleName": "string"
      }
   ],
   "vehicles": [
      {
         "arn": "string",
         "vehicleName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUpdateVehicle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchUpdateVehicle_ResponseSyntax) **   <a name="iotfleetwise-BatchUpdateVehicle-response-errors"></a>
A list of information about errors returned while updating a batch of vehicles, or, if there aren't any errors, an empty list.
Type: Array of [UpdateVehicleError](API_UpdateVehicleError.md) objects

 ** [vehicles](#API_BatchUpdateVehicle_ResponseSyntax) **   <a name="iotfleetwise-BatchUpdateVehicle-response-vehicles"></a>
 A list of information about the batch of updated vehicles.
This list contains only unique IDs for the vehicles that were updated.
Type: Array of [UpdateVehicleResponseItem](API_UpdateVehicleResponseItem.md) objects

## Errors
<a name="API_BatchUpdateVehicle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** LimitExceededException **
A service quota was exceeded.
 ** resourceId **
The identifier of the resource that was exceeded.
 ** resourceType **
The type of resource that was exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_BatchUpdateVehicle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/BatchUpdateVehicle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/BatchUpdateVehicle)
