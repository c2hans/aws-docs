---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateDNSView.html
---

# UpdateDNSView
<a name="API_route53globalresolver_UpdateDNSView"></a>

Updates the configuration of a DNS view.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_UpdateDNSView_RequestSyntax"></a>

```
PATCH /dns-views/{{dnsViewId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "dnssecValidation": "{{string}}",
   "ednsClientSubnet": "{{string}}",
   "firewallRulesFailOpen": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_route53globalresolver_UpdateDNSView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dnsViewId](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-uri-dnsViewId"></a>
The unique identifier of the DNS view to update.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_UpdateDNSView_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-description"></a>
A description of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [dnssecValidation](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-dnssecValidation"></a>
Whether to enable DNSSEC validation for the DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [ednsClientSubnet](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-ednsClientSubnet"></a>
Whether to enable EDNS Client Subnet injection for the DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [firewallRulesFailOpen](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-firewallRulesFailOpen"></a>
Whether firewall rules should fail open when they cannot be evaluated.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [name](#API_route53globalresolver_UpdateDNSView_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-request-name"></a>
The name of the DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

## Response Syntax
<a name="API_route53globalresolver_UpdateDNSView_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_UpdateDNSView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-arn"></a>
The Amazon Resource Name (ARN) of the updated DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-createdAt"></a>
The date and time when the DNS view was originally created.
Type: Timestamp

 ** [description](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-description"></a>
The description of the updated DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnssecValidation](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-dnssecValidation"></a>
Whether DNSSEC validation is enabled for the updated DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [ednsClientSubnet](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-ednsClientSubnet"></a>
Whether EDNS Client Subnet injection is enabled for the updated DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [firewallRulesFailOpen](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-firewallRulesFailOpen"></a>
Whether firewall rules fail open when they cannot be evaluated for the updated DNS view.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [globalResolverId](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-globalResolverId"></a>
The ID of the global resolver associated with the updated DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-id"></a>
The unique identifier of the updated DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-name"></a>
The name of the updated DNS view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-status"></a>
The current status of the updated DNS view.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | ENABLING | DISABLING | DISABLED | DELETING`

 ** [updatedAt](#API_route53globalresolver_UpdateDNSView_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateDNSView-response-updatedAt"></a>
The date and time when the DNS view was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_UpdateDNSView_Errors"></a>

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
<a name="API_route53globalresolver_UpdateDNSView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/UpdateDNSView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/UpdateDNSView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
