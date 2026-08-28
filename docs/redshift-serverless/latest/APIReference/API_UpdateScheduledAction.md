---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_UpdateScheduledAction.html
---

# UpdateScheduledAction
<a name="API_UpdateScheduledAction"></a>

Updates a scheduled action.

## Request Syntax
<a name="API_UpdateScheduledAction_RequestSyntax"></a>

```
{
   "enabled": {{boolean}},
   "endTime": {{number}},
   "roleArn": "{{string}}",
   "schedule": { ... },
   "scheduledActionDescription": "{{string}}",
   "scheduledActionName": "{{string}}",
   "startTime": {{number}},
   "targetAction": { ... }
}
```

## Request Parameters
<a name="API_UpdateScheduledAction_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [enabled](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-enabled"></a>
Specifies whether to enable the scheduled action.
Type: Boolean
Required: No

 ** [endTime](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-endTime"></a>
The end time in UTC of the scheduled action to update.
Type: Timestamp
Required: No

 ** [roleArn](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-roleArn"></a>
The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Management Guide
Type: String
Required: No

 ** [schedule](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-schedule"></a>
The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.
+ Format of at timestamp is `yyyy-mm-ddThh:mm:ss`. For example, `2016-03-04T17:27:00`.
+ Format of cron expression is `(Minutes Hours Day-of-month Month Day-of-week Year)`. For example, `"(0 10 ? * MON *)"`. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.
Type: [Schedule](API_Schedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [scheduledActionDescription](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-scheduledActionDescription"></a>
The descripion of the scheduled action to update to.
Type: String
Required: No

 ** [scheduledActionName](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-scheduledActionName"></a>
The name of the scheduled action to update to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 60.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** [startTime](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-startTime"></a>
The start time in UTC of the scheduled action to update to.
Type: Timestamp
Required: No

 ** [targetAction](#API_UpdateScheduledAction_RequestSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-request-targetAction"></a>
A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.
 `"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`
Type: [TargetAction](API_TargetAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_UpdateScheduledAction_ResponseSyntax"></a>

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
<a name="API_UpdateScheduledAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [scheduledAction](#API_UpdateScheduledAction_ResponseSyntax) **   <a name="redshiftserverless-UpdateScheduledAction-response-scheduledAction"></a>
The ScheduledAction object that was updated.
Type: [ScheduledActionResponse](API_ScheduledActionResponse.md) object

## Errors
<a name="API_UpdateScheduledAction_Errors"></a>

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
<a name="API_UpdateScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/UpdateScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/UpdateScheduledAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
