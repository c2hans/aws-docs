---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DateInterval.html
---

# DateInterval
<a name="API_DateInterval"></a>

The time period of the request.

## Contents
<a name="API_DateInterval_Contents"></a>

 ** End **   <a name="awscostmanagement-Type-DateInterval-End"></a>
The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01`, AWS retrieves cost and usage data from the start date up to, but not including, `2017-05-01`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: Yes

 ** Start **   <a name="awscostmanagement-Type-DateInterval-Start"></a>
The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01`, AWS retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}:\d{2}Z)?`
Required: Yes

## See Also
<a name="API_DateInterval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DateInterval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DateInterval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DateInterval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
