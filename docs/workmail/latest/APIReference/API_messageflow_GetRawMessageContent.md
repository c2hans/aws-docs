---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html
---

# GetRawMessageContent
<a name="API_messageflow_GetRawMessageContent"></a>

Retrieves the raw content of an in-transit email message, in MIME format.

## Request Syntax
<a name="API_messageflow_GetRawMessageContent_RequestSyntax"></a>

```
GET /messages/{{messageId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_messageflow_GetRawMessageContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [messageId](#API_messageflow_GetRawMessageContent_RequestSyntax) **   <a name="workmail-messageflow_GetRawMessageContent-request-uri-messageId"></a>
The identifier of the email message to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-z0-9\-]*`
Required: Yes

## Request Body
<a name="API_messageflow_GetRawMessageContent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_messageflow_GetRawMessageContent_ResponseSyntax"></a>

```
HTTP/1.1 200

{{messageContent}}
```

## Response Elements
<a name="API_messageflow_GetRawMessageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following as the HTTP body.

 ** [messageContent](#API_messageflow_GetRawMessageContent_ResponseSyntax) **   <a name="workmail-messageflow_GetRawMessageContent-response-messageContent"></a>
The raw content of the email message, in MIME format.

## Errors
<a name="API_messageflow_GetRawMessageContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The requested email message is not found.
HTTP Status Code: 404

## Examples
<a name="API_messageflow_GetRawMessageContent_Examples"></a>

In the following examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_messageflow_GetRawMessageContent_Example_1"></a>

This example gets the raw content of an in-transit email message and sends it to a text file named "test".

#### Sample Request
<a name="API_messageflow_GetRawMessageContent_Example_1_Request"></a>

```
GET /messages/a1b2cd34-ef5g-6h7j-kl8m-npq9012345rs HTTP/1.1
Host: workmailmessageflow.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.273 Python/3.6.0 Windows/10 botocore/1.13.9
X-Amz-Date: 20191107T195012Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_messageflow_GetRawMessageContent_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Content-Type: application/json
Date: Thu, 07 Nov 2019 19:50:12 GMT
x-amzn-RequestId: ea71f214-79c5-4f89-9d4e-1ab4c43ae0df
Content-Length: 1344
Connection: keep-alive

Subject: Hello World
From: =?UTF-8?Q?marymajor_marymajor?= <marymajor@example.com>
To: =?UTF-8?Q?mateojackson=40example=2Enet?= <mateojackson@example.net>
Date: Thu, 7 Nov 2019 19:22:46 +0000
Mime-Version: 1.0
Content-Type: multipart/alternative;
 boundary="=_EXAMPLE+"
References: <mail.1ab23c45.5de6.7f890g123hj45678@storage.wm.amazon.com>
X-Priority: 3 (Normal)
X-Mailer: Amazon WorkMail
Thread-Index: EXAMPLE
Thread-Topic: Hello World
Message-Id: <mail.1ab23c45.5de6.7f890g123hj45678@storage.wm.amazon.com>

This is a multi-part message in MIME format. Your mail reader does not
understand MIME message format.
--=_EXAMPLE+
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 7bit

hello world

--=_EXAMPLE+
Content-Type: text/html; charset=utf-8
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE HTML><html>
<head>
<meta name=3D"Generator" content=3D"Amazon WorkMail v3.0-4510">
<meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dutf-8">=

<title>testing</title>
</head>
<body>
<p style=3D"margin: 0px; font-family: Arial, Tahoma, Helvetica, sans-serif; font-size: small;">hello world</p>
</body>
</html>
--=_EXAMPLE+--
```

## See Also
<a name="API_messageflow_GetRawMessageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmailmessageflow-2019-05-01/GetRawMessageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmailmessageflow-2019-05-01/GetRawMessageContent)
