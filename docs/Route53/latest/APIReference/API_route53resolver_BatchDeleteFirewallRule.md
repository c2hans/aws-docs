---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_BatchDeleteFirewallRule.html
---

# BatchDeleteFirewallRule
<a name="API_route53resolver_BatchDeleteFirewallRule"></a>

Deletes multiple DNS Firewall rules from the specified rule group.

## Request Syntax
<a name="API_route53resolver_BatchDeleteFirewallRule_RequestSyntax"></a>

```
{
   "DeleteFirewallRuleEntries": [
      {
         "FirewallDomainListId": "{{string}}",
         "FirewallRuleGroupId": "{{string}}",
         "FirewallThreatProtectionId": "{{string}}",
         "Qtype": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_BatchDeleteFirewallRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeleteFirewallRuleEntries](#API_route53resolver_BatchDeleteFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_BatchDeleteFirewallRule-request-DeleteFirewallRuleEntries"></a>
The list of firewall rules to delete.
Type: Array of [DeleteFirewallRuleEntry](API_route53resolver_DeleteFirewallRuleEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_route53resolver_BatchDeleteFirewallRule_ResponseSyntax"></a>

```
{
   "DeletedFirewallRules": [
      {
         "Action": "string",
         "BlockOverrideDnsType": "string",
         "BlockOverrideDomain": "string",
         "BlockOverrideTtl": number,
         "BlockResponse": "string",
         "ConfidenceThreshold": "string",
         "CreationTime": "string",
         "CreatorRequestId": "string",
         "DnsThreatProtection": "string",
         "FirewallDomainListId": "string",
         "FirewallDomainRedirectionAction": "string",
         "FirewallRuleGroupId": "string",
         "FirewallRuleType": {
            "DnsThreatProtection": {
               "ConfidenceThreshold": "string",
               "Value": "string"
            },
            "FirewallAdvancedContentCategory": {
               "Category": "string"
            },
            "FirewallAdvancedThreatCategory": {
               "Category": "string"
            },
            "PartnerThreatProtection": {
               "Partner": "string"
            }
         },
         "FirewallThreatProtectionId": "string",
         "ModificationTime": "string",
         "Name": "string",
         "Priority": number,
         "Qtype": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "DeleteErrors": [
      {
         "Code": "string",
         "FirewallRule": {
            "FirewallDomainListId": "string",
            "FirewallRuleGroupId": "string",
            "FirewallThreatProtectionId": "string",
            "Qtype": "string"
         },
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_BatchDeleteFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletedFirewallRules](#API_route53resolver_BatchDeleteFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_BatchDeleteFirewallRule-response-DeletedFirewallRules"></a>
The firewall rules that were successfully deleted by the request.
Type: Array of [FirewallRule](API_route53resolver_FirewallRule.md) objects

 ** [DeleteErrors](#API_route53resolver_BatchDeleteFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_BatchDeleteFirewallRule-response-DeleteErrors"></a>
A list of errors that occurred while deleting the firewall rules.
Type: Array of [BatchDeleteFirewallRuleError](API_route53resolver_BatchDeleteFirewallRuleError.md) objects

## Errors
<a name="API_route53resolver_BatchDeleteFirewallRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_BatchDeleteFirewallRule_Examples"></a>

### BatchDeleteFirewallRule Example
<a name="API_route53resolver_BatchDeleteFirewallRule_Example_1"></a>

This example illustrates one usage of BatchDeleteFirewallRule.

#### Sample Request
<a name="API_route53resolver_BatchDeleteFirewallRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 280
X-Amz-Target: Route53Resolver.BatchDeleteFirewallRule
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "DeleteFirewallRuleEntries": [
        {
            "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
            "FirewallDomainListId": "rslvr-fdl-9e956e9bfexample"
        },
        {
            "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
            "FirewallDomainListId": "rslvr-fdl-3b5a094aexample"
        }
    ]
}
```

#### Sample Response
<a name="API_route53resolver_BatchDeleteFirewallRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:03 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 780
x-amzn-RequestId: 6d4c3e5f-7a8b-9c0d-1e2f-3a4b5example
Connection: keep-alive

{
    "DeletedFirewallRules": [
        {
            "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
            "FirewallDomainListId": "rslvr-fdl-9e956e9bfexample",
            "Name": "block-bad-domains-updated",
            "Priority": 150,
            "Action": "BLOCK",
            "BlockResponse": "NXDOMAIN",
            "CreatorRequestId": "batch-create-rule-1",
            "CreationTime": "2026-04-20T12:00:01.000Z",
            "ModificationTime": "2026-04-20T12:00:02.000Z"
        },
        {
            "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
            "FirewallDomainListId": "rslvr-fdl-3b5a094aexample",
            "Name": "allow-safe-domains",
            "Priority": 102,
            "Action": "ALLOW",
            "CreatorRequestId": "batch-create-rule-2",
            "CreationTime": "2026-04-20T12:00:01.000Z",
            "ModificationTime": "2026-04-20T12:00:01.000Z"
        }
    ],
    "DeleteErrors": []
}
```

## See Also
<a name="API_route53resolver_BatchDeleteFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/BatchDeleteFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/BatchDeleteFirewallRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
