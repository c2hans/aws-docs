---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html
---

# ListResolverEndpoints
<a name="API_route53resolver_ListResolverEndpoints"></a>

Lists all the Resolver endpoints that were created using the current AWS account.

## Request Syntax
<a name="API_route53resolver_ListResolverEndpoints_RequestSyntax"></a>

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
<a name="API_route53resolver_ListResolverEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_route53resolver_ListResolverEndpoints_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-request-Filters"></a>
An optional specification to return a subset of Resolver endpoints, such as all inbound Resolver endpoints.
If you submit a second or subsequent `ListResolverEndpoints` request and specify the `NextToken` parameter, you must use the same values for `Filters`, if any, as in the previous request.
Type: Array of [Filter](API_route53resolver_Filter.md) objects
Required: No

 ** [MaxResults](#API_route53resolver_ListResolverEndpoints_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-request-MaxResults"></a>
The maximum number of Resolver endpoints that you want to return in the response to a `ListResolverEndpoints` request. If you don't specify a value for `MaxResults`, Resolver returns up to 100 Resolver endpoints.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_route53resolver_ListResolverEndpoints_RequestSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-request-NextToken"></a>
For the first `ListResolverEndpoints` request, omit this value.
If you have more than `MaxResults` Resolver endpoints, you can submit another `ListResolverEndpoints` request to get the next group of Resolver endpoints. In the next request, specify the value of `NextToken` from the previous response.
Type: String
Required: No

## Response Syntax
<a name="API_route53resolver_ListResolverEndpoints_ResponseSyntax"></a>

```
{
   "MaxResults": number,
   "NextToken": "string",
   "ResolverEndpoints": [
      {
         "Arn": "string",
         "CreationTime": "string",
         "CreatorRequestId": "string",
         "Direction": "string",
         "Dns64Enabled": boolean,
         "HostVPCId": "string",
         "Id": "string",
         "IpAddressCount": number,
         "Ipv6InternetAccessEnabled": boolean,
         "ModificationTime": "string",
         "Name": "string",
         "OutpostArn": "string",
         "PreferredInstanceType": "string",
         "Protocols": [ "string" ],
         "ResolverEndpointType": "string",
         "RniEnhancedMetricsEnabled": boolean,
         "SecurityGroupIds": [ "string" ],
         "Status": "string",
         "StatusMessage": "string",
         "TargetNameServerMetricsEnabled": boolean
      }
   ]
}
```

## Response Elements
<a name="API_route53resolver_ListResolverEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MaxResults](#API_route53resolver_ListResolverEndpoints_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-response-MaxResults"></a>
The value that you specified for `MaxResults` in the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53resolver_ListResolverEndpoints_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-response-NextToken"></a>
If more than `MaxResults` IP addresses match the specified criteria, you can submit another `ListResolverEndpoint` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ResolverEndpoints](#API_route53resolver_ListResolverEndpoints_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_ListResolverEndpoints-response-ResolverEndpoints"></a>
The Resolver endpoints that were created by using the current AWS account, and that match the specified filters, if any.
Type: Array of [ResolverEndpoint](API_route53resolver_ResolverEndpoint.md) objects

## Errors
<a name="API_route53resolver_ListResolverEndpoints_Errors"></a>

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
<a name="API_route53resolver_ListResolverEndpoints_Examples"></a>

### ListResolverEndpoints Example
<a name="API_route53resolver_ListResolverEndpoints_Example_1"></a>

This example illustrates one usage of ListResolverEndpoints.

#### Sample Request
<a name="API_route53resolver_ListResolverEndpoints_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: Route53Resolver.ListResolverEndpoints
X-Amz-Date: 20181101T191920Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{}
```

#### Sample Response
<a name="API_route53resolver_ListResolverEndpoints_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:19:20 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 983
x-amzn-RequestId: 35a62daa-889c-47e4-994e-5a4dbd9818fb
Connection: keep-alive

{
    "MaxResults": 10,
    "ResolverEndpoints": [
        {
            "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-endpoint/rslvr-in-60b9fd8fdbexample",
            "CreationTime": "2018-11-01T18:44:50.372Z",
            "CreatorRequestId": "1234",
            "Direction": "INBOUND",
            "HostVPCId": "vpc-03cf94c75cexample",
            "Id": "rslvr-in-60b9fd8fdbexample",
            "IpAddressCount": 3,
            "ModificationTime": "2018-11-01T18:44:50.372Z",
            "Name": "MyInbound",
            "Protocols": [
                "DoH"
            ],
            "ResolverEndpointType": "IPV4",
            "Dns64Enabled": false,
            "RniEnhancedMetricsEnabled": false,
            "SecurityGroupIds": [
                "sg-020a3554aexample"
            ],
            "Status": "OPERATIONAL",
            "StatusMessage": "This Resolver Endpoint is operational."
        },
        {
            "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-endpoint/rslvr-out-fdc049932d9645ffa",
            "CreationTime": "2018-11-01T19:13:44.830Z",
            "CreatorRequestId": "5678",
            "Direction": "OUTBOUND",
            "HostVPCId": "vpc-0dd415a0edexample",
            "Id": "rslvr-out-fdc049932dexample",
            "IpAddressCount": 2,
            "ModificationTime": "2018-11-01T19:13:44.830Z",
            "Name": "MyOutbound",
            "Protocols": [
                "DoH"
            ],
            "ResolverEndpointType": "IPV4",
            "Ipv6InternetAccessEnabled": false,
            "RniEnhancedMetricsEnabled": false,
            "SecurityGroupIds": [
                "sg-071b99f42example"
            ],
            "Status": "OPERATIONAL",
            "StatusMessage": "This Resolver Endpoint is operational."
            "TargetNameServerMetricsEnabled": true
        }
    ]
}
```

## See Also
<a name="API_route53resolver_ListResolverEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/ListResolverEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ListResolverEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
