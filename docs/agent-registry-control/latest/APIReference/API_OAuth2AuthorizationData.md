---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_OAuth2AuthorizationData.html
---

# OAuth2AuthorizationData

An OAuth 2.0 authorization that waits for a user's approval. The user opens `authorizationUrl` and approves access on GitHub. Amazon Bedrock AgentCore Identity then redirects the browser to the source's `returnUrl`. There, your application completes the authorization by calling the AgentCore Identity `CompleteResourceTokenAuth` operation with `userId`. If the source has no `returnUrl`, the user returns to the AWS Agent Registry console, which completes the authorization. After the authorization completes, the registry synchronizes the record without another request. If the user doesn't approve access before `expiresAt`, the record moves to `CREATE_FAILED` or `UPDATE_FAILED`. To start again, call `UpdateRegistryRecord` with `triggerSynchronization`.

## Contents
<a name="API_OAuth2AuthorizationData_Contents"></a>

 ** authorizationUrl **   <a name="agentregistrycontrol-Type-OAuth2AuthorizationData-authorizationUrl"></a>
The URL that the user opens to approve access. The link is valid for up to 10 minutes. Treat it as sensitive and give it only to the user who approves access.
Type: String
Required: Yes

 ** authorizationAttemptId **   <a name="agentregistrycontrol-Type-OAuth2AuthorizationData-authorizationAttemptId"></a>
The identifier of this authorization attempt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** expiresAt **   <a name="agentregistrycontrol-Type-OAuth2AuthorizationData-expiresAt"></a>
The timestamp when the authorization link expires, 10 minutes after the authorization started. A request that joins an authorization in progress gets less time, and the link might stop working shortly before this time.
Type: Timestamp
Required: No

 ** userId **   <a name="agentregistrycontrol-Type-OAuth2AuthorizationData-userId"></a>
The AgentCore Identity user ID that the authorization is for. Store it with your signed-in user and pass it as `userIdentifier.userId` when your application calls `CompleteResourceTokenAuth`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_OAuth2AuthorizationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/OAuth2AuthorizationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/OAuth2AuthorizationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/OAuth2AuthorizationData)
