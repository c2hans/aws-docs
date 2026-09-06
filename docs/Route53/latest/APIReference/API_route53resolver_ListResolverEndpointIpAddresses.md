---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpointIpAddresses.html
---

# ListResolverEndpointIpAddresses
<a name="API_route53resolver_ListResolverEndpointIpAddresses"></a>

Gets the IP addresses for a specified Resolver endpoint.

## Request Syntax
<a name="API_route53resolver_ListResolverEndpointIpAddresses_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResolverEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_ListResolverEndpointIpAddresses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_route53resolver_ListResolverEndpointIpAddresses_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-request-MaxResults"></a>
The maximum number of IP addresses that you want to return in the response to a `ListResolverEndpointIpAddresses` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 IP addresses.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverEndpointIpAddresses_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-request-NextToken"></a>
For the first `ListResolverEndpointIpAddresses` request, omit this value.
If the specified Resolver endpoint has more than `MaxResults` IP addresses, you can submit another `ListResolverEndpointIpAddresses` request to get the next group of IP addresses. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

 ** [ResolverEndpointId](#API_route53resolver_ListResolverEndpointIpAddresses_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-request-ResolverEndpointId"></a>
The ID of the Resolver endpoint that you want to get IP addresses for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_ListResolverEndpointIpAddresses_ResponseSyntax"></a>

```
{
   "IpAddresses": [
      {
         "CreationTime": "string",
         "Ip": "string",
         "IpId": "string",
         "Ipv6": "string",
         "ModificationTime": "string",
         "Status": "string",
         "StatusMessage": "string",
         "SubnetId": "string"
      }
   ],
   "MaxResults": number,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_route53resolver_ListResolverEndpointIpAddresses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IpAddresses](#API_route53resolver_ListResolverEndpointIpAddresses_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-response-IpAddresses"></a>
Information about the IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints).
Type: Array of [IpAddressResponse](API_route53resolver_IpAddressResponse.md) objects

 ** [MaxResults](#API_route53resolver_ListResolverEndpointIpAddresses_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-response-MaxResults"></a>
The value that you specified for `MaxResults` in the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53resolver_ListResolverEndpointIpAddresses_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpointIpAddresses-response-NextToken"></a>
If the specified endpoint has more than `MaxResults` IP addresses, you can submit another `ListResolverEndpointIpAddresses` request to get the next group of IP addresses. In the next request, specify the value of `NextToken` from the previous response.
Type: String

## Errors
<a name="API_route53resolver_ListResolverEndpointIpAddresses_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceType **
For a `ResourceNotFoundException` error, the type of resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_ListResolverEndpointIpAddresses_Examples"></a>

### ListResolverEndpointIpAddresses Example
<a name="API_route53resolver_ListResolverEndpointIpAddresses_Example_1"></a>

This example illustrates one usage of ListResolverEndpointIpAddresses.

#### Sample Request
<a name="API_route53resolver_ListResolverEndpointIpAddresses_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 52
X-Amz-Target: Route53Resolver.ListResolverEndpointIpAddresses
X-Amz-Date: 20181101T193143Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "ResolverEndpointId": "rslvr-in-60b9fd8fdbexample"
}
```

#### Sample Response
<a name="API_route53resolver_ListResolverEndpointIpAddresses_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:31:43 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 780
x-amzn-RequestId: df6722d0-49a0-4300-a491-fe290example
Connection: keep-alive

{
    "IpAddresses": [
        {
            "CreationTime": "2018-11-01T18:44:50.375Z",
            "Ip": "192.0.2.42",
            "IpId": "rni-42ed238be6example",
            "ModificationTime": "2018-11-01T18:45:10.956Z",
            "Status": "ATTACHED",
            "StatusMessage": "This IP address is operational.",
            "SubnetId": "subnet-02f91e0e98example"
        },
        {
            "CreationTime": "2018-11-01T18:44:50.379Z",
            "Ip": "192.0.2.18",
            "IpId": "rni-2cf1fc97bfexample",
            "ModificationTime": "2018-11-01T18:45:10.724Z",
            "Status": "ATTACHED",
            "StatusMessage": "This IP address is operational.",
            "SubnetId": "subnet-02f91e0e98example"
        },
        {
            "CreationTime": "2018-11-01T18:52:22.471Z",
            "Ip": "192.0.2.40",
            "IpId": "rni-e6b5f1b6e6example",
            "ModificationTime": "2018-11-01T18:52:45.886Z",
            "Status": "ATTACHED",
            "StatusMessage": "This IP address is operational.",
            "SubnetId": "subnet-02f91e0e98example"
        }
    ],
    "MaxResults": 10
}
```

## See Also
<a name="API_route53resolver_ListResolverEndpointIpAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverEndpointIpAddresses)
