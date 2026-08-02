---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserEmbeddingExperienceConfiguration.html
---

# RegisteredUserEmbeddingExperienceConfiguration
<a name="API_RegisteredUserEmbeddingExperienceConfiguration"></a>

The type of experience you want to embed. For registered users, you can embed Quick dashboards or the Amazon Quick Sight console.

**Note**
Exactly one of the experience configurations is required. You can choose `Dashboard` or `QuickSightConsole`. You cannot choose more than one experience configuration.

## Contents
<a name="API_RegisteredUserEmbeddingExperienceConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dashboard **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-Dashboard"></a>
The configuration details for providing a dashboard embedding experience.
Type: [RegisteredUserDashboardEmbeddingConfiguration](API_RegisteredUserDashboardEmbeddingConfiguration.md) object
Required: No

 ** DashboardVisual **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-DashboardVisual"></a>
The type of embedding experience. In this case, Amazon Quick Sight visuals.
Type: [RegisteredUserDashboardVisualEmbeddingConfiguration](API_RegisteredUserDashboardVisualEmbeddingConfiguration.md) object
Required: No

 ** GenerativeQnA **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-GenerativeQnA"></a>
The configuration details for embedding the Generative Q&A experience.
For more information about embedding the Generative Q&A experience, see [Embedding Overview](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html) in the *Amazon Quick Sight User Guide*.
Type: [RegisteredUserGenerativeQnAEmbeddingConfiguration](API_RegisteredUserGenerativeQnAEmbeddingConfiguration.md) object
Required: No

 ** QSearchBar **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-QSearchBar"></a>
The configuration details for embedding the Q search bar.
For more information about embedding the Q search bar, see [Embedding Overview](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html) in the *Amazon Quick Sight User Guide*.
Type: [RegisteredUserQSearchBarEmbeddingConfiguration](API_RegisteredUserQSearchBarEmbeddingConfiguration.md) object
Required: No

 ** QuickChat **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-QuickChat"></a>
The configuration details for embedding the Quick chat agent.
Type: [RegisteredUserQuickChatEmbeddingConfiguration](API_RegisteredUserQuickChatEmbeddingConfiguration.md) object
Required: No

 ** QuickSightConsole **   <a name="QS-Type-RegisteredUserEmbeddingExperienceConfiguration-QuickSightConsole"></a>
The configuration details for providing each Amazon Quick Sight console embedding experience. This can be used along with custom permissions to restrict access to certain features. For more information, see [Customizing Access to the Amazon Quick Sight Console](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html) in the *Amazon Quick User Guide*.
Use ` [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html) ` where you want to provide an authoring portal that allows users to create data sources, datasets, analyses, and dashboards. The users who accesses an embedded Amazon Quick Sight console needs to belong to the author or admin security cohort. If you want to restrict permissions to some of these features, add a custom permissions profile to the user with the ` [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html) ` API operation. Use the ` [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html) ` API operation to add a new user with a custom permission profile attached. For more information, see the following sections in the *Amazon Quick User Guide*:
+  [Embedding the Full Functionality of the Amazon Quick Sight Console for Authenticated Users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-full-console-for-authenticated-users.html)
+  [Customizing Access to the Amazon Quick Console](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html)
For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon Quick Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html).
Type: [RegisteredUserQuickSightConsoleEmbeddingConfiguration](API_RegisteredUserQuickSightConsoleEmbeddingConfiguration.md) object
Required: No

## See Also
<a name="API_RegisteredUserEmbeddingExperienceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserEmbeddingExperienceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserEmbeddingExperienceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserEmbeddingExperienceConfiguration)
