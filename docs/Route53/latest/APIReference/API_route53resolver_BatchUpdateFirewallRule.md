---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_BatchUpdateFirewallRule.html
---

# BatchUpdateFirewallRule
<a name="API_route53resolver_BatchUpdateFirewallRule"></a>

Updates multiple DNS Firewall rules in the specified rule group.

## Request Syntax
<a name="API_route53resolver_BatchUpdateFirewallRule_RequestSyntax"></a>

```
{
   "UpdateFirewallRuleEntries": [
      {
         "Action": "{{string}}",
         "BlockOverrideDnsType": "{{string}}",
         "BlockOverrideDomain": "{{string}}",
         "BlockOverrideTtl": {{number}},
         "BlockResponse": "{{string}}",
         "ConfidenceThreshold": "{{string}}",
         "DnsThreatProtection": "{{string}}",
         "FirewallDomainListId": "{{string}}",
         "FirewallDomainRedirectionAction": "{{string}}",
         "FirewallRuleGroupId": "{{string}}",
         "FirewallRuleType": {
            "DnsThreatProtection": {
               "ConfidenceThreshold": "{{string}}",
               "Value": "{{string}}"
            },
            "FirewallAdvancedContentCategory": {
               "Category": "{{string}}"
            },
            "FirewallAdvancedThreatCategory": {
               "Category": "{{string}}"
            },
            "PartnerThreatProtection": {
               "Partner": "{{string}}"
            }
         },
         "FirewallThreatProtectionId": "{{string}}",
         "Name": "{{string}}",
         "Priority": {{number}},
         "Qtype": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_BatchUpdateFirewallRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [UpdateFirewallRuleEntries](#API_route53resolver_BatchUpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_BatchUpdateFirewallRule-request-UpdateFirewallRuleEntries"></a>
The list of firewall rules to update.
Type: Array of [UpdateFirewallRuleEntry](API_route53resolver_UpdateFirewallRuleEntry.md) objects
Required: Yes

## Response Syntax
<a name="API_route53resolver_BatchUpdateFirewallRule_ResponseSyntax"></a>

```
{
   "UpdatedFirewallRules": [
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
   "UpdateErrors": [
      {
         "Code": "string",
         "FirewallRule": {
            "Action": "string",
            "BlockOverrideDnsType": "string",
            "BlockOverrideDomain": "string",
            "BlockOverrideTtl": number,
            "BlockResponse": "string",
            "ConfidenceThreshold": "string",
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
            "Name": "string",
            "Priority": number,
            "Qtype": "string"
         },
         "Message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_BatchUpdateFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UpdatedFirewallRules](#API_route53resolver_BatchUpdateFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_BatchUpdateFirewallRule-response-UpdatedFirewallRules"></a>
The firewall rules that were successfully updated by the request.
Type: Array of [FirewallRule](API_route53resolver_FirewallRule.md) objects

 ** [UpdateErrors](#API_route53resolver_BatchUpdateFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_BatchUpdateFirewallRule-response-UpdateErrors"></a>
A list of errors that occurred while updating the firewall rules.
Type: Array of [BatchUpdateFirewallRuleError](API_route53resolver_BatchUpdateFirewallRuleError.md) objects

## Errors
<a name="API_route53resolver_BatchUpdateFirewallRule_Errors"></a>

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
<a name="API_route53resolver_BatchUpdateFirewallRule_Examples"></a>

### BatchUpdateFirewallRule Example
<a name="API_route53resolver_BatchUpdateFirewallRule_Example_1"></a>

This example illustrates one usage of BatchUpdateFirewallRule.

#### Sample Request
<a name="API_route53resolver_BatchUpdateFirewallRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 312
X-Amz-Target: Route53Resolver.BatchUpdateFirewallRule
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "UpdateFirewallRuleEntries": [
        {
            "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
            "FirewallDomainListId": "rslvr-fdl-9e956e9bfexample",
            "Priority": 150,
            "Action": "BLOCK",
            "BlockResponse": "NXDOMAIN",
            "Name": "block-bad-domains-updated"
        }
    ]
}
```

#### Sample Response
<a name="API_route53resolver_BatchUpdateFirewallRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 520
x-amzn-RequestId: 5c3b2d4e-6f7a-8b9c-0d1e-2f3a4example
Connection: keep-alive

{
    "UpdatedFirewallRules": [
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
        }
    ],
    "UpdateErrors": []
}
```

## See Also
<a name="API_route53resolver_BatchUpdateFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/BatchUpdateFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/BatchUpdateFirewallRule)
