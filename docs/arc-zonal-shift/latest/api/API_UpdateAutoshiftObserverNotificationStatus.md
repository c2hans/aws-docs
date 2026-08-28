---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateAutoshiftObserverNotificationStatus.html
---

# UpdateAutoshiftObserverNotificationStatus
<a name="API_UpdateAutoshiftObserverNotificationStatus"></a>

Update the status of autoshift observer notification. Autoshift observer notification enables you to be notified, through Amazon EventBridge, when there is an autoshift event for zonal autoshift.

If the status is `ENABLED`, ARC includes all autoshift events when you use the EventBridge pattern `Autoshift In Progress`. When the status is `DISABLED`, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.

For more information, see [ Notifications for practice runs and autoshifts](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftNotification) in the Amazon Application Recovery Controller Developer Guide.

## Request Syntax
<a name="API_UpdateAutoshiftObserverNotificationStatus_RequestSyntax"></a>

```
PUT /autoshift-observer-notification HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAutoshiftObserverNotificationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAutoshiftObserverNotificationStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateAutoshiftObserverNotificationStatus_RequestSyntax) **   <a name="zonalshift-UpdateAutoshiftObserverNotificationStatus-request-status"></a>
The status to set for autoshift observer notification. If the status is `ENABLED`, ARC includes all autoshift events when you use the Amazon EventBridge pattern `Autoshift In Progress`. When the status is `DISABLED`, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Syntax
<a name="API_UpdateAutoshiftObserverNotificationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateAutoshiftObserverNotificationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_UpdateAutoshiftObserverNotificationStatus_ResponseSyntax) **   <a name="zonalshift-UpdateAutoshiftObserverNotificationStatus-response-status"></a>
The status for autoshift observer notification.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateAutoshiftObserverNotificationStatus_Errors"></a>

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
<a name="API_UpdateAutoshiftObserverNotificationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/UpdateAutoshiftObserverNotificationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
