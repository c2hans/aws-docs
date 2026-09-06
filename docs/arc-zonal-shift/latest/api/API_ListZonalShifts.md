---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html
---

# ListZonalShifts
<a name="API_ListZonalShifts"></a>

By default, lists only active zonal shifts in Amazon Application Recovery Controller in your AWS account in this AWS Region. To list historical zonal shifts, specify `--status CANCELED` or `--status EXPIRED`. Most practice runs have a status of EXPIRED. `ListZonalShifts` returns customer-initiated zonal shifts, as well as practice run zonal shifts that ARC started on your behalf for zonal autoshift.

For more information about listing autoshifts, see [ListAutoshifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html).

## Request Syntax
<a name="API_ListZonalShifts_RequestSyntax"></a>

```
GET /zonalshifts?maxResults={{maxResults}}&nextToken={{nextToken}}&resourceIdentifier={{resourceIdentifier}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListZonalShifts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListZonalShifts_RequestSyntax) **   <a name="zonalshift-ListZonalShifts-request-uri-maxResults"></a>
The number of objects that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListZonalShifts_RequestSyntax) **   <a name="zonalshift-ListZonalShifts-request-uri-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.

 ** [resourceIdentifier](#API_ListZonalShifts_RequestSyntax) **   <a name="zonalshift-ListZonalShifts-request-uri-resourceIdentifier"></a>
The identifier for the resource that you want to list zonal shifts for. The identifier is the Amazon Resource Name (ARN) for the resource.
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [status](#API_ListZonalShifts_RequestSyntax) **   <a name="zonalshift-ListZonalShifts-request-uri-status"></a>
A status for a zonal shift.
The `Status` for a zonal shift can have one of the following values:
+  **ACTIVE**: The zonal shift has been started and is active.
+  **EXPIRED**: The zonal shift has expired (the expiry time was exceeded).
+  **CANCELED**: The zonal shift was canceled.
Valid Values: `ACTIVE | EXPIRED | CANCELED`

## Request Body
<a name="API_ListZonalShifts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListZonalShifts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "awayFrom": "string",
         "comment": "string",
         "expiryTime": number,
         "practiceRunOutcome": "string",
         "resourceIdentifier": "string",
         "shiftType": "string",
         "startTime": number,
         "status": "string",
         "zonalShiftId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListZonalShifts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListZonalShifts_ResponseSyntax) **   <a name="zonalshift-ListZonalShifts-response-items"></a>
The items in the response list.
Type: Array of [ZonalShiftSummary](API_ZonalShiftSummary.md) objects

 ** [nextToken](#API_ListZonalShifts_ResponseSyntax) **   <a name="zonalshift-ListZonalShifts-response-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

## Errors
<a name="API_ListZonalShifts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListZonalShifts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/ListZonalShifts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ListZonalShifts)
