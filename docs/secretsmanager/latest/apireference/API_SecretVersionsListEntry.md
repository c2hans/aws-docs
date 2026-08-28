---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_SecretVersionsListEntry.html
---

# SecretVersionsListEntry
<a name="API_SecretVersionsListEntry"></a>

A structure that contains information about one version of a secret.

## Contents
<a name="API_SecretVersionsListEntry_Contents"></a>

 ** CreatedDate **   <a name="SecretsManager-Type-SecretVersionsListEntry-CreatedDate"></a>
The date and time this version of the secret was created.
Type: Timestamp
Required: No

 ** KmsKeyIds **   <a name="SecretsManager-Type-SecretVersionsListEntry-KmsKeyIds"></a>
The KMS keys used to encrypt the secret version.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** LastAccessedDate **   <a name="SecretsManager-Type-SecretVersionsListEntry-LastAccessedDate"></a>
The date that this version of the secret was last accessed. Note that the resolution of this field is at the date level and does not include the time.
Type: Timestamp
Required: No

 ** VersionId **   <a name="SecretsManager-Type-SecretVersionsListEntry-VersionId"></a>
The unique version identifier of this version of the secret.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 64.
Required: No

 ** VersionStages **   <a name="SecretsManager-Type-SecretVersionsListEntry-VersionStages"></a>
An array of staging labels that are currently associated with this version of the secret.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_SecretVersionsListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/SecretVersionsListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/SecretVersionsListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/SecretVersionsListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
