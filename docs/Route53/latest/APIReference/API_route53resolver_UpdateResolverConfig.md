---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverConfig.html
---

# UpdateResolverConfig
<a name="API_route53resolver_UpdateResolverConfig"></a>

Updates the behavior configuration of Amazon Route 53 Resolver behavior for a single VPC from Amazon Virtual Private Cloud.

## Request Syntax
<a name="API_route53resolver_UpdateResolverConfig_RequestSyntax"></a>

```
{
   "AutodefinedReverseFlag": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_UpdateResolverConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutodefinedReverseFlag](#API_route53resolver_UpdateResolverConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverConfig-request-AutodefinedReverseFlag"></a>
Indicates whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. Disabling this option will also affect EC2-Classic instances using ClassicLink. For more information, see [ClassicLink](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html) in the *Amazon EC2 guide*.
We are retiring EC2-Classic on August 15, 2022. We recommend that you migrate from EC2-Classic to a VPC. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 guide* and the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/).
It can take some time for the status change to be completed.

Type: String
Valid Values: `ENABLE | DISABLE | USE_LOCAL_RESOURCE_SETTING`
Required: Yes

 ** [ResourceId](#API_route53resolver_UpdateResolverConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverConfig-request-ResourceId"></a>
The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_UpdateResolverConfig_ResponseSyntax"></a>

```
{
   "ResolverConfig": {
      "AutodefinedReverse": "string",
      "Id": "string",
      "OwnerId": "string",
      "ResourceId": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_UpdateResolverConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverConfig](#API_route53resolver_UpdateResolverConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_UpdateResolverConfig-response-ResolverConfig"></a>
An array that contains settings for the specified Resolver configuration.
Type: [ResolverConfig](API_route53resolver_ResolverConfig.md) object

## Errors
<a name="API_route53resolver_UpdateResolverConfig_Errors"></a>

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

 ** LimitExceededException **
The request caused one or more limits to be exceeded.
 ** ResourceType **
For a `LimitExceededException` error, the type of resource that exceeded the current limit.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ResourceUnavailableException **
The specified resource isn't available.
 ** ResourceType **
For a `ResourceUnavailableException` error, the type of resource that isn't available.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## See Also
<a name="API_route53resolver_UpdateResolverConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/UpdateResolverConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateResolverConfig)
