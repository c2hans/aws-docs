---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_APIErrorType.html
---

# APIErrorType
<a name="API_APIErrorType"></a>

The error Secrets Manager encountered while retrieving an individual secret as part of [BatchGetSecretValue](API_BatchGetSecretValue.md).

## Contents
<a name="API_APIErrorType_Contents"></a>

 ** ErrorCode **   <a name="SecretsManager-Type-APIErrorType-ErrorCode"></a>
The error Secrets Manager encountered while retrieving an individual secret as part of [BatchGetSecretValue](API_BatchGetSecretValue.md), for example `ResourceNotFoundException`,`InvalidParameterException`, `InvalidRequestException`, `DecryptionFailure`, or `AccessDeniedException`.
Type: String
Required: No

 ** Message **   <a name="SecretsManager-Type-APIErrorType-Message"></a>
A message describing the error.
Type: String
Required: No

 ** SecretId **   <a name="SecretsManager-Type-APIErrorType-SecretId"></a>
The ARN or name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_APIErrorType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/APIErrorType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/APIErrorType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/APIErrorType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
