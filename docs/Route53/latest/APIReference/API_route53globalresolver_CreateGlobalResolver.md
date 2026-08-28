---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateGlobalResolver.html
---

# CreateGlobalResolver
<a name="API_route53globalresolver_CreateGlobalResolver"></a>

Creates a new Route 53 Global Resolver instance. A Route 53 Global Resolver is a global, internet-accessible DNS resolver that provides secure DNS resolution for both public and private domains through global anycast IP addresses.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_CreateGlobalResolver_RequestSyntax"></a>

```
POST /global-resolver HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "ipAddressType": "{{string}}",
   "name": "{{string}}",
   "observabilityRegion": "{{string}}",
   "regions": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_route53globalresolver_CreateGlobalResolver_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53globalresolver_CreateGlobalResolver_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-clientToken"></a>
A unique string that identifies the request and ensures idempotency. If you make multiple requests with the same client token, only one Route 53 Global Resolver is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [description](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-description"></a>
An optional description for the Route 53 Global Resolver instance. Maximum length of 1024 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ipAddressType](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-ipAddressType"></a>
The IP address type for the Route 53 Global Resolver. Valid values are IPV4 (default) or DUAL\_STACK for both IPv4 and IPv6 support.
Type: String
Valid Values: `IPV4 | DUAL_STACK`
Required: No

 ** [name](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-name"></a>
A descriptive name for the Route 53 Global Resolver instance. Maximum length of 64 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** [observabilityRegion](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-observabilityRegion"></a>
The AWS Region where query resolution logs and metrics will be aggregated and delivered. If not specified, logging is not enabled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** [regions](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-regions"></a>
List of AWS Regions where the Route 53 Global Resolver will operate. The resolver will be distributed across these Regions to provide global availability and low-latency DNS resolution.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: Yes

 ** [tags](#API_route53globalresolver_CreateGlobalResolver_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-request-tags"></a>
Tags to associate with the Route 53 Global Resolver. Tags are key-value pairs that help you organize and identify your resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_route53globalresolver_CreateGlobalResolver_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_CreateGlobalResolver_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-arn"></a>
The Amazon Resource Name (ARN) of the Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-createdAt"></a>
The date and time when the Route 53 Global Resolver was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-description"></a>
The description of the Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsName](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-dnsName"></a>
The hostname that DNS clients should use for TLS certificate validation when connecting to the Route 53 Global Resolver. This value resolves to the global anycast IP addresses for the resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [id](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-id"></a>
The unique identifier for the Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [ipAddressType](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-ipAddressType"></a>
The IP address type configured for the Route 53 Global Resolver (IPV4 or DUAL\_STACK).
Type: String
Valid Values: `IPV4 | DUAL_STACK`

 ** [ipv4Addresses](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-ipv4Addresses"></a>
The global anycast IPv4 addresses associated with the Route 53 Global Resolver. DNS clients can send queries to these addresses from anywhere on the internet.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`

 ** [ipv6Addresses](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-ipv6Addresses"></a>
The global anycast IPv6 addresses associated with the Route 53 Global Resolver. This field is only populated when ipAddressType is DUAL\_STACK. DNS clients can send queries to these addresses from anywhere on the internet.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`

 ** [name](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-name"></a>
The name of the Route 53 Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [observabilityRegion](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-observabilityRegion"></a>
The AWS Region where observability data for the Route 53 Global Resolver is stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [regions](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-regions"></a>
The AWS Regions where the Route 53 Global Resolver is deployed and operational.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.

 ** [status](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-status"></a>
The current status of the Route 53 Global Resolver. Possible values are CREATING (being provisioned), UPDATING (being modified), OPERATIONAL (ready to serve queries), or DELETING (being removed).
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_CreateGlobalResolver_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateGlobalResolver-response-updatedAt"></a>
The date and time when the Route 53 Global Resolver was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_CreateGlobalResolver_Errors"></a>

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
<a name="API_route53globalresolver_CreateGlobalResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/CreateGlobalResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CreateGlobalResolver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
