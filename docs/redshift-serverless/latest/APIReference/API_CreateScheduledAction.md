---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html
---

# CreateScheduledAction
<a name="API_CreateScheduledAction"></a>

Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the `CreateSnapshot` API operation.

## Request Syntax
<a name="API_CreateScheduledAction_RequestSyntax"></a>

```
{
   "enabled": {{boolean}},
   "endTime": {{number}},
   "namespaceName": "{{string}}",
   "roleArn": "{{string}}",
   "schedule": { ... },
   "scheduledActionDescription": "{{string}}",
   "scheduledActionName": "{{string}}",
   "startTime": {{number}},
   "targetAction": { ... }
}
```

## Request Parameters
<a name="API_CreateScheduledAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [enabled](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-enabled"></a>
Indicates whether the schedule is enabled. If false, the scheduled action does not trigger. For more information about `state` of the scheduled action, see [ScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledAction.html).
Type: Boolean
Required: No

 ** [endTime](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-endTime"></a>
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
Type: Timestamp
Required: No

 ** [namespaceName](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-namespaceName"></a>
The name of the namespace for which to create a scheduled action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [roleArn](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-roleArn"></a>
The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Management Guide
Type: String
Required: Yes

 ** [schedule](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-schedule"></a>
The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.
+ Format of at timestamp is `yyyy-mm-ddThh:mm:ss`. For example, `2016-03-04T17:27:00`.
+ Format of cron expression is `(Minutes Hours Day-of-month Month Day-of-week Year)`. For example, `"(0 10 ? * MON *)"`. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.
Type: [Schedule](API_Schedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [scheduledActionDescription](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-scheduledActionDescription"></a>
The description of the scheduled action.
Type: String
Required: No

 ** [scheduledActionName](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-scheduledActionName"></a>
The name of the scheduled action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 60.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [startTime](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-startTime"></a>
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
Type: Timestamp
Required: No

 ** [targetAction](#API_CreateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-CreateScheduledAction-request-targetAction"></a>
A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.
 `"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`
Type: [TargetAction](API_TargetAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateScheduledAction_ResponseSyntax"></a>

```
{
   "scheduledAction": {
      "endTime": number,
      "namespaceName": "string",
      "nextInvocations": [ number ],
      "roleArn": "string",
      "schedule": { ... },
      "scheduledActionDescription": "string",
      "scheduledActionName": "string",
      "scheduledActionUuid": "string",
      "startTime": number,
      "state": "string",
      "targetAction": { ... }
   }
}
```

## Response Elements
<a name="API_CreateScheduledAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledAction](#API_CreateScheduledAction_ResponseSyntax) **   <a name="redshiftserverless-CreateScheduledAction-response-scheduledAction"></a>
The returned `ScheduledAction` object that describes the properties of a scheduled action.
Type: [ScheduledActionResponse](API_ScheduledActionResponse.md) object

## Errors
<a name="API_CreateScheduledAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateScheduledAction)
