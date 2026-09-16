---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteFirewallRule.html
---

# DeleteFirewallRule
<a name="API_route53resolver_DeleteFirewallRule"></a>

Deletes the specified firewall rule. Identify the rule using either `FirewallDomainListId` (for domain-list and DNS Firewall Advanced rules) or `FirewallThreatProtectionId` (for partner-managed and DNS Firewall Advanced rules) — together with `FirewallRuleGroupId`.

 `DeleteFirewallRule` is the only operation that succeeds against a rule whose `Status` is `CREATION_FAILED`.

## Request Syntax
<a name="API_route53resolver_DeleteFirewallRule_RequestSyntax"></a>

```
{
   "FirewallDomainListId": "{{string}}",
   "FirewallRuleGroupId": "{{string}}",
   "FirewallThreatProtectionId": "{{string}}",
   "Qtype": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_DeleteFirewallRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallDomainListId](#API_route53resolver_DeleteFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteFirewallRule-request-FirewallDomainListId"></a>
The ID of the domain list that's used in the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [FirewallRuleGroupId](#API_route53resolver_DeleteFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteFirewallRule-request-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group that you want to delete the rule from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [FirewallThreatProtectionId](#API_route53resolver_DeleteFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteFirewallRule-request-FirewallThreatProtectionId"></a>
 The ID that is created for a DNS Firewall Advanced rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Qtype](#API_route53resolver_DeleteFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteFirewallRule-request-Qtype"></a>
 The DNS query type that the rule you are deleting evaluates. Allowed values are;
+  A: Returns an IPv4 address.
+ AAAA: Returns an Ipv6 address.
+ CAA: Restricts CAs that can create SSL/TLS certifications for the domain.
+ CNAME: Returns another domain name.
+ DS: Record that identifies the DNSSEC signing key of a delegated zone.
+ MX: Specifies mail servers.
+ NAPTR: Regular-expression-based rewriting of domain names.
+ NS: Authoritative name servers.
+ PTR: Maps an IP address to a domain name.
+ SOA: Start of authority record for the zone.
+ SPF: Lists the servers authorized to send emails from a domain.
+ SRV: Application specific values that identify servers.
+ TXT: Verifies email senders and application-specific values.
+ A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## Response Syntax
<a name="API_route53resolver_DeleteFirewallRule_ResponseSyntax"></a>

```
{
   "FirewallRule": {
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
}
```

## Response Elements
<a name="API_route53resolver_DeleteFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRule](#API_route53resolver_DeleteFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_DeleteFirewallRule-response-FirewallRule"></a>
The specification for the firewall rule that you just deleted.
Type: [FirewallRule](API_route53resolver_FirewallRule.md) object

## Errors
<a name="API_route53resolver_DeleteFirewallRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_DeleteFirewallRule_Examples"></a>

### DeleteFirewallRule Example - delete a partner rule by FirewallThreatProtectionId
<a name="API_route53resolver_DeleteFirewallRule_Example_1"></a>

This example illustrates one usage of DeleteFirewallRule.

#### Sample Request
<a name="API_route53resolver_DeleteFirewallRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 138
X-Amz-Target: Route53Resolver.DeleteFirewallRule
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
    "FirewallThreatProtectionId": "rslvr-ftp-1a2b3c4d5example"
}
```

#### Sample Response
<a name="API_route53resolver_DeleteFirewallRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:05 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 540
x-amzn-RequestId: 9f0a1b2c-3d4e-5f6a-7b8c-9d0e1example
Connection: keep-alive

{
    "FirewallRule": {
        "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
        "FirewallThreatProtectionId": "rslvr-ftp-1a2b3c4d5example",
        "Name": "panw-advanced-threat",
        "Priority": 200,
        "Action": "BLOCK",
        "BlockResponse": "NODATA",
        "CreatorRequestId": "create-partner-rule-1",
        "CreationTime": "2026-04-20T12:00:01.000Z",
        "ModificationTime": "2026-04-20T12:00:05.000Z",
        "Status": "CREATION_FAILED",
        "StatusMessage": "Account is not subscribed to the requested AWS Marketplace product.",
        "FirewallRuleType": {
            "PartnerThreatProtection": {
                "Partner": "PANW_MALWARE_DOMAINS"
            }
        }
    }
}
```

## See Also
<a name="API_route53resolver_DeleteFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/DeleteFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DeleteFirewallRule)
