---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartPracticeRun.html
---

# StartPracticeRun
<a name="API_StartPracticeRun"></a>

Start an on-demand practice run zonal shift in Amazon Application Recovery Controller. With zonal autoshift enabled, you can start an on-demand practice run to verify preparedness at any time. AWS also runs automated practice runs about weekly when you have enabled zonal autoshift.

For more information, see [ Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Application Recovery Controller Developer Guide.

## Request Syntax
<a name="API_StartPracticeRun_RequestSyntax"></a>

```
POST /practiceruns HTTP/1.1
Content-type: application/json

{
   "awayFrom": "{{string}}",
   "comment": "{{string}}",
   "resourceIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartPracticeRun_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartPracticeRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awayFrom](#API_StartPracticeRun_RequestSyntax) **   <a name="zonalshift-StartPracticeRun-request-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is shifted away from for the resource that you specify for the practice run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** [comment](#API_StartPracticeRun_RequestSyntax) **   <a name="zonalshift-StartPracticeRun-request-comment"></a>
The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by AWS if the automatic check for balanced capacity fails. For more information, see [ Capacity checks for practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: Yes

 ** [resourceIdentifier](#API_StartPracticeRun_RequestSyntax) **   <a name="zonalshift-StartPracticeRun-request-resourceIdentifier"></a>
The identifier for the resource that you want to start a practice run zonal shift for. The identifier is the Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_StartPracticeRun_ResponseSyntax"></a>

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
<a name="API_StartPracticeRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awayFrom](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-awayFrom"></a>
The Availability Zone (for example, `use1-az1`) that traffic is shifted away from for the resource that you specify for the practice run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.

 ** [comment](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-comment"></a>
The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by AWS if the automatic check for balanced capacity fails. For more information, see [ Capacity checks for practice runs](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html) in the Amazon Application Recovery Controller Developer Guide.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [expiryTime](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-expiryTime"></a>
The expiry time (expiration time) for an on-demand practice run zonal shift is 30 minutes from the time when you start the practice run, unless you cancel it before that time. However, be aware that the `expiryTime` field for practice run zonal shifts always has a value of 1 minute.
Type: Timestamp

 ** [resourceIdentifier](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-resourceIdentifier"></a>
The identifier for the resource that you want to shift traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [startTime](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-startTime"></a>
The time (UTC) when the zonal shift starts.
Type: Timestamp

 ** [status](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-status"></a>
A status for the practice run (expected status is **ACTIVE**).
Type: String
Valid Values: `ACTIVE | EXPIRED | CANCELED`

 ** [zonalShiftId](#API_StartPracticeRun_ResponseSyntax) **   <a name="zonalshift-StartPracticeRun-response-zonalShiftId"></a>
The identifier of a practice run zonal shift.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 36.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_StartPracticeRun_Errors"></a>

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
<a name="API_StartPracticeRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/StartPracticeRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/StartPracticeRun)
