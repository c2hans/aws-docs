---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverDnssecConfig.html
---

# UpdateResolverDnssecConfig
<a name="API_route53resolver_UpdateResolverDnssecConfig"></a>

Updates an existing DNSSEC validation configuration. If there is no existing DNSSEC validation configuration, one is created.

## Request Syntax
<a name="API_route53resolver_UpdateResolverDnssecConfig_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "Validation": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_UpdateResolverDnssecConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_route53resolver_UpdateResolverDnssecConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverDnssecConfig-request-ResourceId"></a>
The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation status for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Validation](#API_route53resolver_UpdateResolverDnssecConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverDnssecConfig-request-Validation"></a>
The new value that you are specifying for DNSSEC validation for the VPC. The value can be `ENABLE` or `DISABLE`. Be aware that it can take time for a validation status change to be completed.
Type: String
Valid Values: `ENABLE | DISABLE | USE_LOCAL_RESOURCE_SETTING`
Required: Yes

## Response Syntax
<a name="API_route53resolver_UpdateResolverDnssecConfig_ResponseSyntax"></a>

```
{
   "ResolverDNSSECConfig": {
      "Id": "string",
      "OwnerId": "string",
      "ResourceId": "string",
      "ValidationStatus": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_UpdateResolverDnssecConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverDNSSECConfig](#API_route53resolver_UpdateResolverDnssecConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverDnssecConfig-response-ResolverDNSSECConfig"></a>
A complex type that contains settings for the specified DNSSEC configuration.
Type: [ResolverDnssecConfig](API_route53resolver_ResolverDnssecConfig.md) object

## Errors
<a name="API_route53resolver_UpdateResolverDnssecConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
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
<a name="API_route53resolver_UpdateResolverDnssecConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/UpdateResolverDnssecConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateResolverDnssecConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
