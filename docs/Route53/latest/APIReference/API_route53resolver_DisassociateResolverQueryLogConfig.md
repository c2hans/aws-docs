---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html
---

# DisassociateResolverQueryLogConfig
<a name="API_route53resolver_DisassociateResolverQueryLogConfig"></a>

Disassociates a VPC from a query logging configuration.

**Note**
Before you can delete a query logging configuration, you must first disassociate all VPCs from the configuration. If you used AWS Resource Access Manager (AWS RAM) to share a query logging configuration with other accounts, VPCs can be disassociated from the configuration in the following ways:
The accounts that you shared the configuration with can disassociate VPCs from the configuration.
You can stop sharing the configuration.

## Request Syntax
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_RequestSyntax"></a>

```
{
   "ResolverQueryLogConfigId": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverQueryLogConfigId](#API_route53resolver_DisassociateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DisassociateResolverQueryLogConfig-request-ResolverQueryLogConfigId"></a>
The ID of the query logging configuration that you want to disassociate a specified VPC from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResourceId](#API_route53resolver_DisassociateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DisassociateResolverQueryLogConfig-request-ResourceId"></a>
The ID of the Amazon VPC that you want to disassociate from a specified query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_ResponseSyntax"></a>

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
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfigAssociation](#API_route53resolver_DisassociateResolverQueryLogConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_DisassociateResolverQueryLogConfig-response-ResolverQueryLogConfigAssociation"></a>
A complex type that contains settings for the association that you deleted between an Amazon VPC and a query logging configuration.
Type: [ResolverQueryLogConfigAssociation](API_route53resolver_ResolverQueryLogConfigAssociation.md) object

## Errors
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_Errors"></a>

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
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_Examples"></a>

### DisassociateResolverQueryLogConfig Example
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_Example_1"></a>

This example illustrates one usage of DisassociateResolverQueryLogConfig.

#### Sample Request
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: Route53Resolver.DisassociateResolverQueryLogConfig
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
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 18:52:22 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 275
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
        "Status": "DELETING"
    }
}
```

## See Also
<a name="API_route53resolver_DisassociateResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DisassociateResolverQueryLogConfig)
