---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetGlobalResolver.html
---

# GetGlobalResolver
<a name="API_route53globalresolver_GetGlobalResolver"></a>

Retrieves information about a Route 53 Global Resolver instance.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetGlobalResolver_RequestSyntax"></a>

```
GET /global-resolver/{{globalResolverId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetGlobalResolver_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalResolverId](#API_route53globalresolver_GetGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-request-uri-globalResolverId"></a>
The ID of the Route 53 Global Resolver to retrieve information about.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetGlobalResolver_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetGlobalResolver_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_GetGlobalResolver_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-arn"></a>
The Amazon Resource Name (ARN) of the Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-createdAt"></a>
The date and time the Global Resolver was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-description"></a>
The description of the Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsName](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-dnsName"></a>
The hostname used by the customers' DNS clients for certification validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [id](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-id"></a>
The ID of the Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [ipAddressType](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-ipAddressType"></a>
The IP address type configured for the Global Resolver.
Type: String
Valid Values: `IPV4 | DUAL_STACK`

 ** [ipv4Addresses](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-ipv4Addresses"></a>
List of anycast IPv4 addresses associated with the Global Resolver instance.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`

 ** [ipv6Addresses](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-ipv6Addresses"></a>
List of anycast IPv6 addresses associated with the Global Resolver instance. This field is only populated when ipAddressType is DUAL\_STACK.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`

 ** [name](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-name"></a>
The name of the Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [observabilityRegion](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-observabilityRegion"></a>
The AWS Regions in which the users' Global Resolver query resolution logs will be propagated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [regions](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-regions"></a>
The AWS Regions in which the Global Resolver operate.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [status](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-status"></a>
The operational status of the Global Resolver.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_GetGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetGlobalResolver-response-updatedAt"></a>
The date and time the Global Resolver was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_GetGlobalResolver_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

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
<a name="API_route53globalresolver_GetGlobalResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetGlobalResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetGlobalResolver)
