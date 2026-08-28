---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SSHPublicKey.html
---

# SSHPublicKey
<a name="API_SSHPublicKey"></a>

Contains information about an SSH public key.

This data type is used as a response element in the [GetSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetSSHPublicKey.html) and [UploadSSHPublicKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadSSHPublicKey.html) operations.

## Contents
<a name="API_SSHPublicKey_Contents"></a>

 ** Fingerprint **
The MD5 message digest of the SSH public key.
Type: String
Length Constraints: Fixed length of 48.
Pattern: `[:\w]+`
Required: Yes

 ** SSHPublicKeyBody **
The SSH public key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

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

 ** UserName **
The name of the IAM user associated with the SSH public key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** UploadDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the SSH public key was uploaded.
Type: Timestamp
Required: No

## See Also
<a name="API_SSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SSHPublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
