---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListReservations.html
---

# ListReservations
<a name="API_ListReservations"></a>

Returns a list of Reservation objects.

## Request Syntax
<a name="API_ListReservations_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReservations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListReservations_RequestSyntax) **   <a name="redshiftserverless-ListReservations-request-maxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListReservations_RequestSyntax) **   <a name="redshiftserverless-ListReservations-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListReservations_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "reservationsList": [
      {
         "capacity": number,
         "endDate": "string",
         "offering": {
            "currencyCode": "string",
            "duration": number,
            "hourlyCharge": number,
            "offeringId": "string",
            "offeringType": "string",
            "upfrontCharge": number
         },
         "reservationArn": "string",
         "reservationId": "string",
         "startDate": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReservations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReservations_ResponseSyntax) **   <a name="redshiftserverless-ListReservations-response-nextToken"></a>
The token to use when requesting the next set of items.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [reservationsList](#API_ListReservations_ResponseSyntax) **   <a name="redshiftserverless-ListReservations-response-reservationsList"></a>
The serverless reservations returned by the request.
Type: Array of [Reservation](API_Reservation.md) objects

## Errors
<a name="API_ListReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListReservations)
