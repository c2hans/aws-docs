---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroup.html
---

# GetFirewallRuleGroup
<a name="API_route53resolver_GetFirewallRuleGroup"></a>

Retrieves the specified firewall rule group.

## Request Syntax
<a name="API_route53resolver_GetFirewallRuleGroup_RequestSyntax"></a>

```
{
   "FirewallRuleGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetFirewallRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallRuleGroupId](#API_route53resolver_GetFirewallRuleGroup_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallRuleGroup-request-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetFirewallRuleGroup_ResponseSyntax"></a>

```
{
   "FirewallRuleGroup": {
      "Arn": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "Id": "string",
      "ModificationTime": "string",
      "Name": "string",
      "OwnerId": "string",
      "RuleCount": number,
      "ShareStatus": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_GetFirewallRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRuleGroup](#API_route53resolver_GetFirewallRuleGroup_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallRuleGroup-response-FirewallRuleGroup"></a>
A collection of rules used to filter DNS network traffic.
Type: [FirewallRuleGroup](API_route53resolver_FirewallRuleGroup.md) object

## Errors
<a name="API_route53resolver_GetFirewallRuleGroup_Errors"></a>

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
<a name="API_route53resolver_GetFirewallRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetFirewallRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetFirewallRuleGroup)
