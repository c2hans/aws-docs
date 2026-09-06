---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateStateTemplate.html
---

# CreateStateTemplate
<a name="API_CreateStateTemplate"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Creates a state template. State templates contain state properties, which are signals that belong to a signal catalog that is synchronized between the AWS IoT FleetWise Edge and the AWS Cloud.

## Request Syntax
<a name="API_CreateStateTemplate_RequestSyntax"></a>

```
{
   "dataExtraDimensions": [ "{{string}}" ],
   "description": "{{string}}",
   "metadataExtraDimensions": [ "{{string}}" ],
   "name": "{{string}}",
   "signalCatalogArn": "{{string}}",
   "stateTemplateProperties": [ "{{string}}" ],
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStateTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dataExtraDimensions](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-dataExtraDimensions"></a>
A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See [ Processing last known state vehicle data using MQTT messaging](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data)). For example, if you add `Vehicle.Attributes.Make` and `Vehicle.Attributes.Model` attributes, AWS IoT FleetWise will enrich the protobuf encoded payload with those attributes in the `extraDimensions` field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [description](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-description"></a>
A brief description of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [metadataExtraDimensions](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-metadataExtraDimensions"></a>
A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See [ Processing last known state vehicle data using MQTT messaging](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data)). For example, if you add `Vehicle.Attributes.Make` and `Vehicle.Attributes.Model` attributes, AWS IoT FleetWise will include these attributes as User Properties with the MQTT message.
Default: An empty array
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [name](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-name"></a>
The name of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [signalCatalogArn](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-signalCatalogArn"></a>
The ARN of the signal catalog associated with the state template.
Type: String
Required: Yes

 ** [stateTemplateProperties](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-stateTemplateProperties"></a>
A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** [tags](#API_CreateStateTemplate_RequestSyntax) **   <a name="iotfleetwise-CreateStateTemplate-request-tags"></a>
Metadata that can be used to manage the state template.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateStateTemplate_ResponseSyntax"></a>

```
{
   "arn": "string",
   "id": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateStateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-CreateStateTemplate-response-arn"></a>
The Amazon Resource Name (ARN) of the state template.
Type: String

 ** [id](#API_CreateStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-CreateStateTemplate-response-id"></a>
The unique ID of the state template.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[A-Z0-9]+`

 ** [name](#API_CreateStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-CreateStateTemplate-response-name"></a>
The name of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_CreateStateTemplate_Errors"></a>

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

 ** InvalidSignalsException **
The request couldn't be completed because it contains signals that aren't valid.
 ** invalidSignals **
The signals which caused the exception.
HTTP Status Code: 400

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
<a name="API_CreateStateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/CreateStateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateStateTemplate)
