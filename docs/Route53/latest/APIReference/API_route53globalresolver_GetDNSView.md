---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetDNSView.html
---

# GetDNSView
<a name="API_route53globalresolver_GetDNSView"></a>

Retrieves information about a DNS view.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetDNSView_RequestSyntax"></a>

```
GET /dns-views/{{dnsViewId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetDNSView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dnsViewId](#API_route53globalresolver_GetDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-request-uri-dnsViewId"></a>
The ID of the DNS view to retrieve information about.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetDNSView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetDNSView_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_GetDNSView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-arn"></a>
Amazon Resource Name (ARN) of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-createdAt"></a>
The time and date the DNS view was creates on.
Type: Timestamp

 ** [description](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-description"></a>
Description of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnssecValidation](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-dnssecValidation"></a>
Specifies whether DNSSEC is enabled or disabled for the DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [ednsClientSubnet](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-ednsClientSubnet"></a>
Specifies whether edns0 client subnet is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [firewallRulesFailOpen](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-firewallRulesFailOpen"></a>
Specifies the DNS Firewall failure mode configuration. When enabled, the DNS Firewall allows DNS queries to proceed if it's unable to properly evaluate them. When disabled, the DNS Firewall blocks DNS queries it's unable to evaluate.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [globalResolverId](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-globalResolverId"></a>
ID of the Global Resolver the DNS view is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-id"></a>
ID of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-name"></a>
Name of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-status"></a>
Operational status of the DNS view.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | ENABLING | DISABLING | DISABLED | DELETING`

 ** [updatedAt](#API_route53globalresolver_GetDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetDNSView-response-updatedAt"></a>
The time and date the DNS view was updated on.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_GetDNSView_Errors"></a>

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
<a name="API_route53globalresolver_GetDNSView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetDNSView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetDNSView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
