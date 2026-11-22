---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GitHubSynchronizedSource.html
---

# GitHubSynchronizedSource

A GitHub source that a skill record's content was synchronized from, and the commit that the registry read.

## Contents
<a name="API_GitHubSynchronizedSource_Contents"></a>

 ** commitId **   <a name="agentregistrycontrol-Type-GitHubSynchronizedSource-commitId"></a>
The commit that the source's branch or tag pointed to when the registry read it.
Type: String
Length Constraints: Minimum length of 40. Maximum length of 64.
Pattern: `([0-9a-f]{40}|[0-9a-f]{64})`
Required: Yes

 ** synchronizedAt **   <a name="agentregistrycontrol-Type-GitHubSynchronizedSource-synchronizedAt"></a>
The timestamp when the registry read the source.
Type: Timestamp
Required: Yes

 ** url **   <a name="agentregistrycontrol-Type-GitHubSynchronizedSource-url"></a>
The source URL that the registry read.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_GitHubSynchronizedSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/GitHubSynchronizedSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/GitHubSynchronizedSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/GitHubSynchronizedSource)
