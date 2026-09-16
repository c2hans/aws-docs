---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverConfigs.html
---

# ListResolverConfigs
<a name="API_route53resolver_ListResolverConfigs"></a>

Retrieves the Resolver configurations that you have defined. Route 53 Resolver uses the configurations to manage DNS resolution behavior for your VPCs.

## Request Syntax
<a name="API_route53resolver_ListResolverConfigs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListResolverConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListResolverConfigs_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverConfigs-request-MaxResults"></a>
The maximum number of Resolver configurations that you want to return in the response to a `ListResolverConfigs` request. If you don't specify a value for `MaxResults`, up to 100 Resolver configurations are returned.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverConfigs_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverConfigs-request-NextToken"></a>
(Optional) If the current AWS account has more than `MaxResults` Resolver configurations, use `NextToken` to get the second and subsequent pages of results.
For the first `ListResolverConfigs` request, omit this value.
For the second and subsequent requests, get the value of `NextToken` from the previous response and specify that value for `NextToken` in the request.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverConfigs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResolverConfigs": [
      {
         "AutodefinedReverse": "string",
         "Id": "string",
         "OwnerId": "string",
         "ResourceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListResolverConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53resolver_ListResolverConfigs_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverConfigs-response-NextToken"></a>
If a response includes the last of the Resolver configurations that are associated with the current AWS account, `NextToken` doesn't appear in the response.
If a response doesn't include the last of the configurations, you can get more configurations by submitting another `ListResolverConfigs` request. Get the value of `NextToken` that Amazon Route 53 returned in the previous response and include it in `NextToken` in the next request.
Type: String

 ** [ResolverConfigs](#API_route53resolver_ListResolverConfigs_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverConfigs-response-ResolverConfigs"></a>
An array that contains one `ResolverConfigs` element for each Resolver configuration that is associated with the current AWS account.
Type: Array of [ResolverConfig](API_route53resolver_ResolverConfig.md) objects

## Errors
<a name="API_route53resolver_ListResolverConfigs_Errors"></a>

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

 ** ValidationException **
You have provided an invalid command. If you ran the `UpdateFirewallDomains` request. supported values are `ADD`, `REMOVE`, or `REPLACE` a domain.
HTTP Status Code: 400

## See Also
<a name="API_route53resolver_ListResolverConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverConfigs)
