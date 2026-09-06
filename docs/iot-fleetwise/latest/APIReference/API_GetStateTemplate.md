---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetStateTemplate.html
---

# GetStateTemplate
<a name="API_GetStateTemplate"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Retrieves information about a state template.

## Request Syntax
<a name="API_GetStateTemplate_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetStateTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_GetStateTemplate_RequestSyntax) **   <a name="iotfleetwise-GetStateTemplate-request-identifier"></a>
The unique ID of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_GetStateTemplate_ResponseSyntax"></a>

```
{
   "arn": "string",
   "creationTime": number,
   "dataExtraDimensions": [ "string" ],
   "description": "string",
   "id": "string",
   "lastModificationTime": number,
   "metadataExtraDimensions": [ "string" ],
   "name": "string",
   "signalCatalogArn": "string",
   "stateTemplateProperties": [ "string" ]
}
```

## Response Elements
<a name="API_GetStateTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-arn"></a>
The Amazon Resource Name (ARN) of the state template.
Type: String

 ** [creationTime](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-creationTime"></a>
The time the state template was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [dataExtraDimensions](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-dataExtraDimensions"></a>
A list of vehicle attributes associated with the payload published on the state template's MQTT topic.
Default: An empty array
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`

 ** [description](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-description"></a>
A brief description of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [id](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-id"></a>
The unique ID of the state template.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[A-Z0-9]+`

 ** [lastModificationTime](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-lastModificationTime"></a>
The time the state template was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [metadataExtraDimensions](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-metadataExtraDimensions"></a>
A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic.
Default: An empty array
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`

 ** [name](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-name"></a>
The name of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

 ** [signalCatalogArn](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-signalCatalogArn"></a>
The ARN of the signal catalog associated with the state template.
Type: String

 ** [stateTemplateProperties](#API_GetStateTemplate_ResponseSyntax) **   <a name="iotfleetwise-GetStateTemplate-response-stateTemplateProperties"></a>
A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`

## Errors
<a name="API_GetStateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

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
<a name="API_GetStateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetStateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetStateTemplate)
