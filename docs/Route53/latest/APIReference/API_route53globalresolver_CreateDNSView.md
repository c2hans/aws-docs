---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateDNSView.html
---

# CreateDNSView
<a name="API_route53globalresolver_CreateDNSView"></a>

Creates a DNS view within a Route 53 Global Resolver. A DNS view models end users, user groups, networks, and devices, and serves as a parent resource that holds configurations controlling access, authorization, DNS firewall rules, and forwarding rules.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_CreateDNSView_RequestSyntax"></a>

```
POST /dns-views/{{globalResolverId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "dnssecValidation": "{{string}}",
   "ednsClientSubnet": "{{string}}",
   "firewallRulesFailOpen": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_route53globalresolver_CreateDNSView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalResolverId](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-uri-globalResolverId"></a>
The ID of the Route 53 Global Resolver to associate with this DNS view.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_CreateDNSView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-clientToken"></a>
A unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [description](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-description"></a>
An optional description for the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [dnssecValidation](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-dnssecValidation"></a>
Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ednsClientSubnet](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-ednsClientSubnet"></a>
Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [firewallRulesFailOpen](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-firewallRulesFailOpen"></a>
Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [name](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-name"></a>
A descriptive name for the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** [tags](#API_route53globalresolver_CreateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-request-tags"></a>
Tags to associate with the DNS view.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_route53globalresolver_CreateDNSView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "clientToken": "string",
   "createdAt": "string",
   "description": "string",
   "dnssecValidation": "string",
   "ednsClientSubnet": "string",
   "firewallRulesFailOpen": "string",
   "globalResolverId": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_CreateDNSView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-arn"></a>
The Amazon Resource Name (ARN) of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-createdAt"></a>
The date and time when the DNS view was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-description"></a>
The description of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnssecValidation](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-dnssecValidation"></a>
Whether DNSSEC validation is enabled for DNS queries in this DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [ednsClientSubnet](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-ednsClientSubnet"></a>
Whether EDNS Client Subnet injection is enabled for DNS queries in this DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [firewallRulesFailOpen](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-firewallRulesFailOpen"></a>
The behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [globalResolverId](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-globalResolverId"></a>
The ID of the Route 53 Global Resolver instance the DNS view is created for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-id"></a>
The unique identifier for the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-name"></a>
The descriptive name of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-status"></a>
The operational status of the DNS view.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | ENABLING | DISABLING | DISABLED | DELETING`

 ** [updatedAt](#API_route53globalresolver_CreateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateDNSView-response-updatedAt"></a>
The date and time when the DNS view was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_CreateDNSView_Errors"></a>

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
<a name="API_route53globalresolver_CreateDNSView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/CreateDNSView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CreateDNSView)
