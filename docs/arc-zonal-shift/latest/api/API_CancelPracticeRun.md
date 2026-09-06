---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelPracticeRun.html
---

# CancelPracticeRun
<a name="API_CancelPracticeRun"></a>

Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.

## Request Syntax
<a name="API_CancelPracticeRun_RequestSyntax"></a>

```
DELETE /practiceruns/{{zonalShiftId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelPracticeRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [zonalShiftId](#API_CancelPracticeRun_RequestSyntax) **   <a name="zonalshift-CancelPracticeRun-request-uri-zonalShiftId"></a>
The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

## Request Body
<a name="API_CancelPracticeRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelPracticeRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "awayFrom": "string",
   "comment": "string",
   "expiryTime": number,
   "resourceIdentifier": "string",
   "startTime": number,
   "status": "string",
   "zonalShiftId": "string"
}
```

## Response Elements
<a name="API_CancelPracticeRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awayFrom](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic was moved away from for a resource that you specified for the practice run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.

 ** [comment](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-comment"></a>
The initial comment that you entered about the practice run. Be aware that this comment can be overwritten by AWS if the automatic check for balanced capacity fails. For more information, see [ Capacity checks for practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [expiryTime](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-expiryTime"></a>
The expiry time (expiration time) for an on-demand practice run zonal shift is 30 minutes from the time when you start the practice run, unless you cancel it before that time. However, be aware that the `expiryTime` field for practice run zonal shifts always has a value of 1 minute.
Type: Timestamp

 ** [resourceIdentifier](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-resourceIdentifier"></a>
The identifier for the resource that you canceled a practice run zonal shift for. The identifier is the Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [startTime](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-startTime"></a>
The time (UTC) when the zonal shift starts.
Type: Timestamp

 ** [status](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-status"></a>
A status for the practice run that you canceled (expected status is **CANCELED**).
The `Status` for a practice run zonal shift can have one of the following values:
Type: String
Valid Values: `ACTIVE | EXPIRED | CANCELED`

 ** [zonalShiftId](#API_CancelPracticeRun_ResponseSyntax) **   <a name="zonalshift-CancelPracticeRun-response-zonalShiftId"></a>
The identifier of the practice run zonal shift in Amazon Application Recovery Controller that was canceled.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_CancelPracticeRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** reason **
The reason for the conflict exception.
 ** zonalShiftId **
The zonal shift ID associated with the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The input requested a resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CancelPracticeRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/CancelPracticeRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/CancelPracticeRun)
