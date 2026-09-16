---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchDeletePhoneNumber.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# BatchDeletePhoneNumber
<a name="API_BatchDeletePhoneNumber"></a>

 Moves phone numbers into the **Deletion queue**. Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted.

 Phone numbers remain in the **Deletion queue** for 7 days before they are deleted permanently.

## Request Syntax
<a name="API_BatchDeletePhoneNumber_RequestSyntax"></a>

```
POST /phone-numbers?operation=batch-delete HTTP/1.1
Content-type: application/json

{
   "PhoneNumberIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeletePhoneNumber_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeletePhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PhoneNumberIds](#API_BatchDeletePhoneNumber_RequestSyntax) **   <a name="chime-BatchDeletePhoneNumber-request-PhoneNumberIds"></a>
List of phone number IDs.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_BatchDeletePhoneNumber_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberErrors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "PhoneNumberId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeletePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberErrors](#API_BatchDeletePhoneNumber_ResponseSyntax) **   <a name="chime-BatchDeletePhoneNumber-response-PhoneNumberErrors"></a>
If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.
Type: Array of [PhoneNumberError](API_PhoneNumberError.md) objects

## Errors
<a name="API_BatchDeletePhoneNumber_Errors"></a>

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
<a name="API_BatchDeletePhoneNumber_Examples"></a>

 In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchDeletePhoneNumber_Example_1"></a>

 This example moves multiple phone numbers into the **Deletion queue** .

#### Sample Request
<a name="API_BatchDeletePhoneNumber_Example_1_Request"></a>

```
POST /phone-numbers?operation=batch-delete HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T195348Z Authorization: AUTHPARAMS Content-Length: 56 {"PhoneNumberIds": ["%2B12065550100", "%2B12065550101"]}
```

#### Sample Response
<a name="API_BatchDeletePhoneNumber_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: f6ac5632-e71a-4755-997b-971c4dbff22c Content-Type: application/json Content-Length: 24 Date: Wed, 18 Sep 2019 19:53:49 GMT Connection: keep-alive {"PhoneNumberErrors":[]}
```

## See Also
<a name="API_BatchDeletePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/BatchDeletePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/BatchDeletePhoneNumber)
