---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListedConnector.html
---

# ListedConnector
<a name="API_ListedConnector"></a>

Returns details of the connector that is specified.

## Contents
<a name="API_ListedConnector_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-ListedConnector-Arn"></a>
The Amazon Resource Name (ARN) of the specified connector.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: No

 ** ConnectorId **   <a name="TransferFamily-Type-ListedConnector-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: No

 ** Url **   <a name="TransferFamily-Type-ListedConnector-Url"></a>
The URL of the partner's AS2 or SFTP endpoint.
When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_ListedConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListedConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListedConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListedConnector)
