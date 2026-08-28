---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_JobComputePaymentConfig.html
---

# JobComputePaymentConfig
<a name="API_JobComputePaymentConfig"></a>

An object representing the collaboration member's payment responsibilities set by the collaboration creator for query and job compute costs.

## Contents
<a name="API_JobComputePaymentConfig_Contents"></a>

 ** isResponsible **   <a name="API-Type-JobComputePaymentConfig-isResponsible"></a>
Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs (`TRUE`) or has not configured the collaboration member to pay for query and job compute costs (`FALSE`).
One or more members can be configured as payer candidates for query and job compute costs.
An error is returned if the collaboration creator sets a `FALSE` value for the member who can run queries and jobs.
Type: Boolean
Required: Yes

## See Also
<a name="API_JobComputePaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/JobComputePaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/JobComputePaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/JobComputePaymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
