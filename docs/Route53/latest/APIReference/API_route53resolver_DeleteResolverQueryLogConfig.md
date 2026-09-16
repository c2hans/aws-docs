---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverQueryLogConfig.html
---

# DeleteResolverQueryLogConfig
<a name="API_route53resolver_DeleteResolverQueryLogConfig"></a>

Deletes a query logging configuration. When you delete a configuration, Resolver stops logging DNS queries for all of the Amazon VPCs that are associated with the configuration. This also applies if the query logging configuration is shared with other AWS accounts, and the other accounts have associated VPCs with the shared configuration.

Before you can delete a query logging configuration, you must first disassociate all VPCs from the configuration. See [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html).

If you used Resource Access Manager (RAM) to share a query logging configuration with other accounts, you must stop sharing the configuration before you can delete a configuration. The accounts that you shared the configuration with can first disassociate VPCs that they associated with the configuration, but that's not necessary. If you stop sharing the configuration, those VPCs are automatically disassociated from the configuration.

## Request Syntax
<a name="API_route53resolver_DeleteResolverQueryLogConfig_RequestSyntax"></a>

```
{
   "ResolverQueryLogConfigId": "{{string}}"
}
```

## Request Parameters
<a name="API_route53resolver_DeleteResolverQueryLogConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResolverQueryLogConfigId](#API_route53resolver_DeleteResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_DeleteResolverQueryLogConfig-request-ResolverQueryLogConfigId"></a>
The ID of the query logging configuration that you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_route53resolver_DeleteResolverQueryLogConfig_ResponseSyntax"></a>

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
<a name="API_route53resolver_DeleteResolverQueryLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfig](#API_route53resolver_DeleteResolverQueryLogConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_DeleteResolverQueryLogConfig-response-ResolverQueryLogConfig"></a>
Information about the query logging configuration that you deleted, including the status of the request.
Type: [ResolverQueryLogConfig](API_route53resolver_ResolverQueryLogConfig.md) object

## Errors
<a name="API_route53resolver_DeleteResolverQueryLogConfig_Errors"></a>

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
<a name="API_route53resolver_DeleteResolverQueryLogConfig_Examples"></a>

### DeleteResolverQueryLogConfig Example
<a name="API_route53resolver_DeleteResolverQueryLogConfig_Example_1"></a>

This example illustrates one usage of DeleteResolverQueryLogConfig.

#### Sample Request
<a name="API_route53resolver_DeleteResolverQueryLogConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 283
X-Amz-Target: Route53Resolver.DeleteResolverQueryLogConfig
X-Amz-Date: 20200415T191344Z
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
<a name="API_route53resolver_DeleteResolverQueryLogConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:13:44 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 493
x-amzn-RequestId: 08afd081-9d67-4281-a277-b3880example
Connection: keep-alive

{
    "ResolverQueryLogConfig": {
        "Arn": "arn:aws:route53resolver:us-east-1:111122223333:resolver-query-log-config/rqlc-8ca61fe7cexample",
        "AssociationCount": "1",
        "CreationTime": "20200415T191604Z",
        "CreatorRequestId": "ramirezd-20200415T191001Z",
        "DestinationArn": "arn:aws:s3:::amzn-s3-demo-bucket/development/",
        "Id": "rqlc-8ca61fe7cexample",
        "Name": "MyQueryLog",
        "OwnerId": "111122223333",
        "ShareStatus": "NOT_SHARED",
        "Status": "DELETING"
    }
}
```

## See Also
<a name="API_route53resolver_DeleteResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/DeleteResolverQueryLogConfig)
