---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateMulticastGroup.html
---

# CreateMulticastGroup
<a name="API_CreateMulticastGroup"></a>

Creates a multicast group.

## Request Syntax
<a name="API_CreateMulticastGroup_RequestSyntax"></a>

```
POST /multicast-groups HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "LoRaWAN": {
      "DefaultSessionParameters": {
         "DlDr": {{number}},
         "DlFreq": {{number}}
      },
      "DlClass": "{{string}}",
      "ParticipatingGateways": {
         "GatewayList": [ "{{string}}" ],
         "TransmissionInterval": {{number}}
      },
      "RfRegion": "{{string}}"
   },
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMulticastGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMulticastGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateMulticastGroup_RequestSyntax) **   <a name="iotwireless-CreateMulticastGroup-request-ClientRequestToken"></a>
Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Description](#API_CreateMulticastGroup_RequestSyntax) **   <a name="iotwireless-CreateMulticastGroup-request-Description"></a>
The description of the multicast group.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [LoRaWAN](#API_CreateMulticastGroup_RequestSyntax) **   <a name="iotwireless-CreateMulticastGroup-request-LoRaWAN"></a>
The LoRaWAN information that is to be used with the multicast group.
Type: [LoRaWANMulticast](API_LoRaWANMulticast.md) object
Required: Yes

 ** [Name](#API_CreateMulticastGroup_RequestSyntax) **   <a name="iotwireless-CreateMulticastGroup-request-Name"></a>
The name of the multicast group.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [Tags](#API_CreateMulticastGroup_RequestSyntax) **   <a name="iotwireless-CreateMulticastGroup-request-Tags"></a>
The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateMulticastGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateMulticastGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateMulticastGroup_ResponseSyntax) **   <a name="iotwireless-CreateMulticastGroup-response-Arn"></a>
The arn of the multicast group.
Type: String
Length Constraints: Maximum length of 128.

 ** [Id](#API_CreateMulticastGroup_ResponseSyntax) **   <a name="iotwireless-CreateMulticastGroup-response-Id"></a>
The ID of the multicast group.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_CreateMulticastGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_CreateMulticastGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/CreateMulticastGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/CreateMulticastGroup)
