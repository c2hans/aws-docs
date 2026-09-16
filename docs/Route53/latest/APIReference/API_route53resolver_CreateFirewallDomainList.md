---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallDomainList.html
---

# CreateFirewallDomainList
<a name="API_route53resolver_CreateFirewallDomainList"></a>

Creates an empty firewall domain list for use in DNS Firewall rules. You can populate the domains for the new list with a file, using [ImportFirewallDomains](API_route53resolver_ImportFirewallDomains.md), or with domain strings, using [UpdateFirewallDomains](API_route53resolver_UpdateFirewallDomains.md).

## Request Syntax
<a name="API_route53resolver_CreateFirewallDomainList_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_CreateFirewallDomainList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateFirewallDomainList-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows you to retry failed requests without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Name](#API_route53resolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateFirewallDomainList-request-Name"></a>
A name that lets you identify the domain list to manage and use it.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [Tags](#API_route53resolver_CreateFirewallDomainList_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateFirewallDomainList-request-Tags"></a>
A list of the tag keys and values that you want to associate with the domain list.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_route53resolver_CreateFirewallDomainList_ResponseSyntax"></a>

```
{
   "FirewallDomainList": {
      "Arn": "string",
      "Category": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "DomainCount": number,
      "Id": "string",
      "ManagedListType": "string",
      "ManagedOwnerName": "string",
      "ModificationTime": "string",
      "Name": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_CreateFirewallDomainList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallDomainList](#API_route53resolver_CreateFirewallDomainList_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_CreateFirewallDomainList-response-FirewallDomainList"></a>
The domain list that you just created.
Type: [FirewallDomainList](API_route53resolver_FirewallDomainList.md) object

## Errors
<a name="API_route53resolver_CreateFirewallDomainList_Errors"></a>

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

## See Also
<a name="API_route53resolver_CreateFirewallDomainList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/CreateFirewallDomainList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateFirewallDomainList)
