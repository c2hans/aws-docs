---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_JiraProjectMetadata.html
---

# JiraProjectMetadata
<a name="API_JiraProjectMetadata"></a>

Contains metadata about a Jira project that is integrated with the service.

## Contents
<a name="API_JiraProjectMetadata_Contents"></a>

 ** name **   <a name="securityagent-Type-JiraProjectMetadata-name"></a>
Name of the resource e.g. repository name, etc.
Type: String
Required: Yes

 ** projectId **   <a name="securityagent-Type-JiraProjectMetadata-projectId"></a>
The Jira project identifier.
Type: String
Required: Yes

 ** projectKey **   <a name="securityagent-Type-JiraProjectMetadata-projectKey"></a>
The Jira project key, for example PROJ.
Type: String
Required: Yes

 ** providerResourceId **   <a name="securityagent-Type-JiraProjectMetadata-providerResourceId"></a>
Provider Id of the resource e.g. GitHub repository id, etc.
Type: String
Required: Yes

 ** projectName **   <a name="securityagent-Type-JiraProjectMetadata-projectName"></a>
The display name of the Jira project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_JiraProjectMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/JiraProjectMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/JiraProjectMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/JiraProjectMetadata)
