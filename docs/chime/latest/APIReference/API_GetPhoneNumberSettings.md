---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_GetPhoneNumberSettings.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# GetPhoneNumberSettings
<a name="API_GetPhoneNumberSettings"></a>

Retrieves the phone number settings for the administrator's AWS account, such as the default outbound calling name.

## Request Syntax
<a name="API_GetPhoneNumberSettings_RequestSyntax"></a>

```
GET /settings/phone-number HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPhoneNumberSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPhoneNumberSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPhoneNumberSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CallingName": "string",
   "CallingNameUpdatedTimestamp": "string"
}
```

## Response Elements
<a name="API_GetPhoneNumberSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CallingName](#API_GetPhoneNumberSettings_ResponseSyntax) **   <a name="chime-GetPhoneNumberSettings-response-CallingName"></a>
The default outbound calling name for the account.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`

 ** [CallingNameUpdatedTimestamp](#API_GetPhoneNumberSettings_ResponseSyntax) **   <a name="chime-GetPhoneNumberSettings-response-CallingNameUpdatedTimestamp"></a>
The updated outbound calling name timestamp, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_GetPhoneNumberSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

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
<a name="API_GetPhoneNumberSettings_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetPhoneNumberSettings_Example_1"></a>

This example retrieves the phone number settings for the administrator's AWS account.

#### Sample Request
<a name="API_GetPhoneNumberSettings_Example_1_Request"></a>

```
GET /settings/phone-number HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20191028T185743Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_GetPhoneNumberSettings_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: 34cb347e-cc3f-440c-a78f-b7e128207e75 Content-Type: application/json Content-Length: 81 Date: Mon, 28 Oct 2019 18:57:43 GMT Connection: keep-alive {"CallingName":"myName","CallingNameUpdatedTimestamp":"2019-10-28T18:56:42.911Z"}
```

## See Also
<a name="API_GetPhoneNumberSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/GetPhoneNumberSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/GetPhoneNumberSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
