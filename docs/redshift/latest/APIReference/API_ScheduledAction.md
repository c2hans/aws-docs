---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ScheduledAction.html
---

# ScheduledAction
<a name="API_ScheduledAction"></a>

Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see [ScheduledActionType](API_ScheduledActionType.md).

## Contents
<a name="API_ScheduledAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EndTime **
The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.
Type: Timestamp
Required: No

 ** IamRole **
The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the *Amazon Redshift Cluster Management Guide*.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NextInvocations.ScheduledActionTime.N **
List of times when the scheduled action will run.
Type: Array of timestamps
Required: No

 ** Schedule **
The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.
Format of at expressions is "`at(yyyy-mm-ddThh:mm:ss)`". For example, "`at(2016-03-04T17:27:00)`".
Format of cron expressions is "`cron(Minutes Hours Day-of-month Month Day-of-week Year)`". For example, "`cron(0 10 ? * MON *)`". For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide*.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ScheduledActionDescription **
The description of the scheduled action.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ScheduledActionName **
The name of the scheduled action.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** StartTime **
The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.
Type: Timestamp
Required: No

 ** State **
The state of the scheduled action. For example, `DISABLED`.
Type: String
Valid Values: `ACTIVE | DISABLED`
Required: No

 ** TargetAction **
A JSON format string of the Amazon Redshift API operation with input parameters.
"`{\"ResizeCluster\":{\"NodeType\":\"ra3.4xlarge\",\"ClusterIdentifier\":\"my-test-cluster\",\"NumberOfNodes\":3}}`".
Type: [ScheduledActionType](API_ScheduledActionType.md) object
Required: No

## See Also
<a name="API_ScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ScheduledAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
