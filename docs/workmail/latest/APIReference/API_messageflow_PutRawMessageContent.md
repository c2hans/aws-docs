---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_PutRawMessageContent.html
---

# PutRawMessageContent
<a name="API_messageflow_PutRawMessageContent"></a>

Updates the raw content of an in-transit email message, in MIME format.

For more information and examples for using this API, see [ Updating message content with AWS Lambda](https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html).

**Note**
Updates to an in-transit message only appear when you call `PutRawMessageContent` from an AWS Lambda function configured with a synchronous [ Run Lambda](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html#synchronous-rules) rule. If you call `PutRawMessageContent` on a delivered or sent message, the message remains unchanged, even though [GetRawMessageContent](https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html) returns an updated message.

## Request Syntax
<a name="API_messageflow_PutRawMessageContent_RequestSyntax"></a>

```
POST /messages/{{messageId}} HTTP/1.1
Content-type: application/json

{
   "content": {
      "s3Reference": {
         "bucket": "{{string}}",
         "key": "{{string}}",
         "objectVersion": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_messageflow_PutRawMessageContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [messageId](#API_messageflow_PutRawMessageContent_RequestSyntax) **   <a name="workmail-messageflow_PutRawMessageContent-request-uri-messageId"></a>
The identifier of the email message being updated.
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-z0-9\-]*`
Required: Yes

## Request Body
<a name="API_messageflow_PutRawMessageContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [content](#API_messageflow_PutRawMessageContent_RequestSyntax) **   <a name="workmail-messageflow_PutRawMessageContent-request-content"></a>
Describes the raw message content of the updated email message.
Type: [RawMessageContent](API_messageflow_RawMessageContent.md) object
Required: Yes

## Response Syntax
<a name="API_messageflow_PutRawMessageContent_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_messageflow_PutRawMessageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_messageflow_PutRawMessageContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidContentLocation **
WorkMail could not access the updated email content. Possible reasons:
+ You made the request in a region other than your S3 bucket region.
+ The [S3 bucket owner](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-owner-condition.html) is not the same as the calling AWS account.
+ You have an incomplete or missing S3 bucket policy. For more information about policies, see [ Updating message content with AWS Lambda ](https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html) in the *WorkMail Administrator Guide*.
HTTP Status Code: 400

 ** MessageFrozen **
The requested email is not eligible for update. This is usually the case for a redirected email.
HTTP Status Code: 400

 ** MessageRejected **
The requested email could not be updated due to an error in the MIME content. Check the error message for more information about what caused the error.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested email message is not found.
HTTP Status Code: 404

## Examples
<a name="API_messageflow_PutRawMessageContent_Examples"></a>

In the following examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_messageflow_PutRawMessageContent_Example_1"></a>

This example illustrates one usage of PutRawMessageContent.

#### Sample Request
<a name="API_messageflow_PutRawMessageContent_Example_1_Request"></a>

```
POST /messages/4e87856b-f02f-39d5-a029-9e39ace5b6f1 HTTP/1.1
Host: workmailmessageflow.us-east-1.amazonaws.com
Accept-Encoding: gzip, deflate
User-Agent: aws-cli/1.16.230 Python/3.7.5 Darwin/18.7.0 botocore/1.12.220
X-Amz-Date: 20210127T151129Z
Authorization: AUTHPARAMS
Content-Length: 81
Connection: close

{"content": {"s3Reference": {"bucket": "My-S3-Bucket", "key": "My-S3-Object-Key"}}}
```

#### Sample Response
<a name="API_messageflow_PutRawMessageContent_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Type: application/json
Date: Wed, 27 Jan 2021 15:11:30 GMT
x-amzn-RequestId: ddd7de94-a4eb-4af8-8c3f-1d16cf98b458
Content-Length: 2
Connection: Close

{}
```

## See Also
<a name="API_messageflow_PutRawMessageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmailmessageflow-2019-05-01/PutRawMessageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmailmessageflow-2019-05-01/PutRawMessageContent)
