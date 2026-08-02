---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallRule.html
---

# UpdateFirewallRule
<a name="API_route53resolver_UpdateFirewallRule"></a>

Updates the specified firewall rule. The rule's `FirewallRuleType`, `FirewallDomainListId`, and top-level `DnsThreatProtection` match source cannot be changed after creation. Rules whose `Status` is `CREATING` or `CREATION_FAILED` cannot be updated; remove a failed rule with [DeleteFirewallRule](API_route53resolver_DeleteFirewallRule.md).

## Request Syntax
<a name="API_route53resolver_UpdateFirewallRule_RequestSyntax"></a>

```
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
```

## Request Parameters
<a name="API_route53resolver_UpdateFirewallRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-Action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:
+  `ALLOW` - Permit the request to go through. Not available for DNS Firewall Advanced rules.
+  `ALERT` - Permit the request to go through but send an alert to the logs.
+  `BLOCK` - Disallow the request. This option requires additional details in the rule's `BlockResponse`.
Type: String
Valid Values: `ALLOW | BLOCK | ALERT`
Required: No

 ** [BlockOverrideDnsType](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-BlockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Valid Values: `CNAME`
Required: No

 ** [BlockOverrideDomain](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-BlockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [BlockOverrideTtl](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-BlockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** [BlockResponse](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-BlockResponse"></a>
The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK`.
+  `NODATA` - Respond indicating that the query was successful, but no response is available for it.
+  `NXDOMAIN` - Respond indicating that the domain name that's in the query doesn't exist.
+  `OVERRIDE` - Provide a custom override in the response. This option requires custom handling details in the rule's `BlockOverride*` settings.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** [ConfidenceThreshold](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-ConfidenceThreshold"></a>
 The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean:
+  `LOW`: Provides the highest detection rate for threats, but also increases false positives.
+  `MEDIUM`: Provides a balance between detecting threats and false positives.
+  `HIGH`: Detects only the most well corroborated threats with a low rate of false positives.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** [DnsThreatProtection](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-DnsThreatProtection"></a>
 The type of the DNS Firewall Advanced rule. This setting is mutually exclusive with `FirewallDomainListId` and `FirewallRuleType`. Valid values are:
+  `DGA`: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.
+  `DNS_TUNNELING`: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.
+  `DICTIONARY_DGA`: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** [FirewallDomainListId](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-FirewallDomainListId"></a>
The ID of the domain list to use in the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [FirewallDomainRedirectionAction](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-FirewallDomainRedirectionAction"></a>
 How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME.
 `INSPECT_REDIRECTION_DOMAIN`: (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.
 `TRUST_REDIRECTION_DOMAIN`: Inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the domain in the redirection list to the domain list.
Type: String
Valid Values: `INSPECT_REDIRECTION_DOMAIN | TRUST_REDIRECTION_DOMAIN`
Required: No

 ** [FirewallRuleGroupId](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [FirewallRuleType](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-FirewallRuleType"></a>
The rule type configuration for the firewall rule. This is a tagged union — set exactly one of its members. This setting is mutually exclusive with the top-level `FirewallDomainListId` and `DnsThreatProtection` fields. Use one of:
+  `FirewallAdvancedContentCategory` — match an AWS-managed content category (for example, `VIOLENCE_AND_HATE_SPEECH`).
+  `FirewallAdvancedThreatCategory` — match an AWS-managed advanced threat category (for example, `PHISHING`).
+  `DnsThreatProtection` — match a built-in DNS Firewall Advanced threat detector (`DGA`, `DNS_TUNNELING`, or `DICTIONARY_DGA`).
+  `PartnerThreatProtection` — match a third-party threat feed delivered through AWS Marketplace. The selected partner must be an active subscription on the calling account.
To enumerate the values supported in your account, call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md).
Type: [FirewallRuleType](API_route53resolver_FirewallRuleType.md) object
Required: No

 ** [FirewallThreatProtectionId](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-FirewallThreatProtectionId"></a>
 The DNS Firewall Advanced rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Name](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-Name"></a>
The name of the rule.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** [Priority](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-Priority"></a>
The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
You must specify a unique priority for each rule in a rule group. To make it easier to insert rules later, leave space between the numbers, for example, use 100, 200, and so on. You can change the priority setting for the rules in a rule group at any time.
Type: Integer
Required: No

 ** [Qtype](#API_route53resolver_UpdateFirewallRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-request-Qtype"></a>
 The DNS query type you want the rule to evaluate. Allowed values are;
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
**Note**
If you set up a firewall BLOCK rule with action NXDOMAIN on query type equals AAAA, this action will not be applied to synthetic IPv6 addresses generated when DNS64 is enabled.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## Response Syntax
<a name="API_route53resolver_UpdateFirewallRule_ResponseSyntax"></a>

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
<a name="API_route53resolver_UpdateFirewallRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRule](#API_route53resolver_UpdateFirewallRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallRule-response-FirewallRule"></a>
The firewall rule that you just updated.
Type: [FirewallRule](API_route53resolver_FirewallRule.md) object

## Errors
<a name="API_route53resolver_UpdateFirewallRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** ConflictException **
The requested state transition isn't valid. For example, you can't delete a firewall domain list if it is in the process of being deleted, or you can't import domains into a domain list that is in the process of being deleted.
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
<a name="API_route53resolver_UpdateFirewallRule_Examples"></a>

### UpdateFirewallRule Example
<a name="API_route53resolver_UpdateFirewallRule_Example_1"></a>

This example illustrates one usage of UpdateFirewallRule.

#### Sample Request
<a name="API_route53resolver_UpdateFirewallRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 200
X-Amz-Target: Route53Resolver.UpdateFirewallRule
X-Amz-Date: 20260420T120000Z
User-Agent: aws-cli/2.15.0 Python/3.11.6
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20260420/us-east-1/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
    "FirewallDomainListId": "rslvr-fdl-9e956e9bfexample",
    "Priority": 150,
    "Action": "BLOCK",
    "BlockResponse": "NXDOMAIN",
    "Name": "block-bad-domains-updated"
}
```

#### Sample Response
<a name="API_route53resolver_UpdateFirewallRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Sun, 20 Apr 2026 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 460
x-amzn-RequestId: 5c4d3e2f-1a0b-9c8d-7e6f-5a4b3example
Connection: keep-alive

{
    "FirewallRule": {
        "FirewallRuleGroupId": "rslvr-frg-47f93271fexample",
        "FirewallDomainListId": "rslvr-fdl-9e956e9bfexample",
        "Name": "block-bad-domains-updated",
        "Priority": 150,
        "Action": "BLOCK",
        "BlockResponse": "NXDOMAIN",
        "CreatorRequestId": "create-rule-1",
        "CreationTime": "2026-04-20T12:00:01.000Z",
        "ModificationTime": "2026-04-20T12:00:02.000Z"
    }
}
```

## See Also
<a name="API_route53resolver_UpdateFirewallRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/UpdateFirewallRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateFirewallRule)
