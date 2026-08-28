---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListDiscoveredDevices.html
---

# ListDiscoveredDevices
<a name="API_ListDiscoveredDevices"></a>

Lists all devices discovered during a specific device discovery task.

## Request Syntax
<a name="API_ListDiscoveredDevices_RequestSyntax"></a>

```
GET /device-discoveries/{{Identifier}}/devices?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDiscoveredDevices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_ListDiscoveredDevices_RequestSyntax) **   <a name="managedintegrations-ListDiscoveredDevices-request-uri-Identifier"></a>
The identifier of the device discovery job to list discovered devices for.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[A-Za-z0-9]+`
Required: Yes

 ** [MaxResults](#API_ListDiscoveredDevices_RequestSyntax) **   <a name="managedintegrations-ListDiscoveredDevices-request-uri-MaxResults"></a>
The maximum number of discovered devices to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDiscoveredDevices_RequestSyntax) **   <a name="managedintegrations-ListDiscoveredDevices-request-uri-NextToken"></a>
A token used for pagination of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Request Body
<a name="API_ListDiscoveredDevices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDiscoveredDevices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AuthenticationMaterial": "string",
         "Brand": "string",
         "ConnectorDeviceId": "string",
         "ConnectorDeviceName": "string",
         "DeviceTypes": [ "string" ],
         "DiscoveredAt": number,
         "ManagedThingId": "string",
         "Model": "string",
         "Modification": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDiscoveredDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDiscoveredDevices_ResponseSyntax) **   <a name="managedintegrations-ListDiscoveredDevices-response-Items"></a>
The list of discovered devices that match the specified criteria.
Type: Array of [DiscoveredDeviceSummary](API_DiscoveredDeviceSummary.md) objects

 ** [NextToken](#API_ListDiscoveredDevices_ResponseSyntax) **   <a name="managedintegrations-ListDiscoveredDevices-response-NextToken"></a>
A token used for pagination of results when there are more discovered devices than can be returned in a single response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListDiscoveredDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** UnauthorizedException **
You are not authorized to perform this operation.
HTTP Status Code: 401

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListDiscoveredDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListDiscoveredDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
