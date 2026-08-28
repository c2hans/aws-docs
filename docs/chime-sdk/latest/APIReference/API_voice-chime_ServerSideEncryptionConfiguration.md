---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ServerSideEncryptionConfiguration.html
---

# ServerSideEncryptionConfiguration
<a name="API_voice-chime_ServerSideEncryptionConfiguration"></a>

A structure that contains the configuration settings for server-side encryption.

**Note**
We only support symmetric keys. Do not use asymmetric or HMAC keys, or KMS aliases.

## Contents
<a name="API_voice-chime_ServerSideEncryptionConfiguration_Contents"></a>

 ** KmsKeyArn **   <a name="chimesdk-Type-voice-chime_ServerSideEncryptionConfiguration-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt the enrollment data in a voice profile domain. Asymmetric customer managed keys are not supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

## See Also
<a name="API_voice-chime_ServerSideEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/ServerSideEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/ServerSideEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/ServerSideEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
