---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchUpdateFirewallRule.html
---

# BatchUpdateFirewallRule
<a name="API_route53globalresolver_BatchUpdateFirewallRule"></a>

Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_BatchUpdateFirewallRule_RequestSyntax"></a>

```
POST /firewall-rules/batch-update HTTP/1.1
Content-type: application/json

{
   "firewallRules": [
      {
         "action": "{{string}}",
         "blockOverrideDnsType": "{{string}}",
         "blockOverrideDomain": "{{string}}",
         "blockOverrideTtl": {{number}},
         "blockResponse": "{{string}}",
         "confidenceThreshold": "{{string}}",
         "description": "{{string}}",
         "dnsAdvancedProtection": "{{string}}",
         "firewallRuleId": "{{string}}",
         "name": "{{string}}",
         "priority": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_route53globalresolver_BatchUpdateFirewallRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53globalresolver_BatchUpdateFirewallRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [firewallRules](#API_route53globalresolver_BatchUpdateFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchUpdateFirewallRule-request-firewallRules"></a>
The DNS Firewall rule IDs to be updated.
Type: Array of [BatchUpdateFirewallRuleInputItem](API_route53globalresolver_BatchUpdateFirewallRuleInputItem.md) objects
Required: Yes

## Response Syntax
<a name="API_route53globalresolver_BatchUpdateFirewallRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failures": [
      {
         "code": number,
         "firewallRule": {
            "action": "string",
            "blockOverrideDnsType": "string",
            "blockOverrideDomain": "string",
            "blockOverrideTtl": number,
            "blockResponse": "string",
            "clientToken": "string",
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
         },
         "message": "string"
      }
   ],
   "successes": [
      {
         "code": number,
         "firewallRule": {
            "action": "string",
            "blockOverrideDnsType": "string",
            "blockOverrideDomain": "string",
            "blockOverrideTtl": number,
            "blockResponse": "string",
            "clientToken": "string",
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
         },
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53globalresolver_BatchUpdateFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_route53globalresolver_BatchUpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchUpdateFirewallRule-response-failures"></a>
High level information about the DNS Firewall rules that failed to update.
Type: Array of [BatchUpdateFirewallRuleOutputItem](API_route53globalresolver_BatchUpdateFirewallRuleOutputItem.md) objects

 ** [successes](#API_route53globalresolver_BatchUpdateFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchUpdateFirewallRule-response-successes"></a>
High level information about the DNS Firewall rules that were successfully updated.
Type: Array of [BatchUpdateFirewallRuleOutputItem](API_route53globalresolver_BatchUpdateFirewallRuleOutputItem.md) objects

## Errors
<a name="API_route53globalresolver_BatchUpdateFirewallRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

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
<a name="API_route53globalresolver_BatchUpdateFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchUpdateFirewallRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
