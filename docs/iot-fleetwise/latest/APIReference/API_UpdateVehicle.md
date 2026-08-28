---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateVehicle.html
---

# UpdateVehicle
<a name="API_UpdateVehicle"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Updates a vehicle.

## Request Syntax
<a name="API_UpdateVehicle_RequestSyntax"></a>

```
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
```

## Request Parameters
<a name="API_UpdateVehicle_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attributes](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-attributes"></a>
Static information about a vehicle in a key-value pair. For example:
 `"engineType"` : `"1.3 L R2"`
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 150.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** [attributeUpdateMode](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-attributeUpdateMode"></a>
The method the specified attributes will update the existing attributes on the vehicle. Use`Overwite` to replace the vehicle attributes with the specified attributes. Or use `Merge` to combine all attributes.
This is required if attributes are present in the input.
Type: String
Valid Values: `Overwrite | Merge`
Required: No

 ** [decoderManifestArn](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-decoderManifestArn"></a>
The ARN of the decoder manifest associated with this vehicle.
Type: String
Required: No

 ** [modelManifestArn](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-modelManifestArn"></a>
The ARN of a vehicle model (model manifest) associated with the vehicle.
Type: String
Required: No

 ** [stateTemplatesToAdd](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-stateTemplatesToAdd"></a>
Associate state templates with the vehicle.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [stateTemplatesToRemove](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-stateTemplatesToRemove"></a>
Remove state templates from the vehicle.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

 ** [stateTemplatesToUpdate](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-stateTemplatesToUpdate"></a>
Change the `stateTemplateUpdateStrategy` of state templates already associated with the vehicle.
Type: Array of [StateTemplateAssociation](API_StateTemplateAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [vehicleName](#API_UpdateVehicle_RequestSyntax) **   <a name="iotfleetwise-UpdateVehicle-request-vehicleName"></a>
The unique ID of the vehicle to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_UpdateVehicle_ResponseSyntax"></a>

```
{
   "arn": "string",
   "vehicleName": "string"
}
```

## Response Elements
<a name="API_UpdateVehicle_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateVehicle_ResponseSyntax) **   <a name="iotfleetwise-UpdateVehicle-response-arn"></a>
The ARN of the updated vehicle.
Type: String

 ** [vehicleName](#API_UpdateVehicle_ResponseSyntax) **   <a name="iotfleetwise-UpdateVehicle-response-vehicleName"></a>
The ID of the updated vehicle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_UpdateVehicle_Errors"></a>

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
<a name="API_UpdateVehicle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/UpdateVehicle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/UpdateVehicle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
