---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateIntegrationDetails.html
---

# UpdateIntegrationDetails
<a name="API_UpdateIntegrationDetails"></a>

Contains details required to update a code security integration with a specific repository provider.

## Contents
<a name="API_UpdateIntegrationDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** github **   <a name="inspector2-Type-UpdateIntegrationDetails-github"></a>
Details specific to updating an integration with GitHub.
Type: [UpdateGitHubIntegrationDetail](API_UpdateGitHubIntegrationDetail.md) object
Required: No

 ** gitlabSelfManaged **   <a name="inspector2-Type-UpdateIntegrationDetails-gitlabSelfManaged"></a>
Details specific to updating an integration with a self-managed GitLab instance.
Type: [UpdateGitLabSelfManagedIntegrationDetail](API_UpdateGitLabSelfManagedIntegrationDetail.md) object
Required: No

## See Also
<a name="API_UpdateIntegrationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateIntegrationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateIntegrationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateIntegrationDetails)
