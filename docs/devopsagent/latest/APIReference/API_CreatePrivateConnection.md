---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreatePrivateConnection.html
---

# CreatePrivateConnection
<a name="API_CreatePrivateConnection"></a>

Creates a Private Connection to a target resource.

## Request Syntax
<a name="API_CreatePrivateConnection_RequestSyntax"></a>

```
POST /v1/private-connections HTTP/1.1
Content-type: application/json

{
   "mode": { ... },
   "name": "{{string}}",
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

 ** [mode](#API_CreatePrivateConnection_RequestSyntax) **   <a name="devopsagent-CreatePrivateConnection-request-mode"></a>
Private Connection mode configuration.
Type: [PrivateConnectionMode](API_PrivateConnectionMode.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreatePrivateConnection_RequestSyntax) **   <a name="devopsagent-CreatePrivateConnection-request-name"></a>
Unique name for this Private Connection within the account.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** [tags](#API_CreatePrivateConnection_RequestSyntax) **   <a name="devopsagent-CreatePrivateConnection-request-tags"></a>
Tags to add to the Private Connection at creation time.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Required: No

## Response Syntax
<a name="API_CreatePrivateConnection_ResponseSyntax"></a>

```
HTTP/1.1 200
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

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateExpiryTime](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-certificateExpiryTime"></a>
The expiry time of the certificate associated with the Private Connection. Only present when a certificate is associated.
Type: Timestamp

 ** [dnsResolution](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-dnsResolution"></a>
DNS resolution mode for the Private Connection's resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`

 ** [failureMessage](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-failureMessage"></a>
Message describing the reason for a failed Private Connection creation, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [hostAddress](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-hostAddress"></a>
IP address or DNS name of the target resource. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.:\-]+`

 ** [name](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-name"></a>
The name of the Private Connection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`

 ** [resourceConfigurationId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-resourceConfigurationId"></a>
The Resource Configuration ARN. Only present for self-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}|rcfg-[0-9a-z]{17})`

 ** [resourceGatewayId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-resourceGatewayId"></a>
The service-managed Resource Gateway ARN. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`

 ** [status](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-status"></a>
The status of the Private Connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [tags](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-tags"></a>
Tags associated with the created Private Connection.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

 ** [type](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-type"></a>
The type of the Private Connection.
Type: String
Valid Values: `SELF_MANAGED | SERVICE_MANAGED`

 ** [vpcId](#API_CreatePrivateConnection_ResponseSyntax) **   <a name="devopsagent-CreatePrivateConnection-response-vpcId"></a>
VPC identifier of the service-managed Resource Gateway. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Errors
<a name="API_CreatePrivateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreatePrivateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/CreatePrivateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/CreatePrivateConnection)
