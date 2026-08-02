---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateVehicle.html
---

# CreateVehicle
<a name="API_CreateVehicle"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Creates a vehicle, which is an instance of a vehicle model (model manifest). Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.

**Note**
 If you have an existing AWS IoT thing, you can use AWS IoT FleetWise to create a vehicle and collect data from your thing.

For more information, see [Create a vehicle (AWS CLI)](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-cli.html) in the * AWS IoT FleetWise Developer Guide*.

## Request Syntax
<a name="API_CreateVehicle_RequestSyntax"></a>

```
{
   "associationBehavior": "{{string}}",
   "attributes": {
      "{{string}}" : "{{string}}"
   },
   "decoderManifestArn": "{{string}}",
   "modelManifestArn": "{{string}}",
   "stateTemplates": [
      {
         "identifier": "{{string}}",
         "stateTemplateUpdateStrategy": { ... }
      }
   ],
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "vehicleName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVehicle_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [associationBehavior](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-associationBehavior"></a>
 An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing AWS IoT thing as a vehicle.
Default: ``
Type: String
Valid Values: `CreateIotThing | ValidateIotThingExists`
Required: No

 ** [attributes](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-attributes"></a>
Static information about a vehicle in a key-value pair. For example: `"engineType"` : `"1.3 L R2"`
To use attributes with Campaigns or State Templates, you must include them using the request parameters `dataExtraDimensions` and/or `metadataExtraDimensions` (for state templates only) when creating your campaign/state template.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 150.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [decoderManifestArn](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-decoderManifestArn"></a>
 The ARN of a decoder manifest.
Type: String
Required: Yes

 ** [modelManifestArn](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-modelManifestArn"></a>
 The Amazon Resource Name ARN of a vehicle model.
Type: String
Required: Yes

 ** [stateTemplates](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-stateTemplates"></a>
Associate state templates with the vehicle. You can monitor the last known state of the vehicle in near real time.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [tags](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-tags"></a>
Metadata that can be used to manage the vehicle.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [vehicleName](#API_CreateVehicle_RequestSyntax) **   <a name="iotfleetwise-CreateVehicle-request-vehicleName"></a>
 The unique ID of the vehicle to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_CreateVehicle_ResponseSyntax"></a>

```
{
   "arn": "string",
   "thingArn": "string",
   "vehicleName": "string"
}
```

## Response Elements
<a name="API_CreateVehicle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateVehicle_ResponseSyntax) **   <a name="iotfleetwise-CreateVehicle-response-arn"></a>
 The ARN of the created vehicle.
Type: String

 ** [thingArn](#API_CreateVehicle_ResponseSyntax) **   <a name="iotfleetwise-CreateVehicle-response-thingArn"></a>
 The ARN of a created or validated AWS IoT thing.
Type: String

 ** [vehicleName](#API_CreateVehicle_ResponseSyntax) **   <a name="iotfleetwise-CreateVehicle-response-vehicleName"></a>
The unique ID of the created vehicle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_CreateVehicle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
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

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
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
<a name="API_CreateVehicle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/CreateVehicle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateVehicle)
