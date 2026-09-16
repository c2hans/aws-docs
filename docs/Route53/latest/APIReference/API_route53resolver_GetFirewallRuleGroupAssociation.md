---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetFirewallRuleGroupAssociation.html
---

# GetFirewallRuleGroupAssociation
<a name="API_route53resolver_GetFirewallRuleGroupAssociation"></a>

Retrieves a firewall rule group association, which enables DNS filtering for a VPC with one rule group. A VPC can have more than one firewall rule group association, and a rule group can be associated with more than one VPC.

## Request Syntax
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_RequestSyntax"></a>

```
{
   "FirewallRuleGroupAssociationId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallRuleGroupAssociationId](#API_route53resolver_GetFirewallRuleGroupAssociation_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallRuleGroupAssociation-request-FirewallRuleGroupAssociationId"></a>
The identifier of the [FirewallRuleGroupAssociation](API_route53resolver_FirewallRuleGroupAssociation.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_ResponseSyntax"></a>

```
{
   "FirewallRuleGroupAssociation": {
      "Arn": "string",
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "FirewallRuleGroupId": "string",
      "Id": "string",
      "ManagedOwnerName": "string",
      "ModificationTime": "string",
      "MutationProtection": "string",
      "Name": "string",
      "Priority": number,
      "Status": "string",
      "StatusMessage": "string",
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallRuleGroupAssociation](#API_route53resolver_GetFirewallRuleGroupAssociation_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetFirewallRuleGroupAssociation-response-FirewallRuleGroupAssociation"></a>
The association that you requested.
Type: [FirewallRuleGroupAssociation](API_route53resolver_FirewallRuleGroupAssociation.md) object

## Errors
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_Errors"></a>

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
<a name="API_route53resolver_GetFirewallRuleGroupAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetFirewallRuleGroupAssociation)
