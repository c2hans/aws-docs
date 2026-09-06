---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomains.html
---

# ListFirewallDomains
<a name="API_route53resolver_ListFirewallDomains"></a>

Retrieves the domains that you have defined for the specified firewall domain list.

A single call might return only a partial list of the domains. For information, see `MaxResults`.

## Request Syntax
<a name="API_route53resolver_ListFirewallDomains_RequestSyntax"></a>

```
{
   "FirewallDomainListId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListFirewallDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallDomainListId](#API_route53resolver_ListFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomains-request-FirewallDomainListId"></a>
The ID of the domain list whose domains you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [MaxResults](#API_route53resolver_ListFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomains-request-MaxResults"></a>
The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
If you don't specify a value for `MaxResults`, Resolver returns up to 100 objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [NextToken](#API_route53resolver_ListFirewallDomains_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomains-request-NextToken"></a>
For the first call to this list request, omit this value.
When you request a list of objects, Resolver returns at most the number of objects specified in `MaxResults`. If more objects are available for retrieval, Resolver returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListFirewallDomains_ResponseSyntax"></a>

```
{
   "Domains": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_route53resolver_ListFirewallDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domains](#API_route53resolver_ListFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomains-response-Domains"></a>
A list of the domains in the firewall domain list.
This might be a partial list of the domains that you've defined in the domain list. For information, see `MaxResults`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [NextToken](#API_route53resolver_ListFirewallDomains_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomains-response-NextToken"></a>
If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.
Type: String

## Errors
<a name="API_route53resolver_ListFirewallDomains_Errors"></a>

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

## See Also
<a name="API_route53resolver_ListFirewallDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListFirewallDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListFirewallDomains)
