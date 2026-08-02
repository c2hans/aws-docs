---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_As2AsyncMdnConnectorConfig.html
---

# As2AsyncMdnConnectorConfig
<a name="API_As2AsyncMdnConnectorConfig"></a>

Contains the configuration details for asynchronous Message Disposition Notification (MDN) responses in AS2 connectors. This configuration specifies where asynchronous MDN responses should be sent and which servers should handle them.

## Contents
<a name="API_As2AsyncMdnConnectorConfig_Contents"></a>

 ** ServerIds **   <a name="TransferFamily-Type-As2AsyncMdnConnectorConfig-ServerIds"></a>
A list of server identifiers that can handle asynchronous MDN responses. You can specify between 1 and 10 server IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: No

 ** Url **   <a name="TransferFamily-Type-As2AsyncMdnConnectorConfig-Url"></a>
The URL endpoint where asynchronous MDN responses should be sent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_As2AsyncMdnConnectorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/As2AsyncMdnConnectorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/As2AsyncMdnConnectorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/As2AsyncMdnConnectorConfig)
