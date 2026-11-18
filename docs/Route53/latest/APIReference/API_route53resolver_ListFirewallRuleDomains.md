---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallRuleDomains.html
---

# ListFirewallRuleDomains
<a name="API_route53resolver_ListFirewallRuleDomains"></a>

Retrieves the domains of an AutoAllowlist firewall rule. Only the owner of the rule group can call this operation. Results are paginated. Use `MaxResults` and `NextToken` to retrieve additional domains.

Identify the rule by `FirewallThreatProtectionId` to get the domains that DNS Firewall observed in the VPCs that use the rule group, through a rule group association or through a Route 53 Profile that includes the rule group, including VPCs in other accounts. Each domain is returned with its `DomainStatus` and request counts. Use `QueryOptions` to filter and sort the results.

Identify the rule's managed domain list by `FirewallDomainListId` to get the domains that the rule currently allows. For any other domain list, use [ListFirewallDomains](API_route53resolver_ListFirewallDomains.md).

## Request Syntax
<a name="API_route53resolver_ListFirewallRuleDomains_RequestSyntax"></a>

```
{
   "FirewallDomainListId": "{{string}}",
   "FirewallRuleGroupId": "{{string}}",
   "FirewallThreatProtectionId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QueryOptions": {
      "DomainNameFilter": "{{string}}",
      "DomainStatus": "{{string}}",
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_route53resolver_ListFirewallRuleDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallDomainListId](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-FirewallDomainListId"></a>
The ID of the AutoAllowlist rule's managed domain list. Provide this to list the domains that the rule currently allows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [FirewallRuleGroupId](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group that contains the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [FirewallThreatProtectionId](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-FirewallThreatProtectionId"></a>
The threat protection ID that identifies an AutoAllowlist rule. Provide this to list an AutoAllowlist rule's domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [MaxResults](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-MaxResults"></a>
The maximum number of domains that you want to return in a single call. If more domains remain than can be returned, the response includes a `NextToken` value that you can use in a subsequent call to get the next batch. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-NextToken"></a>
For the first call to this operation, omit this value. If more domains remain than can be returned in a single call, the response includes a `NextToken` value. In your next call, specify that value to get the next batch of domains.
Type: String
Required: No

 ** [QueryOptions](#API_route53resolver_ListFirewallRuleDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-request-QueryOptions"></a>
Optional filters and sort order for the returned domains. If you don't specify this, the operation returns the `OBSERVED` domains sorted by `TIME_ADDED` in descending order. See [ListFirewallRuleDomainsQueryOptions](API_route53resolver_ListFirewallRuleDomainsQueryOptions.md).
Type: [ListFirewallRuleDomainsQueryOptions](API_route53resolver_ListFirewallRuleDomainsQueryOptions.md) object
Required: No

## Response Syntax
<a name="API_route53resolver_ListFirewallRuleDomains_ResponseSyntax"></a>

```
{
   "Domains": [
      {
         "AddedTime": "string",
         "DomainName": "string",
         "DomainStatus": "string",
         "Last24HourRequests": number,
         "TotalRequests": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_route53resolver_ListFirewallRuleDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domains](#API_route53resolver_ListFirewallRuleDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-response-Domains"></a>
The domains for the rule. See [FirewallRuleDomain](API_route53resolver_FirewallRuleDomain.md).
Type: Array of [FirewallRuleDomain](API_route53resolver_FirewallRuleDomain.md) objects

 ** [NextToken](#API_route53resolver_ListFirewallRuleDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallRuleDomains-response-NextToken"></a>
If more domains remain than were returned in this response, DNS Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of domains.
Type: String

## Errors
<a name="API_route53resolver_ListFirewallRuleDomains_Errors"></a>

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
<a name="API_route53resolver_ListFirewallRuleDomains_Examples"></a>

### ListFirewallRuleDomains Example
<a name="API_route53resolver_ListFirewallRuleDomains_Example_1"></a>

This example illustrates one usage of ListFirewallRuleDomains.

#### Sample Request
<a name="API_route53resolver_ListFirewallRuleDomains_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
X-Amz-Target: Route53Resolver.ListFirewallRuleDomains
Content-Type: application/x-amz-json-1.1

{
    "FirewallRuleGroupId": "rslvr-frg-abc123",
    "FirewallThreatProtectionId": "rslvr-ftp-def456",
    "QueryOptions": {
        "DomainStatus": "OBSERVED",
        "SortBy": "TIME_ADDED",
        "SortOrder": "DESC",
        "DomainNameFilter": "amazon"
    },
    "MaxResults": 100
}
```

#### Sample Response
<a name="API_route53resolver_ListFirewallRuleDomains_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1

{
    "Domains": [
        {
            "DomainName": "photos.s3.us-east-1.amazonaws.com",
            "DomainStatus": "OBSERVED",
            "Last24HourRequests": 2000,
            "TotalRequests": 48000,
            "AddedTime": "2026-06-09T14:00:00Z"
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListFirewallRuleDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListFirewallRuleDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListFirewallRuleDomains)
