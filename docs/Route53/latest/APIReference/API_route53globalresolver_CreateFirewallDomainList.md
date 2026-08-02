---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallDomainList.html
---

# CreateFirewallDomainList
<a name="API_route53globalresolver_CreateFirewallDomainList"></a>

Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_CreateFirewallDomainList_RequestSyntax"></a>

```
POST /firewall-domain-lists/{{globalResolverId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_route53globalresolver_CreateFirewallDomainList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalResolverId](#API_route53globalresolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-request-uri-globalResolverId"></a>
The ID of the Route 53 Global Resolver that the domain list will be associated with.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_CreateFirewallDomainList_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_route53globalresolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [description](#API_route53globalresolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-request-description"></a>
An optional description for the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [name](#API_route53globalresolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-request-name"></a>
A descriptive name for the firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** [tags](#API_route53globalresolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-request-tags"></a>
An array of user-defined keys and optional values. These tags can be used for categorization and organization.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "description": "string",
   "domainCount": number,
   "globalResolverId": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_CreateFirewallDomainList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-arn"></a>
An Amazon Resource Name (ARN) for the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [createdAt](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-createdAt"></a>
The time and date the domain list was created on.
Type: Timestamp

 ** [description](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-description"></a>
Description for the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [domainCount](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-domainCount"></a>
Number of domains in the domain list.
Type: Integer

 ** [globalResolverId](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-globalResolverId"></a>
The ID of the Route 53 Global Resolver that the domain list is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-id"></a>
ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-name"></a>
Name of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-status"></a>
Creation status of the domain list.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallDomainList-response-updatedAt"></a>
The time and date the domain list was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_CreateFirewallDomainList_Errors"></a>

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
<a name="API_route53globalresolver_CreateFirewallDomainList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/CreateFirewallDomainList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CreateFirewallDomainList)
