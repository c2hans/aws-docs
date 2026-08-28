---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateRule.html
---

# CreateRule
<a name="API_CreateRule"></a>

 **[Custom snapshot and AMI policies only]** Specifies when the policy should create snapshots or AMIs.

**Note**
You must specify either **CronExpression**, or **Interval**, **IntervalUnit**, and **Times**.
If you need to specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you must specify a creation frequency of at least 28 days.

## Contents
<a name="API_CreateRule_Contents"></a>

 ** CronExpression **   <a name="dlm-Type-CreateRule-CronExpression"></a>
The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see the [Cron and rate expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 106.
Pattern: `cron\([^\n]{11,100}\)`
Required: No

 ** Interval **   <a name="dlm-Type-CreateRule-Interval"></a>
The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-CreateRule-IntervalUnit"></a>
The interval unit.
Type: String
Valid Values: `HOURS`
Required: No

 ** Location **   <a name="dlm-Type-CreateRule-Location"></a>
 **[Custom snapshot policies only]** Specifies the destination for snapshots created by the policy. The allowed destinations depend on the location of the targeted resources.
+ If the policy targets resources in a Region, then you must create snapshots in the same Region as the source resource.
+ If the policy targets resources in a Local Zone, you can create snapshots in the same Local Zone or in its parent Region.
+ If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost or in its parent Region.
Specify one of the following values:
+ To create snapshots in the same Region as the source resource, specify `CLOUD`.
+ To create snapshots in the same Local Zone as the source resource, specify `LOCAL_ZONE`.
+ To create snapshots on the same Outpost as the source resource, specify `OUTPOST_LOCAL`.
Default: `CLOUD`
Type: String
Valid Values: `CLOUD | OUTPOST_LOCAL | LOCAL_ZONE`
Required: No

 ** Scripts **   <a name="dlm-Type-CreateRule-Scripts"></a>
 **[Custom snapshot policies that target instances only]** Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances. This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation.
For more information, see [Automating application-consistent snapshots with pre and post scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html).
Type: Array of [Script](API_Script.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** Times **   <a name="dlm-Type-CreateRule-Times"></a>
The time, in UTC, to start the operation. The supported format is hh:mm.
The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Fixed length of 5.
Pattern: `^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
Required: No

## See Also
<a name="API_CreateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CreateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CreateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CreateRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
