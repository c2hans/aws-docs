---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_DeleteFirewallRule.html
---

# DeleteFirewallRule
<a name="API_route53globalresolver_DeleteFirewallRule"></a>

Deletes a DNS firewall rule. This operation cannot be undone.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_DeleteFirewallRule_RequestSyntax"></a>

```
DELETE /firewall-rules/{{firewallRuleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_DeleteFirewallRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [firewallRuleId](#API_route53globalresolver_DeleteFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-request-uri-firewallRuleId"></a>
The unique identifier of the firewall rule to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_DeleteFirewallRule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_DeleteFirewallRule_ResponseSyntax"></a>

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
<a name="API_route53globalresolver_DeleteFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-action"></a>
The action that was configured for the deleted firewall rule.
Type: String
Valid Values: `ALLOW | ALERT | BLOCK`

 ** [blockOverrideDnsType](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-blockOverrideDnsType"></a>
The DNS record type that was configured for the deleted firewall rule's custom response.
Type: String
Valid Values: `CNAME`

 ** [blockOverrideDomain](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-blockOverrideDomain"></a>
The custom domain that was configured for the deleted firewall rule's BLOCK response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\*?[a-zA-Z0-9!"#$%&'()*+,./:;<=>?@\[\\\]^_`{|}~-]+`

 ** [blockOverrideTtl](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-blockOverrideTtl"></a>
The TTL value that was configured for the deleted firewall rule's custom response.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.

 ** [blockResponse](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-blockResponse"></a>
The block response type that was configured for the deleted firewall rule.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`

 ** [confidenceThreshold](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-confidenceThreshold"></a>
The confidence threshold that was configured for the deleted firewall rule's advanced threat detection.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`

 ** [createdAt](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-createdAt"></a>
The date and time when the firewall rule was originally created.
Type: Timestamp

 ** [description](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-description"></a>
The description of the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [dnsAdvancedProtection](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-dnsAdvancedProtection"></a>
Whether advanced DNS threat protection was enabled for the deleted firewall rule.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`

 ** [dnsViewId](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-dnsViewId"></a>
The ID of the DNS view that was associated with the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [firewallDomainListId](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-firewallDomainListId"></a>
The ID of the firewall domain list that was associated with the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-id"></a>
The unique identifier of the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-name"></a>
The name of the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [priority](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-priority"></a>
The priority that was configured for the deleted firewall rule.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 10000.

 ** [queryType](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-queryType"></a>
The DNS query type that the deleted firewall rule was configured to match.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.

 ** [status](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-status"></a>
The final status of the deleted firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`

 ** [updatedAt](#API_route53globalresolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_DeleteFirewallRule-response-updatedAt"></a>
The date and time when the firewall rule was last updated before deletion.
Type: Timestamp

## Errors
<a name="API_route53globalresolver_DeleteFirewallRule_Errors"></a>

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
<a name="API_route53globalresolver_DeleteFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/DeleteFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/DeleteFirewallRule)
