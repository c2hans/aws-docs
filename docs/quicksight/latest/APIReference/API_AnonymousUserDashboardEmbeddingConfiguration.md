---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnonymousUserDashboardEmbeddingConfiguration.html
---

# AnonymousUserDashboardEmbeddingConfiguration
<a name="API_AnonymousUserDashboardEmbeddingConfiguration"></a>

Information about the dashboard that you want to embed.

## Contents
<a name="API_AnonymousUserDashboardEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialDashboardId **   <a name="QS-Type-AnonymousUserDashboardEmbeddingConfiguration-InitialDashboardId"></a>
The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this dashboard.
The Amazon Resource Name (ARN) of this dashboard must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request will fail with `InvalidParameterValueException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** DisabledFeatures **   <a name="QS-Type-AnonymousUserDashboardEmbeddingConfiguration-DisabledFeatures"></a>
A list of all disabled features of a specified anonymous dashboard.
Type: Array of strings
Valid Values: `SHARED_VIEW`
Required: No

 ** EnabledFeatures **   <a name="QS-Type-AnonymousUserDashboardEmbeddingConfiguration-EnabledFeatures"></a>
A list of all enabled features of a specified anonymous dashboard.
Type: Array of strings
Valid Values: `SHARED_VIEW`
Required: No

 ** FeatureConfigurations **   <a name="QS-Type-AnonymousUserDashboardEmbeddingConfiguration-FeatureConfigurations"></a>
The feature configuration for an embedded dashboard.
Type: [AnonymousUserDashboardFeatureConfigurations](API_AnonymousUserDashboardFeatureConfigurations.md) object
Required: No

## See Also
<a name="API_AnonymousUserDashboardEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnonymousUserDashboardEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnonymousUserDashboardEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnonymousUserDashboardEmbeddingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
