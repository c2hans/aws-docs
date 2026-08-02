---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateGitLabSelfManagedIntegrationDetail.html
---

# CreateGitLabSelfManagedIntegrationDetail
<a name="API_CreateGitLabSelfManagedIntegrationDetail"></a>

Contains details required to create an integration with a self-managed GitLab instance.

## Contents
<a name="API_CreateGitLabSelfManagedIntegrationDetail_Contents"></a>

 ** accessToken **   <a name="inspector2-Type-CreateGitLabSelfManagedIntegrationDetail-accessToken"></a>
The personal access token used to authenticate with the self-managed GitLab instance.
Type: String
Required: Yes

 ** instanceUrl **   <a name="inspector2-Type-CreateGitLabSelfManagedIntegrationDetail-instanceUrl"></a>
The URL of the self-managed GitLab instance.
Type: String
Pattern: `https://[-a-zA-Z0-9()@:%_+.~#?&//=]{1,1024}`
Required: Yes

## See Also
<a name="API_CreateGitLabSelfManagedIntegrationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateGitLabSelfManagedIntegrationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateGitLabSelfManagedIntegrationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateGitLabSelfManagedIntegrationDetail)
