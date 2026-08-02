---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetFirewallRule.html
---

# GetFirewallRule
<a name="API_route53globalresolver_GetFirewallRule"></a>

Retrieves information about a DNS firewall rule.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetFirewallRule_RequestSyntax"></a>

```
GET /firewall-rules/{{firewallRuleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetFirewallRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [firewallRuleId](#API_route53globalresolver_GetFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-request-uri-firewallRuleId"></a>
ID of the DNS Firewall rule.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetFirewallRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetFirewallRule_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_GetFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`

 ** [blockOverrideDnsType](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-blockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Valid Values: `CNAME`

 ** [blockOverrideDomain](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-blockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`

 ** [blockOverrideTtl](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-blockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.

 ** [blockResponse](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-blockResponse"></a>
The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK`.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`

 ** [confidenceThreshold](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-confidenceThreshold"></a>
The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`

 ** [createdAt](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-createdAt"></a>
The time and date the DNS Firewall rule was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-description"></a>
The description of the DNS Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsAdvancedProtection](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-dnsAdvancedProtection"></a>
The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS\_TUNNELING, and DICTIONARY\_DGA.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`

 ** [dnsViewId](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-dnsViewId"></a>
The DNS view ID the DNS Firewall is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [firewallDomainListId](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-firewallDomainListId"></a>
The ID of a DNS Firewall domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-id"></a>
ID of the DNS Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-name"></a>
The name of the DNS Firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [priority](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-priority"></a>
The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [queryType](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-queryType"></a>
The DNS query type you want the rule to evaluate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.

 ** [status](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-status"></a>
The operational status of the DNS Firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_GetFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetFirewallRule-response-updatedAt"></a>
The date and time the DNS Firewall rule was updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_GetFirewallRule_Errors"></a>

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
<a name="API_route53globalresolver_GetFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetFirewallRule)
