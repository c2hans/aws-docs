---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CredentialLockerSummary.html
---

# CredentialLockerSummary
<a name="API_CredentialLockerSummary"></a>

Structure describing one Credential Locker.

## Contents
<a name="API_CredentialLockerSummary_Contents"></a>

 ** Arn **   <a name="managedintegrations-Type-CredentialLockerSummary-Arn"></a>
The Amazon Resource Name (ARN) of the credential locker.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:credential-locker/[0-9a-zA-Z]+`
Required: No

 ** CreatedAt **   <a name="managedintegrations-Type-CredentialLockerSummary-CreatedAt"></a>
The timestampe value of when the credential locker was created at.
Type: Timestamp
Required: No

 ** Id **   <a name="managedintegrations-Type-CredentialLockerSummary-Id"></a>
The id of the credential locker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]*`
Required: No

 ** Name **   <a name="managedintegrations-Type-CredentialLockerSummary-Name"></a>
The name of the credential locker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

## See Also
<a name="API_CredentialLockerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/CredentialLockerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/CredentialLockerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/CredentialLockerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
