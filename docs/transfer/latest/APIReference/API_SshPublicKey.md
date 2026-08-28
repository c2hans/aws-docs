---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_SshPublicKey.html
---

# SshPublicKey
<a name="API_SshPublicKey"></a>

Provides information about the public Secure Shell (SSH) key that is associated with a Transfer Family user for the specific file transfer protocol-enabled server (as identified by `ServerId`). The information returned includes the date the key was imported, the public key contents, and the public key ID. A user can store more than one SSH public key associated with their user name on a specific server.

## Contents
<a name="API_SshPublicKey_Contents"></a>

 ** DateImported **   <a name="TransferFamily-Type-SshPublicKey-DateImported"></a>
Specifies the date that the public key was added to the Transfer Family user.
Type: Timestamp
Required: Yes

 ** SshPublicKeyBody **   <a name="TransferFamily-Type-SshPublicKey-SshPublicKeyBody"></a>
Specifies the content of the SSH public key as specified by the `PublicKeyId`.
 AWS Transfer Family accepts RSA, ECDSA, and ED25519 keys.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `\s*(ssh|ecdsa)-[a-z0-9-]+[ \t]+(([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{1,3})?(={0,3})?)(\s*|[ \t]+[\S \t]*\s*)`
Required: Yes

 ** SshPublicKeyId **   <a name="TransferFamily-Type-SshPublicKey-SshPublicKeyId"></a>
Specifies the `SshPublicKeyId` parameter contains the identifier of the public key.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `key-[0-9a-f]{17}`
Required: Yes

## See Also
<a name="API_SshPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/SshPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/SshPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/SshPublicKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
