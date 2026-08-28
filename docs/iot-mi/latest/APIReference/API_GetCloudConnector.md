---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetCloudConnector.html
---

# GetCloudConnector
<a name="API_GetCloudConnector"></a>

Get configuration details for a cloud connector.

## Request Syntax
<a name="API_GetCloudConnector_RequestSyntax"></a>

```
GET /cloud-connectors/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCloudConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_GetCloudConnector_RequestSyntax) **   <a name="managedintegrations-GetCloudConnector-request-uri-Identifier"></a>
The identifier of the C2C connector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetCloudConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCloudConnector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Description": "string",
   "EndpointConfig": {
      "lambda": {
         "arn": "string"
      }
   },
   "EndpointType": "string",
   "Id": "string",
   "Name": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_GetCloudConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-Description"></a>
A description of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`

 ** [EndpointConfig](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-EndpointConfig"></a>
The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.
Type: [EndpointConfig](API_EndpointConfig.md) object

 ** [EndpointType](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-EndpointType"></a>
The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.
Type: String
Valid Values: `LAMBDA`

 ** [Id](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-Id"></a>
The unique identifier of the cloud connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`

 ** [Name](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-Name"></a>
The display name of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`

 ** [Type](#API_GetCloudConnector_ResponseSyntax) **   <a name="managedintegrations-GetCloudConnector-response-Type"></a>
The type of cloud connector created.
Type: String
Valid Values: `LISTED | UNLISTED`

## Errors
<a name="API_GetCloudConnector_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetCloudConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/GetCloudConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/GetCloudConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
