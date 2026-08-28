---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretValueEntry.html
---

# SecretValueEntry
<a name="API_SecretValueEntry"></a>

A structure that contains the secret value and other details for a secret.

## Contents
<a name="API_SecretValueEntry_Contents"></a>

 ** ARN **   <a name="SecretsManager-Type-SecretValueEntry-ARN"></a>
The Amazon Resource Name (ARN) of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** CreatedDate **   <a name="SecretsManager-Type-SecretValueEntry-CreatedDate"></a>
The date the secret was created.
Type: Timestamp
Required: No

 ** Name **   <a name="SecretsManager-Type-SecretValueEntry-Name"></a>
The friendly name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** SecretBinary **   <a name="SecretsManager-Type-SecretValueEntry-SecretBinary"></a>
The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. The parameter represents the binary data as a [base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) string.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** SecretString **   <a name="SecretsManager-Type-SecretValueEntry-SecretString"></a>
The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Required: No

 ** VersionId **   <a name="SecretsManager-Type-SecretValueEntry-VersionId"></a>
The unique version identifier of this version of the secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** VersionStages **   <a name="SecretsManager-Type-SecretValueEntry-VersionStages"></a>
A list of all of the staging labels currently attached to this version of the secret.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_SecretValueEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/SecretValueEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/SecretValueEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/SecretValueEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
