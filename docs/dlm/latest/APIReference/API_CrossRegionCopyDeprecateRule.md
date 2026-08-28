---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyDeprecateRule.html
---

# CrossRegionCopyDeprecateRule
<a name="API_CrossRegionCopyDeprecateRule"></a>

 **[Custom AMI policies only]** Specifies an AMI deprecation rule for cross-Region AMI copies created by an AMI policy.

## Contents
<a name="API_CrossRegionCopyDeprecateRule_Contents"></a>

 ** Interval **   <a name="dlm-Type-CrossRegionCopyDeprecateRule-Interval"></a>
The period after which to deprecate the cross-Region AMI copies. The period must be less than or equal to the cross-Region AMI copy retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** IntervalUnit **   <a name="dlm-Type-CrossRegionCopyDeprecateRule-IntervalUnit"></a>
The unit of time in which to measure the **Interval**. For example, to deprecate a cross-Region AMI copy after 3 months, specify `Interval=3` and `IntervalUnit=MONTHS`.
Type: String
Valid Values: `DAYS | WEEKS | MONTHS | YEARS`
Required: No

## See Also
<a name="API_CrossRegionCopyDeprecateRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/CrossRegionCopyDeprecateRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/CrossRegionCopyDeprecateRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/CrossRegionCopyDeprecateRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Lifecycle Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
