---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateFirewallRule.html
---

# UpdateFirewallRule
<a name="API_route53globalresolver_UpdateFirewallRule"></a>

Updates the configuration of a DNS firewall rule.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_UpdateFirewallRule_RequestSyntax"></a>

```
PATCH /firewall-rules/{{firewallRuleId}} HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}",
   "blockOverrideDnsType": "{{string}}",
   "blockOverrideDomain": "{{string}}",
   "blockOverrideTtl": {{number}},
   "blockResponse": "{{string}}",
   "clientToken": "{{string}}",
   "confidenceThreshold": "{{string}}",
   "description": "{{string}}",
   "dnsAdvancedProtection": "{{string}}",
   "name": "{{string}}",
   "priority": {{number}}
}
```

## URI Request Parameters
<a name="API_route53globalresolver_UpdateFirewallRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [firewallRuleId](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-uri-firewallRuleId"></a>
The ID of the DNS Firewall rule.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_UpdateFirewallRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: No

 ** [blockOverrideDnsType](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-blockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Valid Values: `CNAME`
Required: No

 ** [blockOverrideDomain](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-blockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** [blockOverrideTtl](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-blockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** [blockResponse](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-blockResponse"></a>
The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK`.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** [clientToken](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [confidenceThreshold](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-confidenceThreshold"></a>
The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** [description](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-description"></a>
The description for the Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [dnsAdvancedProtection](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-dnsAdvancedProtection"></a>
The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS\_TUNNELING, and DICTIONARY\_DGA.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** [name](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-name"></a>
The name of the DNS Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** [priority](#API_route53globalresolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-request-priority"></a>
The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## Response Syntax
<a name="API_route53globalresolver_UpdateFirewallRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "blockOverrideDnsType": "string",
   "blockOverrideDomain": "string",
   "blockOverrideTtl": number,
   "blockResponse": "string",
   "confidenceThreshold": "string",
   "createdAt": "string",
   "description": "string",
   "dnsAdvancedProtection": "string",
   "dnsViewId": "string",
   "firewallDomainListId": "string",
   "id": "string",
   "name": "string",
   "priority": number,
   "queryType": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_UpdateFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`

 ** [blockOverrideDnsType](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-blockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Valid Values: `CNAME`

 ** [blockOverrideDomain](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-blockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`

 ** [blockOverrideTtl](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-blockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.

 ** [blockResponse](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-blockResponse"></a>
The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK`.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`

 ** [confidenceThreshold](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-confidenceThreshold"></a>
The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`

 ** [createdAt](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-createdAt"></a>
The time and date the Firewall rule was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-description"></a>
The description of the Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsAdvancedProtection](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-dnsAdvancedProtection"></a>
The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS\_TUNNELING, and DICTIONARY\_DGA.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`

 ** [dnsViewId](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-dnsViewId"></a>
The ID of the DNS view the Firewall rule is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [firewallDomainListId](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-firewallDomainListId"></a>
The ID of the domain list associated with the Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-id"></a>
The ID of the Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-name"></a>
The name of the Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [priority](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-priority"></a>
The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [queryType](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-queryType"></a>
The DNS query type you want the rule to evaluate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.

 ** [status](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-status"></a>
The operational status of the firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateFirewallRule-response-updatedAt"></a>
The time and date the rule was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_UpdateFirewallRule_Errors"></a>

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
<a name="API_route53globalresolver_UpdateFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/UpdateFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/UpdateFirewallRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
