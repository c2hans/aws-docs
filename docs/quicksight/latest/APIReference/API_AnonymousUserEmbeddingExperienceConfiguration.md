---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnonymousUserEmbeddingExperienceConfiguration.html
---

# AnonymousUserEmbeddingExperienceConfiguration
<a name="API_AnonymousUserEmbeddingExperienceConfiguration"></a>

The type of experience you want to embed. For anonymous users, you can embed Quick dashboards.

## Contents
<a name="API_AnonymousUserEmbeddingExperienceConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dashboard **   <a name="QS-Type-AnonymousUserEmbeddingExperienceConfiguration-Dashboard"></a>
The type of embedding experience. In this case, Amazon Quick Sight dashboards.
Type: [AnonymousUserDashboardEmbeddingConfiguration](API_AnonymousUserDashboardEmbeddingConfiguration.md) object
Required: No

 ** DashboardVisual **   <a name="QS-Type-AnonymousUserEmbeddingExperienceConfiguration-DashboardVisual"></a>
The type of embedding experience. In this case, Amazon Quick Sight visuals.
Type: [AnonymousUserDashboardVisualEmbeddingConfiguration](API_AnonymousUserDashboardVisualEmbeddingConfiguration.md) object
Required: No

 ** GenerativeQnA **   <a name="QS-Type-AnonymousUserEmbeddingExperienceConfiguration-GenerativeQnA"></a>
The Generative Q&A experience that you want to use for anonymous user embedding.
Type: [AnonymousUserGenerativeQnAEmbeddingConfiguration](API_AnonymousUserGenerativeQnAEmbeddingConfiguration.md) object
Required: No

 ** QSearchBar **   <a name="QS-Type-AnonymousUserEmbeddingExperienceConfiguration-QSearchBar"></a>
The Q search bar that you want to use for anonymous user embedding.
Type: [AnonymousUserQSearchBarEmbeddingConfiguration](API_AnonymousUserQSearchBarEmbeddingConfiguration.md) object
Required: No

## See Also
<a name="API_AnonymousUserEmbeddingExperienceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnonymousUserEmbeddingExperienceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnonymousUserEmbeddingExperienceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnonymousUserEmbeddingExperienceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
