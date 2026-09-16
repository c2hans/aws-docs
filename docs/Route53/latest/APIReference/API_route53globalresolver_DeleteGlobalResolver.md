---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteGlobalResolver.html
---

# DeleteGlobalResolver
<a name="API_route53globalresolver_DeleteGlobalResolver"></a>

Deletes a Route 53 Global Resolver instance. This operation cannot be undone. All associated DNS views, access sources, tokens, and firewall rules are also deleted.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_DeleteGlobalResolver_RequestSyntax"></a>

```
DELETE /global-resolver/{{globalResolverId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_DeleteGlobalResolver_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalResolverId](#API_route53globalresolver_DeleteGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-request-uri-globalResolverId"></a>
The unique identifier of the Route 53 Global Resolver to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_DeleteGlobalResolver_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "clientToken": "string",
   "createdAt": "string",
   "description": "string",
   "dnsName": "string",
   "id": "string",
   "ipAddressType": "string",
   "ipv4Addresses": [ "string" ],
   "ipv6Addresses": [ "string" ],
   "name": "string",
   "observabilityRegion": "string",
   "regions": [ "string" ],
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_DeleteGlobalResolver_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-arn"></a>
The Amazon Resource Name (ARN) of the deleted Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-createdAt"></a>
The date and time when the Route 53 Global Resolver was originally created.
Type: Timestamp

 ** [description](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-description"></a>
The description of the deleted Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsName](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-dnsName"></a>
The hostname that DNS clients used for TLS certificate validation when connecting to the deleted Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [id](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-id"></a>
The unique identifier of the deleted Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [ipAddressType](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-ipAddressType"></a>
The IP address type that was configured for the deleted Route 53 Global Resolver.
Type: String
Valid Values: `IPV4 | DUAL_STACK`

 ** [ipv4Addresses](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-ipv4Addresses"></a>
The global anycast IPv4 addresses that were associated with the deleted Route 53 Global Resolver.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`

 ** [ipv6Addresses](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-ipv6Addresses"></a>
The global anycast IPv6 addresses that were associated with the deleted Route 53 Global Resolver.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`

 ** [name](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-name"></a>
The name of the deleted Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [observabilityRegion](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-observabilityRegion"></a>
The AWS Region where observability data for the deleted Route 53 Global Resolver was stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [regions](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-regions"></a>
The AWS Regions where the deleted Route 53 Global Resolver was deployed and operational.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [status](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-status"></a>
The final status of the deleted Route 53 Global Resolver.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_DeleteGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteGlobalResolver-response-updatedAt"></a>
The date and time when the Route 53 Global Resolver was last updated before deletion.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_DeleteGlobalResolver_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify the resource ID and try again.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to too many requests. Wait a moment and try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are invalid. Check the parameter values and try again.
 ** fieldList **
The list of fields that aren't valid.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_route53globalresolver_DeleteGlobalResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/DeleteGlobalResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/DeleteGlobalResolver)
