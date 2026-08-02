---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html
---

# CreateResolverRule
<a name="API_route53resolver_CreateResolverRule"></a>

For DNS queries that originate in your VPCs, specifies which Resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.

## Request Syntax
<a name="API_route53resolver_CreateResolverRule_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "DelegationRecord": "{{string}}",
   "DomainName": "{{string}}",
   "Name": "{{string}}",
   "ResolverEndpointId": "{{string}}",
   "RuleType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetIps": [
      {
         "Ip": "{{string}}",
         "Ipv6": "{{string}}",
         "Port": {{number}},
         "Protocol": "{{string}}",
         "ServerNameIndication": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_CreateResolverRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [DelegationRecord](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-DelegationRecord"></a>
 DNS queries with the delegation records that match this domain name are forwarded to the resolvers on your network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [DomainName](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-DomainName"></a>
DNS queries for this domain name are forwarded to the IP addresses that you specify in `TargetIps`. If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [Name](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-Name"></a>
A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.
The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (\_), and spaces. The name cannot consist of only numbers.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** [ResolverEndpointId](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-ResolverEndpointId"></a>
The ID of the outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in `TargetIps`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [RuleType](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-RuleType"></a>
When you want to forward DNS queries for specified domain name to resolvers on your network, specify `FORWARD` or `DELEGATE`.
When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify `SYSTEM`.
For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify `FORWARD` for `RuleType`. To then have Resolver process queries for apex.example.com, you create a rule and specify `SYSTEM` for `RuleType`.
Currently, only Resolver can create rules that have a value of `RECURSIVE` for `RuleType`.
Type: String
Valid Values: `FORWARD | SYSTEM | RECURSIVE | DELEGATE`
Required: Yes

 ** [Tags](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-Tags"></a>
A list of the tag keys and values that you want to associate with the endpoint.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

 ** [TargetIps](#API_route53resolver_CreateResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-request-TargetIps"></a>
The IPs that you want Resolver to forward DNS queries to. You can specify either Ipv4 or Ipv6 addresses but not both in the same rule. Separate IP addresses with a space.
 `TargetIps` is available only when the value of `Rule type` is `FORWARD`. You should not provide TargetIps when the Rule type is `DELEGATE`.
when creating a DELEGATE rule, you must not provide the `TargetIps` parameter. If you provide the `TargetIps`, you may receive an ERROR message similar to "Delegate resolver rules need to specify a nameserver name". This error means you should not provide `TargetIps`.
Type: Array of [TargetAddress](API_route53resolver_TargetAddress.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_route53resolver_CreateResolverRule_ResponseSyntax"></a>

```
{
   "ResolverRule": {
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
}
```

## Response Elements
<a name="API_route53resolver_CreateResolverRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverRule](#API_route53resolver_CreateResolverRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverRule-response-ResolverRule"></a>
Information about the `CreateResolverRule` request, including the status of the request.
Type: [ResolverRule](API_route53resolver_ResolverRule.md) object

## Errors
<a name="API_route53resolver_CreateResolverRule_Errors"></a>

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

 ** ResourceExistsException **
The resource that you tried to create already exists.
 ** ResourceType **
For a `ResourceExistsException` error, the type of resource that the error applies to.
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

## Examples
<a name="API_route53resolver_CreateResolverRule_Examples"></a>

### CreateResolverRule Example
<a name="API_route53resolver_CreateResolverRule_Example_1"></a>

This example illustrates one usage of CreateResolverRule.

#### Sample Request
<a name="API_route53resolver_CreateResolverRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 170
X-Amz-Target: Route53Resolver.CreateResolverRule
X-Amz-Date: 20181101T192331Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "CreatorRequestId": "999",
    "DomainName": "example.com",
    "Name": "MyRule",
    "ResolverEndpointId": "rslvr-out-fdc049932dexample",
    "RuleType": "FORWARD",
    "TargetIps": [
        {
            "Ip": "192.0.2.6"
        }
    ]
}
```

#### Sample Response
<a name="API_route53resolver_CreateResolverRule_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:23:31 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 464
x-amzn-RequestId: f51a7bc8-e9c6-4399-b408-086ecexample
Connection: keep-alive

{
    "ResolverRule": {
        "Arn": "arn:aws:route53resolver:us-east-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample",
        "CreatorRequestId": "999",
        "DomainName": "example.com",
        "Id": "rslvr-rr-5328a0899aexample",
        "Name": "MyRule",
        "OwnerId": "123456789012",
        "ResolverEndpointId": "rslvr-out-fdc049932dexample",
        "RuleType": "FORWARD",
        "ShareStatus": "NOT_SHARED",
        "Status": "COMPLETE",
        "StatusMessage": "[Trace id: 1-5bdb52b3-68082ffc336d18153example] Successfully created Resolver Rule.",
        "TargetIps": [
            {
                "Ip": "192.0.2.6",
                "Port": 53
            }
        ]
    }
}
```

## See Also
<a name="API_route53resolver_CreateResolverRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/CreateResolverRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateResolverRule)
