---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResultByTime.html
---

# ResultByTime
<a name="API_ResultByTime"></a>

The result that's associated with a time period.

## Contents
<a name="API_ResultByTime_Contents"></a>

 ** Estimated **   <a name="awscostmanagement-Type-ResultByTime-Estimated"></a>
Determines whether the result is estimated.
Type: Boolean
Required: No

 ** Groups **   <a name="awscostmanagement-Type-ResultByTime-Groups"></a>
The groups that this time period includes.
Type: Array of [Group](API_Group.md) objects
Required: No

 ** TimePeriod **   <a name="awscostmanagement-Type-ResultByTime-TimePeriod"></a>
The time period that the result covers.
Type: [DateInterval](API_DateInterval.md) object
Required: No

 ** Total **   <a name="awscostmanagement-Type-ResultByTime-Total"></a>
The total amount of cost or usage accrued during the time period.
Type: String to [MetricValue](API_MetricValue.md) object map
Key Length Constraints: Minimum length of 0. Maximum length of 1024.
Key Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ResultByTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ResultByTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ResultByTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ResultByTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
