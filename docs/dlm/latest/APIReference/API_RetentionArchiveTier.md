---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_RetentionArchiveTier.html
---

# RetentionArchiveTier
<a name="API_RetentionArchiveTier"></a>

 **[Custom snapshot policies only]** Describes the retention rule for archived snapshots. Once the archive retention threshold is met, the snapshots are permanently deleted from the archive tier.

**Note**
The archive retention rule must retain snapshots in the archive tier for a minimum of 90 days.

For **count-based schedules**, you must specify **Count**. For **age-based schedules**, you must specify **Interval** and ** IntervalUnit**.

For more information about using snapshot archiving, see [Considerations for snapshot lifecycle policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive).

## Contents
<a name="API_RetentionArchiveTier_Contents"></a>

 ** Count **   <a name="dlm-Type-RetentionArchiveTier-Count"></a>
The maximum number of snapshots to retain in the archive storage tier for each volume. The count must ensure that each snapshot remains in the archive tier for at least 90 days. For example, if the schedule creates snapshots every 30 days, you must specify a count of 3 or more to ensure that each snapshot is archived for at least 90 days.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Interval **   <a name="dlm-Type-RetentionArchiveTier-Interval"></a>
Specifies the period of time to retain snapshots in the archive tier. After this period expires, the snapshot is permanently deleted.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-RetentionArchiveTier-IntervalUnit"></a>
The unit of time in which to measure the **Interval**. For example, to retain a snapshots in the archive tier for 6 months, specify `Interval=6` and `IntervalUnit=MONTHS`.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_RetentionArchiveTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/RetentionArchiveTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/RetentionArchiveTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/RetentionArchiveTier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
