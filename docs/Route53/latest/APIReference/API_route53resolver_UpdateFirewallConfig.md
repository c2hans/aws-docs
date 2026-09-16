---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateFirewallConfig.html
---

# UpdateFirewallConfig
<a name="API_route53resolver_UpdateFirewallConfig"></a>

Updates the configuration of the firewall behavior provided by DNS Firewall for a single VPC from Amazon Virtual Private Cloud (Amazon VPC).

## Request Syntax
<a name="API_route53resolver_UpdateFirewallConfig_RequestSyntax"></a>

```
{
   "FirewallFailOpen": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_UpdateFirewallConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallFailOpen](#API_route53resolver_UpdateFirewallConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallConfig-request-FirewallFailOpen"></a>
Determines how Route 53 Resolver handles queries during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply.
+ By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall blocks queries that it is unable to evaluate properly.
+ If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them.
This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association.
Type: String
Valid Values: `ENABLED | DISABLED | USE_LOCAL_RESOURCE_SETTING`
Required: Yes

 ** [ResourceId](#API_route53resolver_UpdateFirewallConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallConfig-request-ResourceId"></a>
The ID of the VPC that the configuration is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_UpdateFirewallConfig_ResponseSyntax"></a>

```
{
   "FirewallConfig": {
      "FirewallFailOpen": "string",
      "Id": "string",
      "OwnerId": "string",
      "ResourceId": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_UpdateFirewallConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallConfig](#API_route53resolver_UpdateFirewallConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_UpdateFirewallConfig-response-FirewallConfig"></a>
Configuration of the firewall behavior provided by DNS Firewall for a single VPC.
Type: [FirewallConfig](API_route53resolver_FirewallConfig.md) object

## Errors
<a name="API_route53resolver_UpdateFirewallConfig_Errors"></a>

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
<a name="API_route53resolver_UpdateFirewallConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/UpdateFirewallConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateFirewallConfig)
