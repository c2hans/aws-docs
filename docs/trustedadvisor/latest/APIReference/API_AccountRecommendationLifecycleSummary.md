---
source_url: https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_AccountRecommendationLifecycleSummary.html
---

# AccountRecommendationLifecycleSummary
<a name="API_AccountRecommendationLifecycleSummary"></a>

Summary of an AccountRecommendationLifecycle for an Organization Recommendation

## Contents
<a name="API_AccountRecommendationLifecycleSummary_Contents"></a>

 ** accountId **   <a name="ta-Type-AccountRecommendationLifecycleSummary-accountId"></a>
The AWS account ID
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

 ** accountRecommendationArn **   <a name="ta-Type-AccountRecommendationLifecycleSummary-accountRecommendationArn"></a>
The Recommendation ARN
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w-]+:trustedadvisor::\d{12}:recommendation\/[\w-]+`
Required: No

 ** lastUpdatedAt **   <a name="ta-Type-AccountRecommendationLifecycleSummary-lastUpdatedAt"></a>
When the Recommendation was last updated
Type: Timestamp
Required: No

 ** lifecycleStage **   <a name="ta-Type-AccountRecommendationLifecycleSummary-lifecycleStage"></a>
The lifecycle stage from AWS Trusted Advisor Priority
Type: String
Valid Values: `in_progress | pending_response | dismissed | resolved`
Required: No

 ** updatedOnBehalfOf **   <a name="ta-Type-AccountRecommendationLifecycleSummary-updatedOnBehalfOf"></a>
The person on whose behalf a Technical Account Manager (TAM) updated the recommendation. This information is only available when a Technical Account Manager takes an action on a recommendation managed by AWS Trusted Advisor Priority
Type: String
Required: No

 ** updatedOnBehalfOfJobTitle **   <a name="ta-Type-AccountRecommendationLifecycleSummary-updatedOnBehalfOfJobTitle"></a>
The job title of the person on whose behalf a Technical Account Manager (TAM) updated the recommendation. This information is only available when a Technical Account Manager takes an action on a recommendation managed by AWS Trusted Advisor Priority
Type: String
Required: No

 ** updateReason **   <a name="ta-Type-AccountRecommendationLifecycleSummary-updateReason"></a>
Reason for the lifecycle stage change
Type: String
Length Constraints: Minimum length of 10. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** updateReasonCode **   <a name="ta-Type-AccountRecommendationLifecycleSummary-updateReasonCode"></a>
Reason code for the lifecycle state change
Type: String
Valid Values: `non_critical_account | temporary_account | valid_business_case | other_methods_available | low_priority | not_applicable | other`
Required: No

## See Also
<a name="API_AccountRecommendationLifecycleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/trustedadvisor-2022-09-15/AccountRecommendationLifecycleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/trustedadvisor-2022-09-15/AccountRecommendationLifecycleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/trustedadvisor-2022-09-15/AccountRecommendationLifecycleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Trusted Advisor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query trustedadvisor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
