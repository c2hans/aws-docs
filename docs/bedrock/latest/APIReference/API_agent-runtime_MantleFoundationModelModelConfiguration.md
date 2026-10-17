---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_MantleFoundationModelModelConfiguration.html
---

# MantleFoundationModelModelConfiguration
<a name="API_agent-runtime_MantleFoundationModelModelConfiguration"></a>

Model configuration for a Mantle foundation model.

## Contents
<a name="API_agent-runtime_MantleFoundationModelModelConfiguration_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-agent-runtime_MantleFoundationModelModelConfiguration-modelArn"></a>
The ARN of the Mantle foundation model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`
Required: Yes

 ** projectId **   <a name="bedrock-Type-agent-runtime_MantleFoundationModelModelConfiguration-projectId"></a>
The Amazon Bedrock project ID used for billing and usage attribution. If you don't specify a value, the service uses the default project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `(proj_[a-zA-Z0-9]+|default)`
Required: No

## See Also
<a name="API_agent-runtime_MantleFoundationModelModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/MantleFoundationModelModelConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/MantleFoundationModelModelConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/MantleFoundationModelModelConfiguration)
