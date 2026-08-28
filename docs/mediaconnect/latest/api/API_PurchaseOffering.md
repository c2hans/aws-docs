---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_PurchaseOffering.html
---

# PurchaseOffering
<a name="API_PurchaseOffering"></a>

 Submits a request to purchase an offering. If you already have an active reservation, you can't purchase another offering.

## Request Syntax
<a name="API_PurchaseOffering_RequestSyntax"></a>

```
POST /v1/offerings/{{offeringArn}} HTTP/1.1
Content-type: application/json

{
   "reservationName": "{{string}}",
   "start": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PurchaseOffering_RequestParameters"></a>

The request uses the following URI parameters.

 ** [offeringArn](#API_PurchaseOffering_RequestSyntax) **   <a name="mediaconnect-PurchaseOffering-request-uri-offeringArn"></a>
 The Amazon Resource Name (ARN) of the offering.
Required: Yes

## Request Body
<a name="API_PurchaseOffering_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [reservationName](#API_PurchaseOffering_RequestSyntax) **   <a name="mediaconnect-PurchaseOffering-request-reservationName"></a>
 The name that you want to use for the reservation.
Type: String
Required: Yes

 ** [start](#API_PurchaseOffering_RequestSyntax) **   <a name="mediaconnect-PurchaseOffering-request-start"></a>
 The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC).
You can specify any date and time between 12:00am on the first day of the current month to the current time on today's date, inclusive. Specify the start in a 24-hour notation. Use the following format: `YYYY-MM-DDTHH:mm:SSZ`, where `T` and `Z` are literal characters. For example, to specify 11:30pm on March 5, 2020, enter `2020-03-05T23:30:00Z`.
Type: String
Required: Yes

## Response Syntax
<a name="API_PurchaseOffering_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "reservation": {
      "currencyCode": "string",
      "duration": number,
      "durationUnits": "string",
      "end": "string",
      "offeringArn": "string",
      "offeringDescription": "string",
      "pricePerUnit": "string",
      "priceUnits": "string",
      "reservationArn": "string",
      "reservationName": "string",
      "reservationState": "string",
      "resourceSpecification": {
         "reservedBitrate": number,
         "resourceType": "string"
      },
      "start": "string"
   }
}
```

## Response Elements
<a name="API_PurchaseOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [reservation](#API_PurchaseOffering_ResponseSyntax) **   <a name="mediaconnect-PurchaseOffering-response-reservation"></a>
The details of the reservation that you just created when you purchased the offering.
Type: [Reservation](API_Reservation.md) object

## Errors
<a name="API_PurchaseOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_PurchaseOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/PurchaseOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/PurchaseOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
