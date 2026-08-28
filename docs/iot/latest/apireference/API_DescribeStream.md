---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeStream.html
---

# DescribeStream
<a name="API_DescribeStream"></a>

Gets information about a stream.

Requires permission to access the [DescribeStream](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeStream_RequestSyntax"></a>

```
GET /streams/{{streamId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [streamId](#API_DescribeStream_RequestSyntax) **   <a name="iot-DescribeStream-request-uri-streamId"></a>
The stream ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeStream_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "streamInfo": {
      "createdAt": number,
      "description": "string",
      "files": [
         {
            "fileId": number,
            "s3Location": {
               "bucket": "string",
               "key": "string",
               "version": "string"
            }
         }
      ],
      "lastUpdatedAt": number,
      "roleArn": "string",
      "streamArn": "string",
      "streamId": "string",
      "streamVersion": number
   }
}
```

## Response Elements
<a name="API_DescribeStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [streamInfo](#API_DescribeStream_ResponseSyntax) **   <a name="iot-DescribeStream-response-streamInfo"></a>
Information about the stream.
Type: [StreamInfo](API_StreamInfo.md) object

## Errors
<a name="API_DescribeStream_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
