---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_UntagResource.html
---

# UntagResource
<a name="API_route53profiles_UntagResource"></a>

 Removes one or more tags from a specified resource.

## Request Syntax
<a name="API_route53profiles_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{ResourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_route53profiles_UntagResource_RequestSyntax) **   <a name="Route53Profiles-route53profiles_UntagResource-request-uri-ResourceArn"></a>
 The Amazon Resource Name (ARN) for the resource that you want to remove tags from.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [TagKeys](#API_route53profiles_UntagResource_RequestSyntax) **   <a name="Route53Profiles-route53profiles_UntagResource-request-uri-TagKeys"></a>
 The tags that you want to remove to the specified resource.
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_route53profiles_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_route53profiles_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_route53profiles_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ConflictException **
 The request you submitted conflicts with an existing request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The resource you are associating is not found.
 ** ResourceType **
 The resource type that caused the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
 You have provided an invalid command.
HTTP Status Code: 400

## Examples
<a name="API_route53profiles_UntagResource_Examples"></a>

### UntagResource Example
<a name="API_route53profiles_UntagResource_Example_1"></a>

This example illustrates one usage of UntagResource.

#### Sample Request
<a name="API_route53profiles_UntagResource_Example_1_Request"></a>

```
DELETE /tags/arn%3Aaws%3Aroute53profiles%3Aus-east-1%3A123456789012%3Aprofile%2Frp-4987774726example?tagKeys=my-key-1&tagKeys=my-key-2 HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date:20240319T233258Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Length: 0
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=host;x-amz-date;x-amz-security-token,
    Signature=[calculated-signature]
# Request body is empty
```

#### Sample Response
<a name="API_route53profiles_UntagResource_Example_1_Response"></a>

```
HTTP/1.1 204 OK
Date: Tue, 19 Mar 2024 23:33:04 GMT
Content-Type: application/json
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
Access-Control-Expose-Headers: x-amzn-ErrorType, x-amzn-RequestId, x-amzn-ErrorMessage, x-amzn-Trace-Id, x-amz-apigw-id, Date
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example
# Response body is empty
```

## See Also
<a name="API_route53profiles_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/UntagResource)
