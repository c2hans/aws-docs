---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_BatchUpdatePhoneNumber.html
---

# BatchUpdatePhoneNumber
<a name="API_voice-chime_BatchUpdatePhoneNumber"></a>

Updates phone number product types, calling names, or phone number names. You can update one attribute at a time for each `UpdatePhoneNumberRequestItem`. For example, you can update the product type, the calling name, or phone name.

**Note**
You cannot have a duplicate `phoneNumberId` in a request.

## Request Syntax
<a name="API_voice-chime_BatchUpdatePhoneNumber_RequestSyntax"></a>

```
POST /phone-numbers?operation=batch-update HTTP/1.1
Content-type: application/json

{
   "UpdatePhoneNumberRequestItems": [
      {
         "CallingName": "{{string}}",
         "Name": "{{string}}",
         "PhoneNumberId": "{{string}}",
         "ProductType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_voice-chime_BatchUpdatePhoneNumber_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_voice-chime_BatchUpdatePhoneNumber_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UpdatePhoneNumberRequestItems](#API_voice-chime_BatchUpdatePhoneNumber_RequestSyntax) **   <a name="chimesdk-voice-chime_BatchUpdatePhoneNumber-request-UpdatePhoneNumberRequestItems"></a>
Lists the phone numbers in the update request.
Type: Array of [UpdatePhoneNumberRequestItem](API_voice-chime_UpdatePhoneNumberRequestItem.md) objects
Required: Yes

## Response Syntax
<a name="API_voice-chime_BatchUpdatePhoneNumber_ResponseSyntax"></a>

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
<a name="API_voice-chime_BatchUpdatePhoneNumber_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberErrors](#API_voice-chime_BatchUpdatePhoneNumber_ResponseSyntax) **   <a name="chimesdk-voice-chime_BatchUpdatePhoneNumber-response-PhoneNumberErrors"></a>
A list of failed phone numbers and their error messages.
Type: Array of [PhoneNumberError](API_voice-chime_PhoneNumberError.md) objects

## Errors
<a name="API_voice-chime_BatchUpdatePhoneNumber_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
The requested resource couldn't be found.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The number of customer requests exceeds the request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client isn't authorized to request a resource.
HTTP Status Code: 401

## See Also
<a name="API_voice-chime_BatchUpdatePhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/BatchUpdatePhoneNumber)
