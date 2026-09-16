---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListFirewallDomainLists.html
---

# ListFirewallDomainLists
<a name="API_route53resolver_ListFirewallDomainLists"></a>

Retrieves the firewall domain lists that you have defined. For each firewall domain list, you can retrieve the domains that are defined for a list by calling [ListFirewallDomains](API_route53resolver_ListFirewallDomains.md).

A single call to this list operation might return only a partial list of the domain lists. For information, see `MaxResults`.

## Request Syntax
<a name="API_route53resolver_ListFirewallDomainLists_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListFirewallDomainLists_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListFirewallDomainLists_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomainLists-request-MaxResults"></a>
The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
If you don't specify a value for `MaxResults`, Resolver returns up to 100 objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListFirewallDomainLists_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomainLists-request-NextToken"></a>
For the first call to this list request, omit this value.
When you request a list of objects, Resolver returns at most the number of objects specified in `MaxResults`. If more objects are available for retrieval, Resolver returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListFirewallDomainLists_ResponseSyntax"></a>

```
{
   "FirewallDomainLists": [
      {
         "Arn": "string",
         "Category": "string",
         "CreatorRequestId": "string",
         "Id": "string",
         "ManagedListType": "string",
         "ManagedOwnerName": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_route53resolver_ListFirewallDomainLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallDomainLists](#API_route53resolver_ListFirewallDomainLists_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomainLists-response-FirewallDomainLists"></a>
A list of the domain lists that you have defined.
This might be a partial list of the domain lists that you've defined. For information, see `MaxResults`.
Type: Array of [FirewallDomainListMetadata](API_route53resolver_FirewallDomainListMetadata.md) objects

 ** [NextToken](#API_route53resolver_ListFirewallDomainLists_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListFirewallDomainLists-response-NextToken"></a>
If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.
Type: String

## Errors
<a name="API_route53resolver_ListFirewallDomainLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## See Also
<a name="API_route53resolver_ListFirewallDomainLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListFirewallDomainLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListFirewallDomainLists)
