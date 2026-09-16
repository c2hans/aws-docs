---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartDashboardSnapshotJobSchedule.html
---

# StartDashboardSnapshotJobSchedule
<a name="API_StartDashboardSnapshotJobSchedule"></a>

Starts an asynchronous job that runs an existing dashboard schedule and sends the dashboard snapshot through email.

Only one job can run simultaneously in a given schedule. Repeated requests are skipped with a `202` HTTP status code.

For more information, see [Scheduling and sending Amazon Quick Sight reports by email](https://docs.aws.amazon.com/quicksight/latest/user/sending-reports.html) and [Configuring email report settings for a Amazon Quick Sight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/email-reports-from-dashboard.html) in the *Amazon Quick Sight User Guide*.

## Request Syntax
<a name="API_StartDashboardSnapshotJobSchedule_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/schedules/{{ScheduleId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_StartDashboardSnapshotJobSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_StartDashboardSnapshotJobSchedule_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJobSchedule-request-uri-AwsAccountId"></a>
The ID of the AWS account that the dashboard snapshot job is executed in.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DashboardId](#API_StartDashboardSnapshotJobSchedule_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJobSchedule-request-uri-DashboardId"></a>
The ID of the dashboard that you want to start a snapshot job schedule for.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [ScheduleId](#API_StartDashboardSnapshotJobSchedule_RequestSyntax) **   <a name="QS-StartDashboardSnapshotJobSchedule-request-uri-ScheduleId"></a>
The ID of the schedule that you want to start a snapshot job schedule for. The schedule ID can be found in the Amazon Quick Sight console in the **Schedules** pane of the dashboard that the schedule is configured for.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_StartDashboardSnapshotJobSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartDashboardSnapshotJobSchedule_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_StartDashboardSnapshotJobSchedule_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_StartDashboardSnapshotJobSchedule_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJobSchedule-response-Status"></a>
The HTTP status of the request

The following data is returned in JSON format by the service.

 ** [RequestId](#API_StartDashboardSnapshotJobSchedule_ResponseSyntax) **   <a name="QS-StartDashboardSnapshotJobSchedule-response-RequestId"></a>
 The AWS request ID for this operation.
Type: String
Pattern: `.*\S.*`

## Errors
<a name="API_StartDashboardSnapshotJobSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_StartDashboardSnapshotJobSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/StartDashboardSnapshotJobSchedule)
