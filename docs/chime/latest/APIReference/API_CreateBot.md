---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateBot.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# CreateBot
<a name="API_CreateBot"></a>

Creates a bot for an Amazon Chime Enterprise account.

## Request Syntax
<a name="API_CreateBot_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/bots HTTP/1.1
Content-type: application/json

{
   "DisplayName": "{{string}}",
   "Domain": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_CreateBot_RequestSyntax) **   <a name="chime-CreateBot-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateBot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DisplayName](#API_CreateBot_RequestSyntax) **   <a name="chime-CreateBot-request-DisplayName"></a>
The bot display name.
Type: String
Required: Yes

 ** [Domain](#API_CreateBot_RequestSyntax) **   <a name="chime-CreateBot-request-Domain"></a>
The domain of the Amazon Chime Enterprise account.
Type: String
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_CreateBot_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Bot": {
      "BotEmail": "string",
      "BotId": "string",
      "BotType": "string",
      "CreatedTimestamp": "string",
      "Disabled": boolean,
      "DisplayName": "string",
      "SecurityToken": "string",
      "UpdatedTimestamp": "string",
      "UserId": "string"
   }
}
```

## Response Elements
<a name="API_CreateBot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Bot](#API_CreateBot_ResponseSyntax) **   <a name="chime-CreateBot-response-Bot"></a>
The bot details.
Type: [Bot](API_Bot.md) object

## Errors
<a name="API_CreateBot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## Examples
<a name="API_CreateBot_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateBot_Example_1"></a>

This example creates a bot.

#### Sample Request
<a name="API_CreateBot_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/bots HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T172439Z Authorization: AUTHPARAMS Content-Length: 60 {"DisplayName": "myBot", "Domain": "example.com"}
```

#### Sample Response
<a name="API_CreateBot_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: 4c54e5bc-4ff5-4828-a222-59996acbc6ee Content-Type: application/json Content-Length: 374 Date: Wed, 18 Sep 2019 17:24:39 GMT Connection: keep-alive {"Bot":{"BotEmail":"myBot-chimebot@example.com","BotId":"123abcd4-5ef6-789g-0h12-34j56789012k","BotType":"ChatBot","CreatedTimestamp":"2019-09-18T17:24:39.534Z","Disabled":false,"DisplayName":"myBot (Bot)","SecurityToken":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY","UpdatedTimestamp":"2019-09-18T17:24:39.534Z","UserId":"123abcd4-5ef6-789g-0h12-34j56789012k"}}
```

## See Also
<a name="API_CreateBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/CreateBot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/CreateBot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/CreateBot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/CreateBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/CreateBot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/CreateBot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/CreateBot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/CreateBot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/CreateBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/CreateBot)
