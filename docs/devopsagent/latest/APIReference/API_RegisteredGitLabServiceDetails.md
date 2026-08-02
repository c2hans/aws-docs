---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredGitLabServiceDetails.html
---

# RegisteredGitLabServiceDetails
<a name="API_RegisteredGitLabServiceDetails"></a>

Details specific to a registered GitLab instance.

## Contents
<a name="API_RegisteredGitLabServiceDetails_Contents"></a>

 ** targetUrl **   <a name="devopsagent-Type-RegisteredGitLabServiceDetails-targetUrl"></a>
The GitLab instance URL.
Type: String
Required: Yes

 ** tokenType **   <a name="devopsagent-Type-RegisteredGitLabServiceDetails-tokenType"></a>
Type of GitLab access token
Type: String
Valid Values: `personal | group`
Required: Yes

 ** groupId **   <a name="devopsagent-Type-RegisteredGitLabServiceDetails-groupId"></a>
Optional GitLab group ID for group-level access tokens
Type: String
Required: No

## See Also
<a name="API_RegisteredGitLabServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredGitLabServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredGitLabServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredGitLabServiceDetails)
