---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_SftpPortWithOptions.html
---

# SftpPortWithOptions
<a name="API_SftpPortWithOptions"></a>

Specifies the configuration for a single SFTP port on a Transfer Family server that uses the SFTP protocol and has a `PUBLIC` endpoint. Each entry in the `SftpPorts` list is an `SftpPortWithOptions` object that pairs a port number with a communication mode.

## Contents
<a name="API_SftpPortWithOptions_Contents"></a>

 ** SftpPort **   <a name="TransferFamily-Type-SftpPortWithOptions-SftpPort"></a>
The port on which the Transfer Family server listens for SFTP connections. Specify any integer from 2000 to 65535, or 22. This value is required for each entry in the `SftpPorts` list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** CommunicationMode **   <a name="TransferFamily-Type-SftpPortWithOptions-CommunicationMode"></a>
Determines whether the server or the client sends data first when a client establishes an SFTP connection on this port. Valid values are `SERVER_TALK_FIRST` and `CLIENT_TALK_FIRST`. For a description of each mode, see the `SftpPorts` property. This value is optional.
Type: String
Valid Values: `CLIENT_TALK_FIRST | SERVER_TALK_FIRST`
Required: No

## See Also
<a name="API_SftpPortWithOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/SftpPortWithOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/SftpPortWithOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/SftpPortWithOptions)
