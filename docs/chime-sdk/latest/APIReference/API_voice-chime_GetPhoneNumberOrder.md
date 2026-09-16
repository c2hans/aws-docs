---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetPhoneNumberOrder.html
---

# GetPhoneNumberOrder
<a name="API_voice-chime_GetPhoneNumberOrder"></a>

Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.

## Request Syntax
<a name="API_voice-chime_GetPhoneNumberOrder_RequestSyntax"></a>

```
GET /phone-number-orders/{{phoneNumberOrderId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_voice-chime_GetPhoneNumberOrder_RequestParameters"></a>

The request uses the following URI parameters.

 ** [phoneNumberOrderId](#API_voice-chime_GetPhoneNumberOrder_RequestSyntax) **   <a name="chimesdk-voice-chime_GetPhoneNumberOrder-request-uri-PhoneNumberOrderId"></a>
The ID of the phone number order .
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: Yes

## Request Body
<a name="API_voice-chime_GetPhoneNumberOrder_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_voice-chime_GetPhoneNumberOrder_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberOrder": {
      "CreatedTimestamp": "string",
      "FocDate": "string",
      "OrderedPhoneNumbers": [
         {
            "E164PhoneNumber": "string",
            "Status": "string"
         }
      ],
      "OrderType": "string",
      "PhoneNumberOrderId": "string",
      "ProductType": "string",
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_voice-chime_GetPhoneNumberOrder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberOrder](#API_voice-chime_GetPhoneNumberOrder_ResponseSyntax) **   <a name="chimesdk-voice-chime_GetPhoneNumberOrder-response-PhoneNumberOrder"></a>
The phone number order details.
Type: [PhoneNumberOrder](API_voice-chime_PhoneNumberOrder.md) object

## Errors
<a name="API_voice-chime_GetPhoneNumberOrder_Errors"></a>

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
<a name="API_voice-chime_GetPhoneNumberOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/GetPhoneNumberOrder)
