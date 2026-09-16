---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CreateFirewallRule.html
---

# CreateFirewallRule
<a name="API_route53globalresolver_CreateFirewallRule"></a>

Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_CreateFirewallRule_RequestSyntax"></a>

```
POST /firewall-rules HTTP/1.1
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
   "dnsViewId": "{{string}}",
   "firewallDomainListId": "{{string}}",
   "name": "{{string}}",
   "priority": {{number}},
   "qType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_route53globalresolver_CreateFirewallRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53globalresolver_CreateFirewallRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:
+  `ALLOW` - Permit the request to go through.
+  `ALERT` - Permit the request and send metrics and logs to CloudWatch.
+  `BLOCK` - Disallow the request. This option requires additional details in the rule's `BlockResponse`.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`
Required: Yes

 ** [blockOverrideDnsType](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-blockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
This setting is required if the `BlockResponse` setting is `OVERRIDE`.
Type: String
Valid Values: `CNAME`
Required: No

 ** [blockOverrideDomain](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-blockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
This setting is required if the `BlockResponse` setting is `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`
Required: No

 ** [blockOverrideTtl](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-blockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
This setting is required if the `BlockResponse` setting is `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** [blockResponse](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-blockResponse"></a>
The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** [clientToken](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [confidenceThreshold](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-confidenceThreshold"></a>
The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** [description](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-description"></a>
An optional description for the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [dnsAdvancedProtection](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-dnsAdvancedProtection"></a>
Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** [dnsViewId](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-dnsViewId"></a>
The ID of the DNS view to associate with this firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** [firewallDomainListId](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-firewallDomainListId"></a>
The ID of the firewall domain list to use in this rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: No

 ** [name](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-name"></a>
A descriptive name for the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** [priority](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-priority"></a>
The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [qType](#API_route53globalresolver_CreateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-request-qType"></a>
The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Required: No

## Response Syntax
<a name="API_route53globalresolver_CreateFirewallRule_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_CreateFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-action"></a>
The action that DNS Firewall takes on DNS queries that match this rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`

 ** [blockOverrideDnsType](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-blockOverrideDnsType"></a>
The DNS record type for the custom response when blockResponse is OVERRIDE.
Type: String
Valid Values: `CNAME`

 ** [blockOverrideDomain](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-blockOverrideDomain"></a>
The custom domain to return when the action is BLOCK and blockResponse is OVERRIDE.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`

 ** [blockOverrideTtl](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-blockOverrideTtl"></a>
The time-to-live (TTL) value for the custom response when blockResponse is OVERRIDE.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.

 ** [blockResponse](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-blockResponse"></a>
The response to return when the action is BLOCK.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`

 ** [confidenceThreshold](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-confidenceThreshold"></a>
The confidence threshold for advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`

 ** [createdAt](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-createdAt"></a>
The date and time when the firewall rule was created.
Type: Timestamp

 ** [description](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-description"></a>
The description of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsAdvancedProtection](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-dnsAdvancedProtection"></a>
Whether advanced DNS threat protection is enabled for this rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`

 ** [dnsViewId](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-dnsViewId"></a>
The ID of the DNS view associated with this firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [firewallDomainListId](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-firewallDomainListId"></a>
The ID of the firewall domain list used in this rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-id"></a>
The unique identifier for the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-name"></a>
The name of the firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [priority](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-priority"></a>
The priority of the firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [queryType](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-queryType"></a>
The DNS query type that this rule matches.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.

 ** [status](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-status"></a>
The operational status of the firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_CreateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_CreateFirewallRule-response-updatedAt"></a>
The date and time when the firewall rule was last updated.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_CreateFirewallRule_Errors"></a>

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
<a name="API_route53globalresolver_CreateFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/CreateFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CreateFirewallRule)
