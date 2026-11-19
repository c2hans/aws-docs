---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_IamCredentialProvider.html
---

# IamCredentialProvider

An IAM credential provider for authenticating requests. This structure contains the configuration for authenticating with a target endpoint using IAM credentials and SigV4 signing.

## Contents
<a name="API_IamCredentialProvider_Contents"></a>

 ** service **   <a name="BedrockAgentCore-Type-IamCredentialProvider-service"></a>
The name of the AWS service used for SigV4 signing. This value identifies the service to authenticate with when sending requests to the target endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

 ** region **   <a name="BedrockAgentCore-Type-IamCredentialProvider-region"></a>
The AWS Region used for SigV4 signing. If not specified, defaults to the Region of the resource that makes the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`
Required: No

## See Also
<a name="API_IamCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/IamCredentialProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/IamCredentialProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/IamCredentialProvider)
