---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverDnssecConfigs.html
---

# ListResolverDnssecConfigs
<a name="API_route53resolver_ListResolverDnssecConfigs"></a>

Lists the configurations for DNSSEC validation that are associated with the current AWS account.

## Request Syntax
<a name="API_route53resolver_ListResolverDnssecConfigs_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListResolverDnssecConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_route53resolver_ListResolverDnssecConfigs_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverDnssecConfigs-request-Filters"></a>
An optional specification to return a subset of objects.
Type: Array of [Filter](API_route53resolver_Filter.md) objects
Required: No

 ** [MaxResults](#API_route53resolver_ListResolverDnssecConfigs_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverDnssecConfigs-request-MaxResults"></a>
 *Optional*: An integer that specifies the maximum number of DNSSEC configuration results that you want Amazon Route 53 to return. If you don't specify a value for `MaxResults`, Route 53 returns up to 100 configuration per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverDnssecConfigs_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverDnssecConfigs-request-NextToken"></a>
(Optional) If the current AWS account has more than `MaxResults` DNSSEC configurations, use `NextToken` to get the second and subsequent pages of results.
For the first `ListResolverDnssecConfigs` request, omit this value.
For the second and subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverDnssecConfigs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResolverDnssecConfigs": [
      {
         "Id": "string",
         "OwnerId": "string",
         "ResourceId": "string",
         "ValidationStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListResolverDnssecConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53resolver_ListResolverDnssecConfigs_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverDnssecConfigs-response-NextToken"></a>
If a response includes the last of the DNSSEC configurations that are associated with the current AWS account, `NextToken` doesn't appear in the response.
If a response doesn't include the last of the configurations, you can get more configurations by submitting another [ListResolverDnssecConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResolverDnssecConfigs.html) request. Get the value of `NextToken` that Amazon Route 53 returned in the previous response and include it in `NextToken` in the next request.
Type: String

 ** [ResolverDnssecConfigs](#API_route53resolver_ListResolverDnssecConfigs_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverDnssecConfigs-response-ResolverDnssecConfigs"></a>
An array that contains one [ResolverDnssecConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResolverDnssecConfig.html) element for each configuration for DNSSEC validation that is associated with the current AWS account. It doesn't contain disabled DNSSEC configurations for the resource.
Type: Array of [ResolverDnssecConfig](API_route53resolver_ResolverDnssecConfig.md) objects

## Errors
<a name="API_route53resolver_ListResolverDnssecConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The current account doesn't have the IAM permissions required to perform the specified Resolver operation.
This error can also be thrown when a customer has reached the 5120 character limit for a resource policy for CloudWatch Logs.
HTTP Status Code: 400

 ** InternalServiceErrorException **
We encountered an unknown error. Try again in a few minutes.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The value that you specified for `NextToken` in a `List` request isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters in this request are not valid.
 ** FieldName **
For an `InvalidParameterException` error, the name of the parameter that's invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## See Also
<a name="API_route53resolver_ListResolverDnssecConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverDnssecConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverDnssecConfigs)
