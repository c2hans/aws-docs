---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_AssociatePhoneNumberWithUser.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# AssociatePhoneNumberWithUser
<a name="API_AssociatePhoneNumberWithUser"></a>

Associates a phone number with the specified Amazon Chime user.

## Request Syntax
<a name="API_AssociatePhoneNumberWithUser_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/users/{userId}?operation=associate-phone-number HTTP/1.1
Content-type: application/json

{
   "E164PhoneNumber": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociatePhoneNumberWithUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_AssociatePhoneNumberWithUser_RequestSyntax) **   <a name="chime-AssociatePhoneNumberWithUser-request-uri-AccountId"></a>
The Amazon Chime account ID.
Required: Yes

 ** [userId](#API_AssociatePhoneNumberWithUser_RequestSyntax) **   <a name="chime-AssociatePhoneNumberWithUser-request-uri-UserId"></a>
The user ID.
Required: Yes

## Request Body
<a name="API_AssociatePhoneNumberWithUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [E164PhoneNumber](#API_AssociatePhoneNumberWithUser_RequestSyntax) **   <a name="chime-AssociatePhoneNumberWithUser-request-E164PhoneNumber"></a>
The phone number, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

## Response Syntax
<a name="API_AssociatePhoneNumberWithUser_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociatePhoneNumberWithUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociatePhoneNumberWithUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation.
HTTP Status Code: 403

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
<a name="API_AssociatePhoneNumberWithUser_Examples"></a>

 In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference* .

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_AssociatePhoneNumberWithUser_Example_1"></a>

This example associates the specified phone number with the specified Amazon Chime user.

#### Sample Request
<a name="API_AssociatePhoneNumberWithUser_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/users/1ab2345c-67de-8901-f23g-45h678901j2k?operation=associate-phone-number HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T181244Z Authorization: AUTHPARAMS Content-Length: 35 {"E164PhoneNumber": "+12065550100"}
```

#### Sample Response
<a name="API_AssociatePhoneNumberWithUser_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: d70a1eae-c35a-4607-ac37-6e9a62f7c163 Content-Type: application/json Content-Length: 2 Date: Wed, 18 Sep 2019 18:12:45 GMT Connection: keep-alive {}
```

## See Also
<a name="API_AssociatePhoneNumberWithUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/AssociatePhoneNumberWithUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/AssociatePhoneNumberWithUser)
