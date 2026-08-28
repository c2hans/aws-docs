---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserDashboardEmbeddingConfiguration.html
---

# RegisteredUserDashboardEmbeddingConfiguration
<a name="API_RegisteredUserDashboardEmbeddingConfiguration"></a>

Information about the dashboard you want to embed.

## Contents
<a name="API_RegisteredUserDashboardEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InitialDashboardId **   <a name="QS-Type-RegisteredUserDashboardEmbeddingConfiguration-InitialDashboardId"></a>
The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this dashboard if the user has permissions to view it.
If the user does not have permission to view this dashboard, they see a permissions error message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** FeatureConfigurations **   <a name="QS-Type-RegisteredUserDashboardEmbeddingConfiguration-FeatureConfigurations"></a>
The feature configurations of an embbedded Amazon Quick Sight dashboard.
Type: [RegisteredUserDashboardFeatureConfigurations](API_RegisteredUserDashboardFeatureConfigurations.md) object
Required: No

## See Also
<a name="API_RegisteredUserDashboardEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserDashboardEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserDashboardEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserDashboardEmbeddingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
