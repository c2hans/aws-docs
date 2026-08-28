---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyPrivacyBudget.html
---

# DifferentialPrivacyPrivacyBudget
<a name="API_DifferentialPrivacyPrivacyBudget"></a>

Specifies the configured epsilon value and the utility in terms of total aggregations, as well as the remaining aggregations available.

## Contents
<a name="API_DifferentialPrivacyPrivacyBudget_Contents"></a>

 ** aggregations **   <a name="API-Type-DifferentialPrivacyPrivacyBudget-aggregations"></a>
This information includes the configured epsilon value and the utility in terms of total aggregations, as well as the remaining aggregations.
Type: Array of [DifferentialPrivacyPrivacyBudgetAggregation](API_DifferentialPrivacyPrivacyBudgetAggregation.md) objects
Required: Yes

 ** epsilon **   <a name="API-Type-DifferentialPrivacyPrivacyBudget-epsilon"></a>
The epsilon value that you configured.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: Yes

## See Also
<a name="API_DifferentialPrivacyPrivacyBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyPrivacyBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyPrivacyBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyPrivacyBudget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
