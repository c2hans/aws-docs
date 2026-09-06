---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_SftpConnectorConnectionDetails.html
---

# SftpConnectorConnectionDetails
<a name="API_SftpConnectorConnectionDetails"></a>

Contains the details for an SFTP connector connection.

## Contents
<a name="API_SftpConnectorConnectionDetails_Contents"></a>

 ** HostKey **   <a name="TransferFamily-Type-SftpConnectorConnectionDetails-HostKey"></a>
The SSH public key of the remote SFTP server. This is returned during the initial connection attempt when you call `TestConnection`. It allows you to retrieve the valid server host key to update the connector when you are unable to obtain it in advance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_SftpConnectorConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/SftpConnectorConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/SftpConnectorConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/SftpConnectorConnectionDetails)
