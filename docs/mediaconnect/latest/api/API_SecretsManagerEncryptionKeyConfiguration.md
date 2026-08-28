---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SecretsManagerEncryptionKeyConfiguration.html
---

# SecretsManagerEncryptionKeyConfiguration
<a name="API_SecretsManagerEncryptionKeyConfiguration"></a>

The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

## Contents
<a name="API_SecretsManagerEncryptionKeyConfiguration_Contents"></a>

 ** roleArn **   <a name="mediaconnect-Type-SecretsManagerEncryptionKeyConfiguration-roleArn"></a>
The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+`
Required: Yes

 ** secretArn **   <a name="mediaconnect-Type-SecretsManagerEncryptionKeyConfiguration-secretArn"></a>
The ARN of the AWS Secrets Manager secret used for transit encryption.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`
Required: Yes

## See Also
<a name="API_SecretsManagerEncryptionKeyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SecretsManagerEncryptionKeyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SecretsManagerEncryptionKeyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SecretsManagerEncryptionKeyConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
