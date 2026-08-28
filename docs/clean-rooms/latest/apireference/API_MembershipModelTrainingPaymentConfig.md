---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipModelTrainingPaymentConfig.html
---

# MembershipModelTrainingPaymentConfig
<a name="API_MembershipModelTrainingPaymentConfig"></a>

An object representing the collaboration member's model training payment responsibilities set by the collaboration creator.

## Contents
<a name="API_MembershipModelTrainingPaymentConfig_Contents"></a>

 ** isResponsible **   <a name="API-Type-MembershipModelTrainingPaymentConfig-isResponsible"></a>
Indicates whether the collaboration member has accepted to pay for model training costs (`TRUE`) or has not accepted to pay for model training costs (`FALSE`).
If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for model training costs.
+ If you set the value to `TRUE` but you are not responsible to pay for model training costs.
Type: Boolean
Required: Yes

## See Also
<a name="API_MembershipModelTrainingPaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipModelTrainingPaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipModelTrainingPaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipModelTrainingPaymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
