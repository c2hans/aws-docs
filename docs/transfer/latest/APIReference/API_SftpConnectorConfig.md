---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_SftpConnectorConfig.html
---

# SftpConnectorConfig
<a name="API_SftpConnectorConfig"></a>

Contains the details for an SFTP connector object. The connector object is used for transferring files to and from a partner's SFTP server.

## Contents
<a name="API_SftpConnectorConfig_Contents"></a>

 ** MaxConcurrentConnections **   <a name="TransferFamily-Type-SftpConnectorConfig-MaxConcurrentConnections"></a>
Specify the number of concurrent connections that your connector creates to the remote server. The default value is `1`. The maximum values is `5`.
If you are using the AWS Management Console, the default value is `5`.
This parameter specifies the number of active connections that your connector can establish with the remote server at the same time. Increasing this value can enhance connector performance when transferring large file batches by enabling parallel operations.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** TrustedHostKeys **   <a name="TransferFamily-Type-SftpConnectorConfig-TrustedHostKeys"></a>
The public portion of the host key, or keys, that are used to identify the external server to which you are connecting. You can use the `ssh-keyscan` command against the SFTP server to retrieve the necessary key.
 `TrustedHostKeys` is optional for `CreateConnector`. If not provided, you can use `TestConnection` to retrieve the server host key during the initial connection attempt, and subsequently update the connector with the observed host key.
When creating connectors with egress config (VPC\_LATTICE type connectors), since host name is not something we can verify, the only accepted trusted host key format is `key-type key-body` without the host name. For example: `ssh-rsa AAAAB3Nza...<long-string-for-public-key>`
The three standard SSH public key format elements are `<key type>`, `<body base64>`, and an optional `<comment>`, with spaces between each element. Specify only the `<key type>` and `<body base64>`: do not enter the `<comment>` portion of the key.
For the trusted host key, AWS Transfer Family accepts RSA and ECDSA keys.
+ For RSA keys, the `<key type>` string is `ssh-rsa`.
+ For ECDSA keys, the `<key type>` string is either `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, or `ecdsa-sha2-nistp521`, depending on the size of the key you generated.
Run this command to retrieve the SFTP server host key, where your SFTP server name is `ftp.host.com`.
 `ssh-keyscan ftp.host.com`
This prints the public host key to standard output.
 `ftp.host.com ssh-rsa AAAAB3Nza...<long-string-for-public-key>`
Copy and paste this string into the `TrustedHostKeys` field for the `create-connector` command or into the **Trusted host keys** field in the console.
For VPC Lattice type connectors (VPC\_LATTICE), remove the hostname from the key and use only the `key-type key-body` format. In this example, it should be: `ssh-rsa AAAAB3Nza...<long-string-for-public-key>`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** UserSecretId **   <a name="TransferFamily-Type-SftpConnectorConfig-UserSecretId"></a>
The identifier for the secret (in AWS Secrets Manager) that contains the SFTP user's private key, password, or both. The identifier must be the Amazon Resource Name (ARN) of the secret.
+ Required when creating an SFTP connector
+ Optional when updating an existing SFTP connector
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_SftpConnectorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/SftpConnectorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/SftpConnectorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/SftpConnectorConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
