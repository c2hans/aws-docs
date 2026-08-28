---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_TestRecommendation.html
---

# TestRecommendation
<a name="API_TestRecommendation"></a>

Defines a test recommendation.

## Contents
<a name="API_TestRecommendation_Contents"></a>

 ** referenceId **   <a name="resiliencehub-Type-TestRecommendation-referenceId"></a>
Reference identifier for the test recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** appComponentId **   <a name="resiliencehub-Type-TestRecommendation-appComponentId"></a>
Indicates the identifier of the AppComponent.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{0,254}`
Required: No

 ** appComponentName **   <a name="resiliencehub-Type-TestRecommendation-appComponentName"></a>
Name of the AppComponent.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** dependsOnAlarms **   <a name="resiliencehub-Type-TestRecommendation-dependsOnAlarms"></a>
 A list of recommended alarms that are used in the test and must be exported before or with the test.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** description **   <a name="resiliencehub-Type-TestRecommendation-description"></a>
Description for the test recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** intent **   <a name="resiliencehub-Type-TestRecommendation-intent"></a>
Intent of the test recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** items **   <a name="resiliencehub-Type-TestRecommendation-items"></a>
The test recommendation items.
Type: Array of [RecommendationItem](API_RecommendationItem.md) objects
Required: No

 ** name **   <a name="resiliencehub-Type-TestRecommendation-name"></a>
Name of the test recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** prerequisite **   <a name="resiliencehub-Type-TestRecommendation-prerequisite"></a>
Prerequisite of the test recommendation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** recommendationId **   <a name="resiliencehub-Type-TestRecommendation-recommendationId"></a>
Identifier for the test recommendation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: No

 ** recommendationStatus **   <a name="resiliencehub-Type-TestRecommendation-recommendationStatus"></a>
Status of the recommended test.
Type: String
Valid Values: `Implemented | Inactive | NotImplemented | Excluded`
Required: No

 ** risk **   <a name="resiliencehub-Type-TestRecommendation-risk"></a>
Level of risk for this test recommendation.
Type: String
Valid Values: `Small | Medium | High`
Required: No

 ** type **   <a name="resiliencehub-Type-TestRecommendation-type"></a>
Type of test recommendation.
Type: String
Valid Values: `Software | Hardware | AZ | Region`
Required: No

## See Also
<a name="API_TestRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/TestRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/TestRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/TestRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
