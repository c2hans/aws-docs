---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallDomainList.html
---

# GetFirewallDomainList
<a name="API_route53globalresolver_GetFirewallDomainList"></a>

Retrieves information about a firewall domain list.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetFirewallDomainList_RequestSyntax"></a>

```
GET /firewall-domain-lists/{{firewallDomainListId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetFirewallDomainList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [firewallDomainListId](#API_route53globalresolver_GetFirewallDomainList_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-request-uri-firewallDomainListId"></a>
ID of the domain list.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetFirewallDomainList_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetFirewallDomainList_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "clientToken": "string",
   "createdAt": "string",
   "description": "string",
   "domainCount": number,
   "globalResolverId": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_GetFirewallDomainList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-arn"></a>
Amazon Resource Name (ARN) of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-createdAt"></a>
The time and date the domain list was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-description"></a>
The description of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [domainCount](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-domainCount"></a>
Number of domains in the domain list.
Type: Integer

 ** [globalResolverId](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-globalResolverId"></a>
ID of the Global Resolver that the domain list is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-id"></a>
ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-name"></a>
Name of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-status"></a>
Operational status of the domain list.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [statusMessage](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-statusMessage"></a>
Additional information about the status of the domain list.
Type: String

 ** [updatedAt](#API_route53globalresolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallDomainList-response-updatedAt"></a>
The date and time the domain list was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_GetFirewallDomainList_Errors"></a>

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
<a name="API_route53globalresolver_GetFirewallDomainList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetFirewallDomainList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetFirewallDomainList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
