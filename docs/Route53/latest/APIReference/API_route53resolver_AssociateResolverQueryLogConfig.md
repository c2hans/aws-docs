---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html
---

# AssociateResolverQueryLogConfig
<a name="API_route53resolver_AssociateResolverQueryLogConfig"></a>

Associates an Amazon VPC with a specified query logging configuration. Route 53 Resolver logs DNS queries that originate in all of the Amazon VPCs that are associated with a specified query logging configuration. To associate more than one VPC with a configuration, submit one `AssociateResolverQueryLogConfig` request for each VPC.

**Note**
The VPCs that you associate with a query logging configuration must be in the same Region as the configuration.

To remove a VPC from a query logging configuration, see [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html).

## Request Syntax
<a name="API_route53resolver_AssociateResolverQueryLogConfig_RequestSyntax"></a>

```
{
   "ResolverQueryLogConfigId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_AssociateResolverQueryLogConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverQueryLogConfigId](#API_route53resolver_AssociateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverQueryLogConfig-request-ResolverQueryLogConfigId"></a>
The ID of the query logging configuration that you want to associate a VPC with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResourceId](#API_route53resolver_AssociateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverQueryLogConfig-request-ResourceId"></a>
The ID of an Amazon VPC that you want this query logging configuration to log queries for.
The VPCs and the query logging configuration must be in the same Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_AssociateResolverQueryLogConfig_ResponseSyntax"></a>

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
<a name="API_route53resolver_AssociateResolverQueryLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfigAssociation](#API_route53resolver_AssociateResolverQueryLogConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_AssociateResolverQueryLogConfig-response-ResolverQueryLogConfigAssociation"></a>
A complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.
Type: [ResolverQueryLogConfigAssociation](API_route53resolver_ResolverQueryLogConfigAssociation.md) object

## Errors
<a name="API_route53resolver_AssociateResolverQueryLogConfig_Errors"></a>

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

 ** ThrottlingException **
The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

## Examples
<a name="API_route53resolver_AssociateResolverQueryLogConfig_Examples"></a>

### AssociateResolverQueryLogConfig Example
<a name="API_route53resolver_AssociateResolverQueryLogConfig_Example_1"></a>

This example illustrates one usage of AssociateResolverQueryLogConfig.

#### Sample Request
<a name="API_route53resolver_AssociateResolverQueryLogConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: Route53Resolver.AssociateResolverQueryLogConfig
X-Amz-Date: 20200415T185222Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20200415/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "ResolverQueryLogConfigId": "rqlc-8ca61fe7cexample",
    "Resource": {
        "VpcId": "vpc-03cf94c75cexample"
    }
}
```

#### Sample Response
<a name="API_route53resolver_AssociateResolverQueryLogConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 18:52:22 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 479
x-amzn-RequestId: bda80f7b-0f2c-41d1-9043-f36d3example
Connection: keep-alive

{
    "ResolverQueryLogConfigAssociation":{
        "CreationTime": "2020-04-15T18:52:23.30Z",
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
<a name="API_route53resolver_AssociateResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/AssociateResolverQueryLogConfig)
