---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UpdateRecommendationStatusItem.html
---

# UpdateRecommendationStatusItem
<a name="API_UpdateRecommendationStatusItem"></a>

Defines the operational recommendation item that needs a status update.

## Contents
<a name="API_UpdateRecommendationStatusItem_Contents"></a>

 ** resourceId **   <a name="resiliencehub-Type-UpdateRecommendationStatusItem-resourceId"></a>
Resource identifier of the operational recommendation item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** targetAccountId **   <a name="resiliencehub-Type-UpdateRecommendationStatusItem-targetAccountId"></a>
Identifier of the target AWS account.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** targetRegion **   <a name="resiliencehub-Type-UpdateRecommendationStatusItem-targetRegion"></a>
Identifier of the target AWS Region.
Type: String
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

## See Also
<a name="API_UpdateRecommendationStatusItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/UpdateRecommendationStatusItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/UpdateRecommendationStatusItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/UpdateRecommendationStatusItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
