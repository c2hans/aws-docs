---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdatePrivateConnectionCertificate.html
---

# UpdatePrivateConnectionCertificate
<a name="API_UpdatePrivateConnectionCertificate"></a>

Updates the certificate associated with a private connection. Certificates can be added or replaced but not removed.

## Request Syntax
<a name="API_UpdatePrivateConnectionCertificate_RequestSyntax"></a>

```
POST /UpdatePrivateConnectionCertificate HTTP/1.1
Content-type: application/json

{
   "certificate": "{{string}}",
   "privateConnectionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePrivateConnectionCertificate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePrivateConnectionCertificate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificate](#API_UpdatePrivateConnectionCertificate_RequestSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-request-certificate"></a>
The PEM-encoded certificate chain for the private connection.
Type: String
Required: Yes

 ** [privateConnectionName](#API_UpdatePrivateConnectionCertificate_RequestSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-request-privateConnectionName"></a>
The name of the private connection to update.
Type: String
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
   "tags": {
      "string" : "string"
   },
   "type": "string",
   "vpcId": "string"
}
```

## Response Elements
<a name="API_UpdatePrivateConnectionCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateExpiryTime](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-certificateExpiryTime"></a>
The date and time the connection's certificate expires, in UTC format.
Type: Timestamp

 ** [dnsResolution](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-dnsResolution"></a>
The DNS resolution mode for the resource gateway.
Type: String
Valid Values: `PUBLIC | IN_VPC`

 ** [failureMessage](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-failureMessage"></a>
A message describing why the private connection entered a failed state, if applicable.
Type: String

 ** [hostAddress](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-hostAddress"></a>
The IP address or DNS name of the target resource.
Type: String

 ** [name](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-name"></a>
The name of the private connection.
Type: String

 ** [resourceConfigurationId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-resourceConfigurationId"></a>
The identifier or ARN of the VPC Lattice resource configuration.
Type: String

 ** [resourceGatewayId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-resourceGatewayId"></a>
The identifier or ARN of the VPC Lattice resource gateway.
Type: String

 ** [status](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-status"></a>
The current status of the private connection.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [tags](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-tags"></a>
The tags attached to the private connection.
Type: String to string map

 ** [type](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-type"></a>
The type of the private connection, indicating whether it is service-managed or self-managed.
Type: String
Valid Values: `SERVICE_MANAGED | SELF_MANAGED`

 ** [vpcId](#API_UpdatePrivateConnectionCertificate_ResponseSyntax) **   <a name="securityagent-UpdatePrivateConnectionCertificate-response-vpcId"></a>
The identifier of the VPC the resource gateway is created in.
Type: String

## Errors
<a name="API_UpdatePrivateConnectionCertificate_Errors"></a>

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
<a name="API_UpdatePrivateConnectionCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdatePrivateConnectionCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
