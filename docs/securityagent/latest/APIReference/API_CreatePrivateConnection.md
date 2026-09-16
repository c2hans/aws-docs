---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreatePrivateConnection.html
---

# CreatePrivateConnection
<a name="API_CreatePrivateConnection"></a>

Creates a private connection for reaching a self-hosted provider instance over private networking using Amazon VPC Lattice.

## Request Syntax
<a name="API_CreatePrivateConnection_RequestSyntax"></a>

```
POST /CreatePrivateConnection HTTP/1.1
Content-type: application/json

{
   "mode": { ... },
   "privateConnectionName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePrivateConnection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePrivateConnection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [mode](#API_CreatePrivateConnection_RequestSyntax) **   <a name="securityagent-CreatePrivateConnection-request-mode"></a>
The configuration for the private connection. Specify either a service-managed or a self-managed mode.
Type: [PrivateConnectionMode](API_PrivateConnectionMode.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [privateConnectionName](#API_CreatePrivateConnection_RequestSyntax) **   <a name="securityagent-CreatePrivateConnection-request-privateConnectionName"></a>
A unique name for the private connection within your account.
Type: String
Required: Yes

 ** [tags](#API_CreatePrivateConnection_RequestSyntax) **   <a name="securityagent-CreatePrivateConnection-request-tags"></a>
The tags to attach to the private connection.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreatePrivateConnection_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "certificateExpiryTime": "string",
   "dnsResolution": "string",
   "failureMessage": "string",
   "hostAddress": "string",
   "name": "string",
   "resourceConfigurationId": "string",
   "resourceGatewayId": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "type": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_CreatePrivateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [certificateExpiryTime](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-certificateExpiryTime"></a>
The date and time the connection's certificate expires, in UTC format.
Type: Timestamp

 ** [dnsResolution](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-dnsResolution"></a>
The DNS resolution mode for the resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`

 ** [failureMessage](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-failureMessage"></a>
A message describing why the private connection entered a failed state, if applicable.
Type: String

 ** [hostAddress](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-hostAddress"></a>
The IP address or DNS name of the target resource.
Type: String

 ** [name](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-name"></a>
The name of the private connection.
Type: String

 ** [resourceConfigurationId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-resourceConfigurationId"></a>
The identifier or ARN of the VPC Lattice resource configuration.
Type: String

 ** [resourceGatewayId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-resourceGatewayId"></a>
The identifier or ARN of the VPC Lattice resource gateway.
Type: String

 ** [status](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-status"></a>
The current status of the private connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [tags](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-tags"></a>
The tags attached to the private connection.
Type: String to string map

 ** [type](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-type"></a>
The type of the private connection, indicating whether it is service-managed or self-managed.
Type: String
Valid Values: `SERVICE_MANAGED | SELF_MANAGED`

 ** [vpcId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="securityagent-CreatePrivateConnection-response-vpcId"></a>
The identifier of the VPC the resource gateway is created in.
Type: String

## Errors
<a name="API_CreatePrivateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** message **
Error description.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
 ** message **
Error description.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
 ** message **
Error description.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.
 ** message **
Error description.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** message **
Error description.
 ** quotaCode **
Quota code for throttling limit.
 ** serviceCode **
Service code for throttling limit.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered during validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreatePrivateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreatePrivateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreatePrivateConnection)
