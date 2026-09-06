---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html
---

# ListResolverRules
<a name="API_route53resolver_ListResolverRules"></a>

Lists the Resolver rules that were created using the current AWS account.

## Request Syntax
<a name="API_route53resolver_ListResolverRules_RequestSyntax"></a>

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
<a name="API_route53resolver_ListResolverRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_route53resolver_ListResolverRules_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-request-Filters"></a>
An optional specification to return a subset of Resolver rules, such as all Resolver rules that are associated with the same Resolver endpoint.
If you submit a second or subsequent `ListResolverRules` request and specify the `NextToken` parameter, you must use the same values for `Filters`, if any, as in the previous request.
Type: Array of [Filter](API_route53resolver_Filter.md) objects
Required: No

 ** [MaxResults](#API_route53resolver_ListResolverRules_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-request-MaxResults"></a>
The maximum number of Resolver rules that you want to return in the response to a `ListResolverRules` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 Resolver rules.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverRules_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-request-NextToken"></a>
For the first `ListResolverRules` request, omit this value.
If you have more than `MaxResults` Resolver rules, you can submit another `ListResolverRules` request to get the next group of Resolver rules. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverRules_ResponseSyntax"></a>

```
{
   "MaxResults": number,
   "NextToken": "string",
   "ResolverRules": [
      {
         "Arn": "string",
         "CreationTime": "string",
         "CreatorRequestId": "string",
         "DelegationRecord": "string",
         "DomainName": "string",
         "Id": "string",
         "ModificationTime": "string",
         "Name": "string",
         "OwnerId": "string",
         "ResolverEndpointId": "string",
         "RuleType": "string",
         "ShareStatus": "string",
         "Status": "string",
         "StatusMessage": "string",
         "TargetIps": [
            {
               "Ip": "string",
               "Ipv6": "string",
               "Port": number,
               "Protocol": "string",
               "ServerNameIndication": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListResolverRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaxResults](#API_route53resolver_ListResolverRules_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-response-MaxResults"></a>
The value that you specified for `MaxResults` in the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53resolver_ListResolverRules_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-response-NextToken"></a>
If more than `MaxResults` Resolver rules match the specified criteria, you can submit another `ListResolverRules` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ResolverRules](#API_route53resolver_ListResolverRules_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverRules-response-ResolverRules"></a>
The Resolver rules that were created using the current AWS account and that match the specified filters, if any.
Type: Array of [ResolverRule](API_route53resolver_ResolverRule.md) objects

## Errors
<a name="API_route53resolver_ListResolverRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_route53resolver_ListResolverRules_Examples"></a>

### ListResolverRules Example
<a name="API_route53resolver_ListResolverRules_Example_1"></a>

This example illustrates one usage of ListResolverRules.

#### Sample Request
<a name="API_route53resolver_ListResolverRules_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: Route53Resolver.ListResolverRules
X-Amz-Date: 20181101T192600Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{}
```

#### Sample Response
<a name="API_route53resolver_ListResolverRules_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:26:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 483
x-amzn-RequestId: cfa09aaa-6619-40d4-8791-064c6example
Connection: keep-alive

{
    "MaxResults": 30,
    "ResolverRules": [
        {
            "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample",
            "CreatorRequestId": "999",
            "DomainName": "example.com",
            "Id": "rslvr-rr-5328a0899aexample",
            "OwnerId": "123456789012",
            "ResolverEndpointId": "rslvr-out-fdc049932dexample",
            "RuleType": "FORWARD",
            "Status": "COMPLETE",
            "StatusMessage": "[Trace id: 1-5bdb52b3-68082ffc336d18153example] Successfully created Resolver Rule.",
            "TargetIps": [
                {
                    "Ip": "192.0.2.6",
                    "Port": 53
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListResolverRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverRules)
