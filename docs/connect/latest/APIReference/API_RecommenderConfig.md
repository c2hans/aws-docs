---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RecommenderConfig.html
---

# RecommenderConfig
<a name="API_RecommenderConfig"></a>

Configuration for the recommender used to generate personalized recommendations included in an outbound web notification.

## Contents
<a name="API_RecommenderConfig_Contents"></a>

 ** DomainName **   <a name="connect-Type-RecommenderConfig-DomainName"></a>
The name of the Amazon Personalize domain that hosts the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** RecommenderName **   <a name="connect-Type-RecommenderConfig-RecommenderName"></a>
The name of the recommender used to generate the recommendations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Context **   <a name="connect-Type-RecommenderConfig-Context"></a>
A map of contextual key-value pairs supplied to the recommender to influence the recommendations returned.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_RecommenderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RecommenderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RecommenderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RecommenderConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
