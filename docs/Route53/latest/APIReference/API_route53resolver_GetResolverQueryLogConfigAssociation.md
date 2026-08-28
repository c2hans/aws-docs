---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html
---

# GetResolverQueryLogConfigAssociation
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation"></a>

Gets information about a specified association between a Resolver query logging configuration and an Amazon VPC. When you associate a VPC with a query logging configuration, Resolver logs DNS queries that originate in that VPC.

## Request Syntax
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_RequestSyntax"></a>

```
{
   "ResolverQueryLogConfigAssociationId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverQueryLogConfigAssociationId](#API_route53resolver_GetResolverQueryLogConfigAssociation_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverQueryLogConfigAssociation-request-ResolverQueryLogConfigAssociationId"></a>
The ID of the Resolver query logging configuration association that you want to get information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_ResponseSyntax"></a>

```
{
   "ResolverQueryLogConfigAssociation": {
      "CreationTime": "string",
      "Error": "string",
      "ErrorMessage": "string",
      "Id": "string",
      "ResolverQueryLogConfigId": "string",
      "ResourceId": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfigAssociation](#API_route53resolver_GetResolverQueryLogConfigAssociation_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverQueryLogConfigAssociation-response-ResolverQueryLogConfigAssociation"></a>
Information about the Resolver query logging configuration association that you specified in a `GetQueryLogConfigAssociation` request.
Type: [ResolverQueryLogConfigAssociation](API_route53resolver_ResolverQueryLogConfigAssociation.md) object

## Errors
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_Errors"></a>

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

## Examples
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_Examples"></a>

### GetResolverQueryLogConfigAssociation Example
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_Example_1"></a>

This example illustrates one usage of GetResolverQueryLogConfigAssociation.

#### Sample Request
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 48
X-Amz-Target: Route53Resolver.GetResolverQueryLogConfigAssociation
X-Amz-Date: 20200731T192652Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "ResolverQueryLogConfigAssociationId": "rqlca-ff85e1ffexample"
}
```

#### Sample Response
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:26:52 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 464
x-amzn-RequestId: 1d7c8aad-1c63-413d-88a9-bc7b0example
Connection: keep-alive

{
    "ResolverQueryLogConfigAssociation":{
        "CreationTime": "2020-07-31T18:52:23.30Z",
        "Error": "",
        "ErrorMessage": "",
        "Id": "rqlca-ff85e1ffexample",
        "ResolverQueryLogConfigId": "rqlc-8ca61fe7cexample",
        "Resource": "vpc-03cf94c75cexample",
        "Status": "CREATED"
    }
}
```

## See Also
<a name="API_route53resolver_GetResolverQueryLogConfigAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetResolverQueryLogConfigAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
