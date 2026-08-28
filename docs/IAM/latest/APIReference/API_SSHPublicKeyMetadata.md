---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SSHPublicKeyMetadata.html
---

# SSHPublicKeyMetadata
<a name="API_SSHPublicKeyMetadata"></a>

Contains information about an SSH public key, without the key's body or fingerprint.

This data type is used as a response element in the [ListSSHPublicKeys](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListSSHPublicKeys.html) operation.

## Contents
<a name="API_SSHPublicKeyMetadata_Contents"></a>

 ** SSHPublicKeyId **
The unique identifier for the SSH public key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** Status **
The status of the SSH public key. `Active` means that the key can be used for authentication with an CodeCommit repository. `Inactive` means that the key cannot be used.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: Yes

 ** UploadDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the SSH public key was uploaded.
Type: Timestamp
Required: Yes

 ** UserName **
The name of the IAM user associated with the SSH public key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## See Also
<a name="API_SSHPublicKeyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SSHPublicKeyMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SSHPublicKeyMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SSHPublicKeyMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
