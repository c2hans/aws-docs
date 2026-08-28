---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessGateway.html
---

# UpdateWirelessGateway
<a name="API_UpdateWirelessGateway"></a>

Updates properties of a wireless gateway.

## Request Syntax
<a name="API_UpdateWirelessGateway_RequestSyntax"></a>

```
PATCH /wireless-gateways/{{Id}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "JoinEuiFilters": [
      [ "{{string}}" ]
   ],
   "MaxEirp": {{number}},
   "Name": "{{string}}",
   "NetIdFilters": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateWirelessGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-uri-Id"></a>
The ID of the resource to update.
Length Constraints: Maximum length of 256.
Required: Yes

## Request Body
<a name="API_UpdateWirelessGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-Description"></a>
A new description of the resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** [JoinEuiFilters](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-JoinEuiFilters"></a>
A list of JoinEuiRange used by LoRa gateways to filter LoRa frames.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Array Members: Fixed number of 2 items.
Pattern: `[a-fA-F0-9]{16}`
Required: No

 ** [MaxEirp](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-MaxEirp"></a>
The MaxEIRP value.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 30.
Required: No

 ** [Name](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-Name"></a>
The new name of the resource.
The following special characters aren't accepted: `<>^#~$`
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [NetIdFilters](#API_UpdateWirelessGateway_RequestSyntax) **   <a name="iotwireless-UpdateWirelessGateway-request-NetIdFilters"></a>
A list of NetId values that are used by LoRa gateways to filter the uplink frames.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `[a-fA-F0-9]{6}`
Required: No

## Response Syntax
<a name="API_UpdateWirelessGateway_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateWirelessGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateWirelessGateway_Errors"></a>

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
<a name="API_UpdateWirelessGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/UpdateWirelessGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateWirelessGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
