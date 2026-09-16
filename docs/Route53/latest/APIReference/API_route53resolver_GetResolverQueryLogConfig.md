---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfig.html
---

# GetResolverQueryLogConfig
<a name="API_route53resolver_GetResolverQueryLogConfig"></a>

Gets information about a specified Resolver query logging configuration, such as the number of VPCs that the configuration is logging queries for and the location that logs are sent to.

## Request Syntax
<a name="API_route53resolver_GetResolverQueryLogConfig_RequestSyntax"></a>

```
{
   "ResolverQueryLogConfigId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_GetResolverQueryLogConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverQueryLogConfigId](#API_route53resolver_GetResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverQueryLogConfig-request-ResolverQueryLogConfigId"></a>
The ID of the Resolver query logging configuration that you want to get information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_GetResolverQueryLogConfig_ResponseSyntax"></a>

```
{
   "ResolverQueryLogConfig": {
      "Arn": "string",
      "AssociationCount": number,
      "CreationTime": "string",
      "CreatorRequestId": "string",
      "DestinationArn": "string",
      "Id": "string",
      "Name": "string",
      "OwnerId": "string",
      "ShareStatus": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_route53resolver_GetResolverQueryLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfig](#API_route53resolver_GetResolverQueryLogConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_GetResolverQueryLogConfig-response-ResolverQueryLogConfig"></a>
Information about the Resolver query logging configuration that you specified in a `GetQueryLogConfig` request.
Type: [ResolverQueryLogConfig](API_route53resolver_ResolverQueryLogConfig.md) object

## Errors
<a name="API_route53resolver_GetResolverQueryLogConfig_Errors"></a>

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
<a name="API_route53resolver_GetResolverQueryLogConfig_Examples"></a>

### GetResolverQueryLogConfig Example
<a name="API_route53resolver_GetResolverQueryLogConfig_Example_1"></a>

This example illustrates one usage of GetResolverQueryLogConfig.

#### Sample Request
<a name="API_route53resolver_GetResolverQueryLogConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 48
X-Amz-Target: Route53Resolver.GetResolverQueryLogConfig
X-Amz-Date: 20200731T192652Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "ResolverQueryLogConfigId": "rqlc-8ca61fe7cexample"
}
```

#### Sample Response
<a name="API_route53resolver_GetResolverQueryLogConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:26:52 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 464
x-amzn-RequestId: 1d7c8aad-1c63-413d-88a9-bc7b0example
Connection: keep-alive

{
    "ResolverQueryLogConfig": {
        "Arn": "arn:aws:route53resolver:us-east-1:111122223333:resolver-query-log-config/rqlc-8ca61fe7cexample",
        "AssociationCount": "1",
        "CreationTime": "20200731T191604Z",
        "CreatorRequestId": "ramirezd-20200731T191001Z",
        "DestinationArn": "arn:aws:s3:::amzn-s3-demo-bucket/development/",
        "Id": "rqlc-8ca61fe7c055415a",
        "Name": "MyQueryLog",
        "OwnerId": "111122223333",
        "ShareStatus": "NOT_SHARED",
        "Status": "CREATING"
    }
}
```

## See Also
<a name="API_route53resolver_GetResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/GetResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/GetResolverQueryLogConfig)
