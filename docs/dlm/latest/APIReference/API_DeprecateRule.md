---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_DeprecateRule.html
---

# DeprecateRule
<a name="API_DeprecateRule"></a>

 **[Custom AMI policies only]** Specifies an AMI deprecation rule for AMIs created by an AMI lifecycle policy.

For age-based schedules, you must specify **Interval** and **IntervalUnit**. For count-based schedules, you must specify **Count**.

## Contents
<a name="API_DeprecateRule_Contents"></a>

 ** Count **   <a name="dlm-Type-DeprecateRule-Count"></a>
If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate. The count must be less than or equal to the schedule's retention count, and it can't be greater than 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Interval **   <a name="dlm-Type-DeprecateRule-Interval"></a>
If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule. The period must be less than or equal to the schedule's retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-DeprecateRule-IntervalUnit"></a>
The unit of time in which to measure the **Interval**.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_DeprecateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/DeprecateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/DeprecateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/DeprecateRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
