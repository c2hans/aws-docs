---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartBulkAssociateWirelessDeviceWithMulticastGroup.html
---

# StartBulkAssociateWirelessDeviceWithMulticastGroup
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup"></a>

Starts a bulk association of all qualifying wireless devices with a multicast group.

## Request Syntax
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestSyntax"></a>

```
PATCH /multicast-groups/{{Id}}/bulk HTTP/1.1
Content-type: application/json

{
   "QueryString": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestSyntax) **   <a name="iotwireless-StartBulkAssociateWirelessDeviceWithMulticastGroup-request-uri-Id"></a>
The ID of the multicast group.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [QueryString](#API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestSyntax) **   <a name="iotwireless-StartBulkAssociateWirelessDeviceWithMulticastGroup-request-QueryString"></a>
Query string used to search for wireless devices as part of the bulk associate and disassociate process.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [Tags](#API_StartBulkAssociateWirelessDeviceWithMulticastGroup_RequestSyntax) **   <a name="iotwireless-StartBulkAssociateWirelessDeviceWithMulticastGroup-request-Tags"></a>
The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_Errors"></a>

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
<a name="API_StartBulkAssociateWirelessDeviceWithMulticastGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/StartBulkAssociateWirelessDeviceWithMulticastGroup)
