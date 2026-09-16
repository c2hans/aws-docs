---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdatePrivateConnectionCertificate.html
---

# UpdatePrivateConnectionCertificate
<a name="API_UpdatePrivateConnectionCertificate"></a>

Updates the certificate associated with a Private Connection.

## Request Syntax
<a name="API_UpdatePrivateConnectionCertificate_RequestSyntax"></a>

```
POST /v1/private-connections/{{name}}/certificate HTTP/1.1
Content-type: application/json

{
   "certificate": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePrivateConnectionCertificate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdatePrivateConnectionCertificate_RequestSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-request-uri-name"></a>
The name of the Private Connection.
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: Yes

## Request Body
<a name="API_UpdatePrivateConnectionCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificate](#API_UpdatePrivateConnectionCertificate_RequestSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-request-certificate"></a>
The new certificate for the Private Connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: Yes

## Response Syntax
<a name="API_UpdatePrivateConnectionCertificate_ResponseSyntax"></a>

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
   "type": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_UpdatePrivateConnectionCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateExpiryTime](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-certificateExpiryTime"></a>
The expiry time of the certificate associated with the Private Connection. Only present when a certificate is associated.
Type: Timestamp

 ** [dnsResolution](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-dnsResolution"></a>
DNS resolution mode for the Private Connection's resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`

 ** [failureMessage](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-failureMessage"></a>
Message describing the reason for a failed Private Connection update, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [hostAddress](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-hostAddress"></a>
IP address or DNS name of the target resource. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9.:\-]+`

 ** [name](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-name"></a>
The name of the Private Connection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z0-9]([a-z0-9-]*[a-z0-9])?`

 ** [resourceConfigurationId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-resourceConfigurationId"></a>
The Resource Configuration ARN. Only present for self-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}|rcfg-[0-9a-z]{17})`

 ** [resourceGatewayId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-resourceGatewayId"></a>
The service-managed Resource Gateway ARN. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`

 ** [status](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-status"></a>
The status of the Private Connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [type](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-type"></a>
The type of the Private Connection.
Type: String
Valid Values: `SELF_MANAGED | SERVICE_MANAGED`

 ** [vpcId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="devopsagent-UpdatePrivateConnectionCertificate-response-vpcId"></a>
VPC identifier of the service-managed Resource Gateway. Only present for service-managed Private Connections.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`

## Errors
<a name="API_UpdatePrivateConnectionCertificate_Errors"></a>

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
<a name="API_UpdatePrivateConnectionCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/UpdatePrivateConnectionCertificate)
