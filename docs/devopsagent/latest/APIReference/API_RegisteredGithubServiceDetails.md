---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredGithubServiceDetails.html
---

# RegisteredGithubServiceDetails
<a name="API_RegisteredGithubServiceDetails"></a>

Details specific to a registered GitHub service.

## Contents
<a name="API_RegisteredGithubServiceDetails_Contents"></a>

 ** owner **   <a name="devopsagent-Type-RegisteredGithubServiceDetails-owner"></a>
The GitHub repository owner name.
Type: String
Required: Yes

 ** ownerType **   <a name="devopsagent-Type-RegisteredGithubServiceDetails-ownerType"></a>
The GitHub repository owner type.
Type: String
Valid Values: `organization | user`
Required: Yes

 ** targetUrl **   <a name="devopsagent-Type-RegisteredGithubServiceDetails-targetUrl"></a>
The GitHub Enterprise Server instance URL (absent for github.com).
Type: String
Required: No

## See Also
<a name="API_RegisteredGithubServiceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredGithubServiceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredGithubServiceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredGithubServiceDetails)
