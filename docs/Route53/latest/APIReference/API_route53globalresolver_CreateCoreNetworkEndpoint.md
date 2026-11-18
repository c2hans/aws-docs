---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateCoreNetworkEndpoint.html
---

# CreateCoreNetworkEndpoint
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint"></a>

Creates a core network endpoint, which enables DNS resolution for AWS Cloud WAN core network segments. The endpoint connects a Route 53 Global Resolver to an AWS Cloud WAN core network so that resources attached to the core network can send DNS queries to the resolver.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax"></a>

```
POST /core-network-endpoints HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "coreNetworkArn": "{{string}}",
   "globalResolverId": "{{string}}",
   "ipAddresses": [
      {
         "dnsLabel": "{{string}}",
         "ipv4Address": "{{string}}",
         "ipv6Address": "{{string}}",
         "regions": [ "{{string}}" ],
         "regionScope": "{{string}}"
      }
   ],
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-clientToken"></a>
A unique, case-sensitive identifier that ensures the request is idempotent. Making the same request multiple times with the same `clientToken` produces the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [coreNetworkArn](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-coreNetworkArn"></a>
The Amazon Resource Name (ARN) of the AWS Cloud WAN core network to connect to this endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** [globalResolverId](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-globalResolverId"></a>
The ID of the Route 53 Global Resolver to associate with this core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** [ipAddresses](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-ipAddresses"></a>
The IP addresses that the core network endpoint uses to resolve DNS queries within the AWS Cloud WAN core network.
Type: Array of [CoreNetworkEndpointDnsIpInputItem](API_route53globalresolver_CoreNetworkEndpointDnsIpInputItem.md) objects
Required: Yes

 ** [name](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-name"></a>
A descriptive name for the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** [tags](#API_route53globalresolver_CreateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-request-tags"></a>
An array of user-defined keys and optional values that you can use to categorize and organize the core network endpoint.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "availableRegions": [ "string" ],
   "coreNetworkArn": "string",
   "createdAt": "string",
   "globalResolverId": "string",
   "id": "string",
   "ipAddresses": [
      {
         "dnsLabel": "string",
         "dnsName": "string",
         "ipv4Address": "string",
         "ipv6Address": "string",
         "regions": [ "string" ],
         "regionScope": "string"
      }
   ],
   "name": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-arn"></a>
The Amazon Resource Name (ARN) of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [availableRegions](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-availableRegions"></a>
The AWS Regions in which the core network endpoint is available.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [coreNetworkArn](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-coreNetworkArn"></a>
The Amazon Resource Name (ARN) of the AWS Cloud WAN core network connected to the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [createdAt](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-createdAt"></a>
The date and time when the core network endpoint was created.
Type: Timestamp

 ** [globalResolverId](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-globalResolverId"></a>
The ID of the Route 53 Global Resolver associated with the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-id"></a>
The unique identifier of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [ipAddresses](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-ipAddresses"></a>
The IP addresses that the core network endpoint uses to resolve DNS queries within the AWS Cloud WAN core network.
Type: Array of [CoreNetworkEndpointDnsIpItem](API_route53globalresolver_CoreNetworkEndpointDnsIpItem.md) objects

 ** [name](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-name"></a>
The name of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-status"></a>
The current status of the core network endpoint.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_CreateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateCoreNetworkEndpoint-response-updatedAt"></a>
The date and time when the core network endpoint was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed one or more service quotas. Check your current usage and quotas, then try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 402

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
<a name="API_route53globalresolver_CreateCoreNetworkEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CreateCoreNetworkEndpoint)
