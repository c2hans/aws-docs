---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html
---

# DeleteResolverRule
<a name="API_route53resolver_DeleteResolverRule"></a>

Deletes a Resolver rule. Before you can delete a Resolver rule, you must disassociate it from all the VPCs that you associated the Resolver rule with. For more information, see [DisassociateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverRule.html).

## Request Syntax
<a name="API_route53resolver_DeleteResolverRule_RequestSyntax"></a>

```
{
   "ResolverRuleId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_DeleteResolverRule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverRuleId](#API_route53resolver_DeleteResolverRule_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteResolverRule-request-ResolverRuleId"></a>
The ID of the Resolver rule that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_DeleteResolverRule_ResponseSyntax"></a>

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
<a name="API_route53resolver_DeleteResolverRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverRule](#API_route53resolver_DeleteResolverRule_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_DeleteResolverRule-response-ResolverRule"></a>
Information about the `DeleteResolverRule` request, including the status of the request.
Type: [ResolverRule](API_route53resolver_ResolverRule.md) object

## Errors
<a name="API_route53resolver_DeleteResolverRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceInUseException **
The resource that you tried to update or delete is currently in use.
 ** ResourceType **
For a `ResourceInUseException` error, the type of resource that is currently in use.
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
<a name="API_route53resolver_DeleteResolverRule_Examples"></a>

### DeleteResolverRule Example
<a name="API_route53resolver_DeleteResolverRule_Example_1"></a>

This example illustrates one usage of DeleteResolverRule.

#### Sample Request
<a name="API_route53resolver_DeleteResolverRule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 170
X-Amz-Target: Route53Resolver.DeleteResolverRule
X-Amz-Date: 20181101T192331Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "ResolverRuleId": "rslvr-rr-5328a0899aexample"
}
```

#### Sample Response
<a name="API_route53resolver_DeleteResolverRule_Example_1_Response"></a>

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
        "OwnerId": "123456789012",
        "ResolverEndpointId": "rslvr-out-fdc049932dexample",
        "RuleType": "FORWARD",
        "Status": "COMPLETE",
        "StatusMessage": "[Trace id: 1-5bdb52b3-68082ffc336d18153example] Successfully deleted Resolver Rule.",
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
<a name="API_route53resolver_DeleteResolverRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/DeleteResolverRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DeleteResolverRule)
