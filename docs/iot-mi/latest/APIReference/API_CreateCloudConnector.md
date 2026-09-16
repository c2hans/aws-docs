---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateCloudConnector.html
---

# CreateCloudConnector
<a name="API_CreateCloudConnector"></a>

Creates a C2C (cloud-to-cloud) connector.

## Request Syntax
<a name="API_CreateCloudConnector_RequestSyntax"></a>

```
POST /cloud-connectors HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "EndpointConfig": {
      "lambda": {
         "arn": "{{string}}"
      }
   },
   "EndpointType": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCloudConnector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCloudConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateCloudConnector_RequestSyntax) **   <a name="managedintegrations-CreateCloudConnector-request-ClientToken"></a>
An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9=_-]+`
Required: No

 ** [Description](#API_CreateCloudConnector_RequestSyntax) **   <a name="managedintegrations-CreateCloudConnector-request-Description"></a>
A description of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** [EndpointConfig](#API_CreateCloudConnector_RequestSyntax) **   <a name="managedintegrations-CreateCloudConnector-request-EndpointConfig"></a>
The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.
Type: [EndpointConfig](API_EndpointConfig.md) object
Required: Yes

 ** [EndpointType](#API_CreateCloudConnector_RequestSyntax) **   <a name="managedintegrations-CreateCloudConnector-request-EndpointType"></a>
The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.
Type: String
Valid Values: `LAMBDA`
Required: No

 ** [Name](#API_CreateCloudConnector_RequestSyntax) **   <a name="managedintegrations-CreateCloudConnector-request-Name"></a>
The display name of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: Yes

## Response Syntax
<a name="API_CreateCloudConnector_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_CreateCloudConnector_ResponseSyntax) **   <a name="managedintegrations-CreateCloudConnector-response-Id"></a>
The unique identifier assigned to the newly created cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

## Errors
<a name="API_CreateCloudConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict with the request.
HTTP Status Code: 409

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_CreateCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/CreateCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CreateCloudConnector)
