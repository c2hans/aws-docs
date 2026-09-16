---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeReservation.html
---

# DescribeReservation
<a name="API_DescribeReservation"></a>

 Displays the details of a reservation. The response includes the reservation name, state, start date and time, and the details of the offering that make up the rest of the reservation (such as price, duration, and outbound bandwidth).

## Request Syntax
<a name="API_DescribeReservation_RequestSyntax"></a>

```
GET /v1/reservations/{{reservationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeReservation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reservationArn](#API_DescribeReservation_RequestSyntax) **   <a name="mediaconnect-DescribeReservation-request-uri-reservationArn"></a>
The Amazon Resource Name (ARN) of the offering.
Required: Yes

## Request Body
<a name="API_DescribeReservation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeReservation_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_DescribeReservation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reservation](#API_DescribeReservation_ResponseSyntax) **   <a name="mediaconnect-DescribeReservation-response-reservation"></a>
 A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate.
Type: [Reservation](API_Reservation.md) object

## Errors
<a name="API_DescribeReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

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
<a name="API_DescribeReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DescribeReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DescribeReservation)
