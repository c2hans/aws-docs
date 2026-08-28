---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRule.html
---

# BatchDeleteFirewallRule
<a name="API_route53globalresolver_BatchDeleteFirewallRule"></a>

Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_BatchDeleteFirewallRule_RequestSyntax"></a>

```
POST /firewall-rules/batch-delete HTTP/1.1
Content-type: application/json

{
   "firewallRules": [
      {
         "firewallRuleId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_route53globalresolver_BatchDeleteFirewallRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53globalresolver_BatchDeleteFirewallRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [firewallRules](#API_route53globalresolver_BatchDeleteFirewallRule_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchDeleteFirewallRule-request-firewallRules"></a>
An array of the DNS Firewall IDs to be deleted.
Type: Array of [BatchDeleteFirewallRuleInputItem](API_route53globalresolver_BatchDeleteFirewallRuleInputItem.md) objects
Required: Yes

## Response Syntax
<a name="API_route53globalresolver_BatchDeleteFirewallRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failures": [
      {
         "code": number,
         "firewallRule": {
            "clientToken": "string",
            "id": "string",
            "name": "string",
            "status": "string"
         },
         "message": "string"
      }
   ],
   "successes": [
      {
         "code": number,
         "firewallRule": {
            "clientToken": "string",
            "id": "string",
            "name": "string",
            "status": "string"
         },
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53globalresolver_BatchDeleteFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failures](#API_route53globalresolver_BatchDeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchDeleteFirewallRule-response-failures"></a>
High level information about the DNS Firewall rules that failed to delete.
Type: Array of [BatchDeleteFirewallRuleOutputItem](API_route53globalresolver_BatchDeleteFirewallRuleOutputItem.md) objects

 ** [successes](#API_route53globalresolver_BatchDeleteFirewallRule_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_BatchDeleteFirewallRule-response-successes"></a>
High level information about the DNS Firewall rules that were deleted successfully.
Type: Array of [BatchDeleteFirewallRuleOutputItem](API_route53globalresolver_BatchDeleteFirewallRuleOutputItem.md) objects

## Errors
<a name="API_route53globalresolver_BatchDeleteFirewallRule_Errors"></a>

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
<a name="API_route53globalresolver_BatchDeleteFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchDeleteFirewallRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
