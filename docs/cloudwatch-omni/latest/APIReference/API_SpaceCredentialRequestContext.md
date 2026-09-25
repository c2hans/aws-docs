---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SpaceCredentialRequestContext.html
---

# SpaceCredentialRequestContext
<a name="API_SpaceCredentialRequestContext"></a>

Identifies what the credentials are for: either an existing space, or a target account in a domain. Specify spaceId, or both domainId and targetAccountId.

## Contents
<a name="API_SpaceCredentialRequestContext_Contents"></a>

 ** domainId **   <a name="cloudwatchomni-Type-SpaceCredentialRequestContext-domainId"></a>
The ID of the domain, when returning credentials for a target account that does not yet have a space.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: No

 ** spaceId **   <a name="cloudwatchomni-Type-SpaceCredentialRequestContext-spaceId"></a>
The ID of an existing space to return credentials for.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** targetAccountId **   <a name="cloudwatchomni-Type-SpaceCredentialRequestContext-targetAccountId"></a>
The ID of the target member account. Required when domainId is set.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_SpaceCredentialRequestContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/SpaceCredentialRequestContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/SpaceCredentialRequestContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/SpaceCredentialRequestContext)
