---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetAutoshiftObserverNotificationStatus.html
---

# GetAutoshiftObserverNotificationStatus
<a name="API_GetAutoshiftObserverNotificationStatus"></a>

Returns the status of the autoshift observer notification. Autoshift observer notifications notify you through Amazon EventBridge when there is an autoshift event for zonal autoshift. The status can be `ENABLED` or `DISABLED`. When `ENABLED`, a notification is sent when an autoshift is triggered. When `DISABLED`, notifications are not sent.

## Request Syntax
<a name="API_GetAutoshiftObserverNotificationStatus_RequestSyntax"></a>

```
GET /autoshift-observer-notification HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutoshiftObserverNotificationStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAutoshiftObserverNotificationStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutoshiftObserverNotificationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_GetAutoshiftObserverNotificationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetAutoshiftObserverNotificationStatus_ResponseSyntax) **   <a name="zonalshift-GetAutoshiftObserverNotificationStatus-response-status"></a>
The status of autoshift observer notification. If the status is `ENABLED`, ARC includes all autoshift events when you use the Amazon EventBridge pattern `Autoshift In Progress`. When the status is `DISABLED`, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_GetAutoshiftObserverNotificationStatus_Errors"></a>

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

## See Also
<a name="API_GetAutoshiftObserverNotificationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/GetAutoshiftObserverNotificationStatus)
