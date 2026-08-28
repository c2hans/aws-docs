---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnonymousUserQSearchBarEmbeddingConfiguration.html
---

# AnonymousUserQSearchBarEmbeddingConfiguration
<a name="API_AnonymousUserQSearchBarEmbeddingConfiguration"></a>

The settings that you want to use with the Q search bar.

## Contents
<a name="API_AnonymousUserQSearchBarEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialTopicId **   <a name="QS-Type-AnonymousUserQSearchBarEmbeddingConfiguration-InitialTopicId"></a>
The Quick Sight Q topic ID of the legacy topic that you want the anonymous user to see first. This ID is included in the output URL. When the URL in response is accessed, Quick Sight renders the Q search bar with this legacy topic pre-selected.
The Amazon Resource Name (ARN) of this Q legacy topic must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request fails with an `InvalidParameterValueException` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+`
Required: Yes

## See Also
<a name="API_AnonymousUserQSearchBarEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnonymousUserQSearchBarEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnonymousUserQSearchBarEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnonymousUserQSearchBarEmbeddingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
