---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_RetainRule.html
---

# RetainRule
<a name="API_RetainRule"></a>

 **[Custom snapshot and AMI policies only]** Specifies a retention rule for snapshots created by snapshot policies, or for AMIs created by AMI policies.

**Note**
For snapshot policies that have an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html), this retention rule applies to standard tier retention. When the retention threshold is met, snapshots are moved from the standard to the archive tier.
For snapshot policies that do not have an **ArchiveRule**, snapshots are permanently deleted when this retention threshold is met.

You can retain snapshots based on either a count or a time interval.
+  **Count-based retention**

  You must specify **Count**. If you specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you can specify a retention count of `0` to archive snapshots immediately after creation. If you specify a [FastRestoreRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html), [ShareRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html), or a [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html), then you must specify a retention count of `1` or more.
+  **Age-based retention**

  You must specify **Interval** and **IntervalUnit**. If you specify an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html) for the schedule, then you can specify a retention interval of `0` days to archive snapshots immediately after creation. If you specify a [FastRestoreRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html), [ShareRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html), or a [CrossRegionCopyRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html), then you must specify a retention interval of `1` day or more.

## Contents
<a name="API_RetainRule_Contents"></a>

 ** Count **   <a name="dlm-Type-RetainRule-Count"></a>
The number of snapshots to retain for each volume, up to a maximum of 1000. For example if you want to retain a maximum of three snapshots, specify `3`. When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** Interval **   <a name="dlm-Type-RetainRule-Interval"></a>
The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-RetainRule-IntervalUnit"></a>
The unit of time for time-based retention. For example, to retain snapshots for 3 months, specify `Interval=3` and `IntervalUnit=MONTHS`. Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an [ArchiveRule](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html).
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_RetainRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/RetainRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/RetainRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/RetainRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
