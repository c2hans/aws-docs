---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_TrustedAccessResolutionContext.html
---

# TrustedAccessResolutionContext

Account and optional project context evaluated when resolving a trusted access program's status.

## Contents
<a name="API_TrustedAccessResolutionContext_Contents"></a>

 ** accountId **   <a name="bedrock-Type-TrustedAccessResolutionContext-accountId"></a>
AWS account for which the program status was resolved, including applicable organization settings.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** projectArn **   <a name="bedrock-Type-TrustedAccessResolutionContext-projectArn"></a>
The canonical ARN of the authorized named project for which participation was resolved. Omitted when the request has no project context.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_TrustedAccessResolutionContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TrustedAccessResolutionContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TrustedAccessResolutionContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TrustedAccessResolutionContext)
