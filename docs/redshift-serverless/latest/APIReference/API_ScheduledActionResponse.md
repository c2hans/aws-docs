---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledActionResponse.html
---

# ScheduledActionResponse
<a name="API_ScheduledActionResponse"></a>

The returned scheduled action object.

## Contents
<a name="API_ScheduledActionResponse_Contents"></a>

 ** endTime **   <a name="redshiftserverless-Type-ScheduledActionResponse-endTime"></a>
The end time of
Type: Timestamp
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-ScheduledActionResponse-namespaceName"></a>
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** nextInvocations **   <a name="redshiftserverless-Type-ScheduledActionResponse-nextInvocations"></a>
An array of timestamps of when the next scheduled actions will trigger.
Type: Array of timestamps
Required: No

 ** roleArn **   <a name="redshiftserverless-Type-ScheduledActionResponse-roleArn"></a>
The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Management Guide
Type: String
Required: No

 ** schedule **   <a name="redshiftserverless-Type-ScheduledActionResponse-schedule"></a>
The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.
+ Format of at timestamp is `yyyy-mm-ddThh:mm:ss`. For example, `2016-03-04T17:27:00`.
+ Format of cron expression is `(Minutes Hours Day-of-month Month Day-of-week Year)`. For example, `"(0 10 ? * MON *)"`. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.
Type: [Schedule](API_Schedule.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** scheduledActionDescription **   <a name="redshiftserverless-Type-ScheduledActionResponse-scheduledActionDescription"></a>
The description of the scheduled action.
Type: String
Required: No

 ** scheduledActionName **   <a name="redshiftserverless-Type-ScheduledActionResponse-scheduledActionName"></a>
The name of the scheduled action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 60.
Pattern: `[a-z0-9-]+`
Required: No

 ** scheduledActionUuid **   <a name="redshiftserverless-Type-ScheduledActionResponse-scheduledActionUuid"></a>
The uuid of the scheduled action.
Type: String
Required: No

 ** startTime **   <a name="redshiftserverless-Type-ScheduledActionResponse-startTime"></a>
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
Type: Timestamp
Required: No

 ** state **   <a name="redshiftserverless-Type-ScheduledActionResponse-state"></a>
The state of the scheduled action.
Type: String
Valid Values: `ACTIVE | DISABLED`
Required: No

 ** targetAction **   <a name="redshiftserverless-Type-ScheduledActionResponse-targetAction"></a>
A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.
 `"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`
Type: [TargetAction](API_TargetAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ScheduledActionResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ScheduledActionResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ScheduledActionResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ScheduledActionResponse)
