---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateUserSettings.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# UpdateUserSettings
<a name="API_UpdateUserSettings"></a>

Updates the settings for the specified user, such as phone number settings.

## Request Syntax
<a name="API_UpdateUserSettings_RequestSyntax"></a>

```
PUT /accounts/{{accountId}}/users/{{userId}}/settings HTTP/1.1
Content-type: application/json

{
   "UserSettings": {
      "Telephony": {
         "InboundCalling": {{boolean}},
         "OutboundCalling": {{boolean}},
         "SMS": {{boolean}}
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateUserSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_UpdateUserSettings_RequestSyntax) **   <a name="chime-UpdateUserSettings-request-uri-AccountId"></a>
The Amazon Chime account ID.
Required: Yes

 ** [userId](#API_UpdateUserSettings_RequestSyntax) **   <a name="chime-UpdateUserSettings-request-uri-UserId"></a>
The user ID.
Required: Yes

## Request Body
<a name="API_UpdateUserSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserSettings](#API_UpdateUserSettings_RequestSyntax) **   <a name="chime-UpdateUserSettings-request-UserSettings"></a>
The user settings to update.
Type: [UserSettings](API_UserSettings.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateUserSettings_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateUserSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateUserSettings_Errors"></a>

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
<a name="API_UpdateUserSettings_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateUserSettings_Example_1"></a>

This example updates the settings for the specified user.

#### Sample Request
<a name="API_UpdateUserSettings_Example_1_Request"></a>

```
PUT /accounts/12a3456b-7c89-012d-3456-78901e23fg45/users/1ab2345c-67de-8901-f23g-45h678901j2k/settings HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T181826Z Authorization: AUTHPARAMS Content-Length: 95 {"UserSettings": {"Telephony": {"InboundCalling": true, "OutboundCalling": true, "SMS": true}}}
```

#### Sample Response
<a name="API_UpdateUserSettings_Example_1_Response"></a>

```
HTTP/1.1 204 No Content x-amzn-RequestId: 72ab9592-8aa8-4de1-9dd7-a8f84011261b Content-Type: application/json Date: Wed, 18 Sep 2019 18:18:27 GMT Connection: keep-alive
```

## See Also
<a name="API_UpdateUserSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/UpdateUserSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/UpdateUserSettings)
