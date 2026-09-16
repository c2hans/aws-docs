---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ListGroundStationReservations.html
---

# ListGroundStationReservations
<a name="API_ListGroundStationReservations"></a>

Returns a list of reservations for a specified ground station.

## Request Syntax
<a name="API_ListGroundStationReservations_RequestSyntax"></a>

```
GET /groundstation/{{groundStationId}}/reservation?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&reservationTypes={{reservationTypes}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGroundStationReservations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-endTime"></a>
End time of the reservation window in UTC.
Required: Yes

 ** [groundStationId](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-groundStationId"></a>
ID of a ground station.
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

 ** [maxResults](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-maxResults"></a>
Maximum number of ground station reservations returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-nextToken"></a>
Next token returned in the request of a previous `ListGroundStationReservations` call. Used to get the next page of results.
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

 ** [reservationTypes](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-reservationTypes"></a>
Types of reservations to filter by.
Valid Values: `MAINTENANCE | CONTACT`

 ** [startTime](#API_ListGroundStationReservations_RequestSyntax) **   <a name="groundstation-ListGroundStationReservations-request-uri-startTime"></a>
Start time of the reservation window in UTC.
Required: Yes

## Request Body
<a name="API_ListGroundStationReservations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGroundStationReservations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reservationList": [
      {
         "antennaName": "string",
         "endTime": number,
         "groundStationId": "string",
         "reservationDetails": { ... },
         "reservationType": "string",
         "startTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListGroundStationReservations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListGroundStationReservations_ResponseSyntax) **   <a name="groundstation-ListGroundStationReservations-response-nextToken"></a>
Next token to be used in a subsequent `ListGroundStationReservations` call to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1000.
Pattern: `[A-Za-z0-9-/+_.=]+`

 ** [reservationList](#API_ListGroundStationReservations_ResponseSyntax) **   <a name="groundstation-ListGroundStationReservations-response-reservationList"></a>
List of ground station reservations.
Type: Array of [GroundStationReservationListItem](API_GroundStationReservationListItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListGroundStationReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

## See Also
<a name="API_ListGroundStationReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/ListGroundStationReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ListGroundStationReservations)
