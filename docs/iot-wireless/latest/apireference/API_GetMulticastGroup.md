---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetMulticastGroup.html
---

# GetMulticastGroup
<a name="API_GetMulticastGroup"></a>

Gets information about a multicast group.

## Request Syntax
<a name="API_GetMulticastGroup_RequestSyntax"></a>

```
GET /multicast-groups/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMulticastGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetMulticastGroup_RequestSyntax) **   <a name="iotwireless-GetMulticastGroup-request-uri-Id"></a>
The ID of the multicast group.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_GetMulticastGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMulticastGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "CreatedAt": number,
   "Description": "string",
   "Id": "string",
   "LoRaWAN": {
      "DefaultSessionParameters": {
         "DlDr": number,
         "DlFreq": number
      },
      "DlClass": "string",
      "NumberOfDevicesInGroup": number,
      "NumberOfDevicesRequested": number,
      "ParticipatingGateways": {
         "GatewayList": [ "string" ],
         "TransmissionInterval": number
      },
      "RfRegion": "string"
   },
   "Name": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetMulticastGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-Arn"></a>
The arn of the multicast group.
Type: String
Length Constraints: Maximum length of 128.

 ** [CreatedAt](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-CreatedAt"></a>
Created at timestamp for the resource.
Type: Timestamp

 ** [Description](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-Description"></a>
The description of the new resource.
Type: String
Length Constraints: Maximum length of 2048.

 ** [Id](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-Id"></a>
The ID of the multicast group.
Type: String
Length Constraints: Maximum length of 256.

 ** [LoRaWAN](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-LoRaWAN"></a>
The LoRaWAN information that is to be returned from getting multicast group information.
Type: [LoRaWANMulticastGet](API_LoRaWANMulticastGet.md) object

 ** [Name](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-Name"></a>
The name of the multicast group.
Type: String
Length Constraints: Maximum length of 256.

 ** [Status](#API_GetMulticastGroup_ResponseSyntax) **   <a name="iotwireless-GetMulticastGroup-response-Status"></a>
The status of the multicast group.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetMulticastGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

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
<a name="API_GetMulticastGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/GetMulticastGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GetMulticastGroup)
