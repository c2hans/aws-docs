---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateResponderGateway.html
---

# UpdateResponderGateway
<a name="API_UpdateResponderGateway"></a>

Updates a responder gateway. This operation updates the description, listener configuration, and managed endpoint configuration. To change the domain name, port, or protocol of a responder gateway, delete the gateway and create a new one.

## Request Syntax
<a name="API_UpdateResponderGateway_RequestSyntax"></a>

```
POST /responder-gateway/{{gatewayId}}/update HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "domainName": "{{string}}",
   "listenerConfig": {
      "protocols": [ "{{string}}" ]
   },
   "managedEndpointConfiguration": { ... },
   "port": {{number}},
   "protocol": "{{string}}",
   "trustStoreConfiguration": {
      "certificateAuthorityCertificates": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateResponderGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_UpdateResponderGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `clientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: Yes

 ** [description](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-description"></a>
An optional description for the responder gateway.
Type: String
Pattern: `[A-Za-z0-9 ]+`
Required: No

 ** [domainName](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-domainName"></a>
Domain name for the responder gateway. This operation does not change the domain name of an existing gateway. To use a different domain name, delete the gateway and create a new one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`
Required: No

 ** [listenerConfig](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-listenerConfig"></a>
The listener configuration for the responder gateway.
Type: [ListenerConfig](API_ListenerConfig.md) object
Required: No

 ** [managedEndpointConfiguration](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-managedEndpointConfiguration"></a>
The configuration for the managed endpoint.
Type: [ManagedEndpointConfiguration](API_ManagedEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [port](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-port"></a>
Networking port to use. This operation does not change the port of an existing gateway. To use a different port, delete the gateway and create a new one.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** [protocol](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-protocol"></a>
Networking protocol to use. This operation does not change the protocol of an existing gateway. To use a different protocol, delete the gateway and create a new one.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

 ** [trustStoreConfiguration](#API_UpdateResponderGateway_RequestSyntax) **   <a name="rtbfabric-UpdateResponderGateway-request-trustStoreConfiguration"></a>
The configuration of the trust store.
Type: [TrustStoreConfiguration](API_TrustStoreConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateResponderGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "gatewayId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateResponderGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [gatewayId](#API_UpdateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-UpdateResponderGateway-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [status](#API_UpdateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-UpdateResponderGateway-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | ACTIVE | PENDING_DELETION | DELETED | ERROR | PENDING_UPDATE | ISOLATED | PENDING_ISOLATION | PENDING_RESTORATION`

## Errors
<a name="API_UpdateResponderGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed because of a conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateResponderGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/UpdateResponderGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateResponderGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
