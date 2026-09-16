---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListOutpostResolvers.html
---

# ListOutpostResolvers
<a name="API_route53resolver_ListOutpostResolvers"></a>

Lists all the Resolvers on Outposts that were created using the current AWS account.

## Request Syntax
<a name="API_route53resolver_ListOutpostResolvers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OutpostArn": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListOutpostResolvers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListOutpostResolvers_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListOutpostResolvers-request-MaxResults"></a>
The maximum number of Resolvers on the Outpost that you want to return in the response to a `ListOutpostResolver` request. If you don't specify a value for `MaxResults`, the request returns up to 100 Resolvers.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListOutpostResolvers_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListOutpostResolvers-request-NextToken"></a>
For the first `ListOutpostResolver` request, omit this value.

Type: String
Required: No

 ** [OutpostArn](#API_route53resolver_ListOutpostResolvers_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListOutpostResolvers-request-OutpostArn"></a>
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

## Response Syntax
<a name="API_route53resolver_ListOutpostResolvers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OutpostResolvers": [
      {
         "Arn": "string",
         "CreationTime": "string",
         "CreatorRequestId": "string",
         "Id": "string",
         "InstanceCount": number,
         "ModificationTime": "string",
         "Name": "string",
         "OutpostArn": "string",
         "PreferredInstanceType": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListOutpostResolvers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53resolver_ListOutpostResolvers_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListOutpostResolvers-response-NextToken"></a>
If more than `MaxResults` Resolvers match the specified criteria, you can submit another `ListOutpostResolver` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [OutpostResolvers](#API_route53resolver_ListOutpostResolvers_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListOutpostResolvers-response-OutpostResolvers"></a>
The Resolvers on Outposts that were created by using the current AWS account, and that match the specified filters, if any.
Type: Array of [OutpostResolver](API_route53resolver_OutpostResolver.md) objects

## Errors
<a name="API_route53resolver_ListOutpostResolvers_Errors"></a>

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
<a name="API_route53resolver_ListOutpostResolvers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListOutpostResolvers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListOutpostResolvers)
