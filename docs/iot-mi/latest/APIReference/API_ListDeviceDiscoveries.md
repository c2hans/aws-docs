---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListDeviceDiscoveries.html
---

# ListDeviceDiscoveries
<a name="API_ListDeviceDiscoveries"></a>

Lists all device discovery tasks, with optional filtering by type and status.

## Request Syntax
<a name="API_ListDeviceDiscoveries_RequestSyntax"></a>

```
GET /device-discoveries?MaxResults={{MaxResults}}&NextToken={{NextToken}}&StatusFilter={{StatusFilter}}&TypeFilter={{TypeFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDeviceDiscoveries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDeviceDiscoveries_RequestSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-request-uri-MaxResults"></a>
The maximum number of device discovery jobs to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDeviceDiscoveries_RequestSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-request-uri-NextToken"></a>
A token used for pagination of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

 ** [StatusFilter](#API_ListDeviceDiscoveries_RequestSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-request-uri-StatusFilter"></a>
The status to filter device discovery jobs by.
Valid Values: `RUNNING | SUCCEEDED | FAILED | TIMED_OUT`

 ** [TypeFilter](#API_ListDeviceDiscoveries_RequestSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-request-uri-TypeFilter"></a>
The discovery type to filter device discovery jobs by.
Valid Values: `ZWAVE | ZIGBEE | CLOUD | CUSTOM | CONTROLLER_CAPABILITY_REDISCOVERY`

## Request Body
<a name="API_ListDeviceDiscoveries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDeviceDiscoveries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "DiscoveryType": "string",
         "Id": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDeviceDiscoveries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDeviceDiscoveries_ResponseSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-response-Items"></a>
The list of device discovery jobs that match the specified criteria.
Type: Array of [DeviceDiscoverySummary](API_DeviceDiscoverySummary.md) objects

 ** [NextToken](#API_ListDeviceDiscoveries_ResponseSyntax) **   <a name="managedintegrations-ListDeviceDiscoveries-response-NextToken"></a>
A token used for pagination of results when there are more device discovery jobs than can be returned in a single response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Errors
<a name="API_ListDeviceDiscoveries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

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
<a name="API_ListDeviceDiscoveries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListDeviceDiscoveries)
