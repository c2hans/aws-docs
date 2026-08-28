---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateSnapshotScheduleActionParameters.html
---

# CreateSnapshotScheduleActionParameters
<a name="API_CreateSnapshotScheduleActionParameters"></a>

The parameters that you can use to configure a [scheduled action](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) to create a snapshot. For more information about creating a scheduled action, see [CreateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html).

## Contents
<a name="API_CreateSnapshotScheduleActionParameters_Contents"></a>

 ** namespaceName **   <a name="redshiftserverless-Type-CreateSnapshotScheduleActionParameters-namespaceName"></a>
The name of the namespace for which you want to configure a scheduled action to create a snapshot.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** snapshotNamePrefix **   <a name="redshiftserverless-Type-CreateSnapshotScheduleActionParameters-snapshotNamePrefix"></a>
A string prefix that is attached to the name of the snapshot created by the scheduled action. The final name of the snapshot is the string prefix appended by the date and time of when the snapshot was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 235.
Required: Yes

 ** retentionPeriod **   <a name="redshiftserverless-Type-CreateSnapshotScheduleActionParameters-retentionPeriod"></a>
The retention period of the snapshot created by the scheduled action.
Type: Integer
Required: No

 ** tags **   <a name="redshiftserverless-Type-CreateSnapshotScheduleActionParameters-tags"></a>
An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the snapshot.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_CreateSnapshotScheduleActionParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateSnapshotScheduleActionParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateSnapshotScheduleActionParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateSnapshotScheduleActionParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
