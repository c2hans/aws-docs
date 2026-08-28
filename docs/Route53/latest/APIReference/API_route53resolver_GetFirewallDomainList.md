---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallDomainList.html
---

# GetFirewallDomainList
<a name="API_route53resolver_GetFirewallDomainList"></a>

Retrieves the specified firewall domain list.

## Request Syntax
<a name="API_route53resolver_GetFirewallDomainList_RequestSyntax"></a>

```
{
   "FirewallDomainListId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetFirewallDomainList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallDomainListId](#API_route53resolver_GetFirewallDomainList_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallDomainList-request-FirewallDomainListId"></a>
The ID of the domain list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetFirewallDomainList_ResponseSyntax"></a>

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
<a name="API_route53resolver_GetFirewallDomainList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallDomainList](#API_route53resolver_GetFirewallDomainList_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallDomainList-response-FirewallDomainList"></a>
The domain list that you requested.
Type: [FirewallDomainList](API_route53resolver_FirewallDomainList.md) object

## Errors
<a name="API_route53resolver_GetFirewallDomainList_Errors"></a>

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

## See Also
<a name="API_route53resolver_GetFirewallDomainList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetFirewallDomainList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetFirewallDomainList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
