---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateCoreNetworkEndpoint.html
---

# UpdateCoreNetworkEndpoint
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint"></a>

Updates the configuration of a core network endpoint. You can change the name and modify the IP addresses that the endpoint uses for DNS resolution.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestSyntax"></a>

```
PATCH /core-network-endpoints/{{coreNetworkEndpointId}} HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "updateIpAddresses": [
      {
         "dnsLabel": "{{string}}",
         "ipv4Address": "{{string}}",
         "ipv6Address": "{{string}}",
         "operation": "{{string}}",
         "regions": [ "{{string}}" ],
         "regionScope": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [coreNetworkEndpointId](#API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-request-uri-coreNetworkEndpointId"></a>
The unique identifier of the core network endpoint to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-request-name"></a>
The name of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** [updateIpAddresses](#API_route53globalresolver_UpdateCoreNetworkEndpoint_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-request-updateIpAddresses"></a>
The IP address changes to apply to the core network endpoint. Use this parameter to add or remove the IP addresses that the endpoint uses to resolve DNS queries within the AWS Cloud WAN core network.
Type: Array of [UpdateIpAddressEntry](API_route53globalresolver_UpdateIpAddressEntry.md) objects
Required: No

## Response Syntax
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-arn"></a>
The Amazon Resource Name (ARN) of the updated core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [availableRegions](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-availableRegions"></a>
The AWS Regions in which the updated core network endpoint is available.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [coreNetworkArn](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-coreNetworkArn"></a>
The Amazon Resource Name (ARN) of the AWS Cloud WAN core network connected to the updated endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [createdAt](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-createdAt"></a>
The date and time when the core network endpoint was originally created.
Type: Timestamp

 ** [globalResolverId](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-globalResolverId"></a>
The ID of the Route 53 Global Resolver associated with the updated core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-id"></a>
The unique identifier of the updated core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [ipAddresses](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-ipAddresses"></a>
The IP addresses that the updated core network endpoint uses to resolve DNS queries within the AWS Cloud WAN core network.
Type: Array of [CoreNetworkEndpointDnsIpItem](API_route53globalresolver_CoreNetworkEndpointDnsIpItem.md) objects

 ** [name](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-name"></a>
The name of the updated core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-status"></a>
The current status of the updated core network endpoint.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_UpdateCoreNetworkEndpoint_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateCoreNetworkEndpoint-response-updatedAt"></a>
The date and time when the core network endpoint was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_Errors"></a>

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
<a name="API_route53globalresolver_UpdateCoreNetworkEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/UpdateCoreNetworkEndpoint)
