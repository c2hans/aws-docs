---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverQueryLogConfig.html
---

# CreateResolverQueryLogConfig
<a name="API_route53resolver_CreateResolverQueryLogConfig"></a>

Creates a Resolver query logging configuration, which defines where you want Resolver to save DNS query logs that originate in your VPCs. Resolver can log queries only for VPCs that are in the same Region as the query logging configuration.

To specify which VPCs you want to log queries for, you use `AssociateResolverQueryLogConfig`. For more information, see [AssociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html).

You can optionally use AWS Resource Access Manager (AWS RAM) to share a query logging configuration with other AWS accounts. The other accounts can then associate VPCs with the configuration. The query logs that Resolver creates for a configuration include all DNS queries that originate in all VPCs that are associated with the configuration.

## Request Syntax
<a name="API_route53resolver_CreateResolverQueryLogConfig_RequestSyntax"></a>

```
{
   "CreatorRequestId": "{{string}}",
   "DestinationArn": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_route53resolver_CreateResolverQueryLogConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreatorRequestId](#API_route53resolver_CreateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverQueryLogConfig-request-CreatorRequestId"></a>
A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [DestinationArn](#API_route53resolver_CreateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverQueryLogConfig-request-DestinationArn"></a>
The ARN of the resource that you want Resolver to send query logs. You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream. Examples of valid values include the following:
+  **S3 bucket**:

   `arn:aws:s3:::amzn-s3-demo-bucket`

  You can optionally append a file prefix to the end of the ARN.

   `arn:aws:s3:::amzn-s3-demo-bucket/development/`
+  **CloudWatch Logs log group**:

   `arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*`
+  **Kinesis Data Firehose delivery stream**:

   `arn:aws:kinesis:us-east-2:0123456789:stream/my_stream_name`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: Yes

 ** [Name](#API_route53resolver_CreateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverQueryLogConfig-request-Name"></a>
The name that you want to give the query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [Tags](#API_route53resolver_CreateResolverQueryLogConfig_RequestSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverQueryLogConfig-request-Tags"></a>
A list of the tag keys and values that you want to associate with the query logging configuration.
Type: Array of [Tag](API_route53resolver_Tag.md) objects
Array Members: Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_route53resolver_CreateResolverQueryLogConfig_ResponseSyntax"></a>

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
<a name="API_route53resolver_CreateResolverQueryLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResolverQueryLogConfig](#API_route53resolver_CreateResolverQueryLogConfig_ResponseSyntax) **   <a name="Route53Resolver-route53resolver_CreateResolverQueryLogConfig-response-ResolverQueryLogConfig"></a>
Information about the `CreateResolverQueryLogConfig` request, including the status of the request.
Type: [ResolverQueryLogConfig](API_route53resolver_ResolverQueryLogConfig.md) object

## Errors
<a name="API_route53resolver_CreateResolverQueryLogConfig_Errors"></a>

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
<a name="API_route53resolver_CreateResolverQueryLogConfig_Examples"></a>

### CreateResolverQueryLogConfig Example
<a name="API_route53resolver_CreateResolverQueryLogConfig_Example_1"></a>

This example illustrates one usage of CreateResolverQueryLogConfig.

#### Sample Request
<a name="API_route53resolver_CreateResolverQueryLogConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: route53resolver.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 283
X-Amz-Target: Route53Resolver.CreateResolverQueryLogConfig
X-Amz-Date: 20200415T191344Z
User-Agent: aws-cli/1.16.45 Python/2.7.10 Darwin/16.7.0 botocore/1.12.35
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
               Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-2/route53resolver/aws4_request,
               SignedHeaders=content-type;host;x-amz-date;x-amz-target,
               Signature=[calculated-signature]

{
    "CreatorRequestId": "ramirezd-20200415T191001Z",
    "DestinationArn": "arn:aws:s3:::amzn-s3-demo-bucket/development/",
    "Name": "MyQueryLog",
    "Tags": [
        {
            "Key": "LineOfBusiness",
            "Value": "Engineering"
        }
    ]
}
```

#### Sample Response
<a name="API_route53resolver_CreateResolverQueryLogConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 01 Nov 2018 19:13:44 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 531
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
        "Status": "CREATING"
    }
}
```

## See Also
<a name="API_route53resolver_CreateResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateResolverQueryLogConfig)
