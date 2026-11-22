---
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_DescriptorSourceFromUrl.html
---

# DescriptorSourceFromUrl

 A URL-based descriptor source that identifies where descriptor content is retrieved from.

## Contents
<a name="API_DescriptorSourceFromUrl_Contents"></a>

 ** url **   <a name="agentregistry-Type-DescriptorSourceFromUrl-url"></a>
 The URL from which the descriptor content is retrieved. For an agent skill that synchronizes its SKILL.md from GitHub, this is the GitHub folder URL. The data plane doesn't return Amazon S3 (`s3://`) source URLs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https|s3)://.*`
Required: Yes

## See Also
<a name="API_DescriptorSourceFromUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/DescriptorSourceFromUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/DescriptorSourceFromUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/DescriptorSourceFromUrl)
