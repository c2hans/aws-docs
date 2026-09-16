---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ProxyConfig.html
---

# ProxyConfig
<a name="API_ProxyConfig"></a>

Contains configuration for PROXY protocol version 2 (PPv2) support on an AWS Transfer Family server. When enabled, Transfer Family reads the added PPv2 header from incoming connections to extract the client's source IP address. This address is then available in Amazon CloudWatch Logs entries and is passed to custom identity providers during authentication, enabling IP-based access policies. For more information, see [Working with Network Load Balancers](https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html).

## Contents
<a name="API_ProxyConfig_Contents"></a>

 ** SftpMode **   <a name="TransferFamily-Type-ProxyConfig-SftpMode"></a>
Specifies whether the Transfer Family server requires or ignores a PPv2 header containing the client's source IP address on incoming SFTP connections. If you don't specify a value, the default is `NONE`
+  `NONE`: the server reads and ignores any PPv2 header on incoming SFTP connections. This is the default value. Use this value when your SFTP server is not behind an NLB, or when you do not need to preserve the client's source IP address through an NLB.
+  `PROXY_PROTOCOL_V2_ENFORCED`: the server requires a valid PPv2 header on every incoming SFTP connection. When a valid header is present, the server applies it and uses the source IP address from the header. If a connection arrives without a PPv2 header, the server refuses the connection and logs an error to Amazon CloudWatch Logs indicating that the expected PPv2 header was missing. Use this value when your SFTP server is behind an NLB with PPv2 enabled on the target group.
**Important**
With `PROXY_PROTOCOL_V2_ENFORCED` you must restrict the server's VPC endpoint security group to allow inbound traffic only via the trusted NLB. For more information, see [Working with Network Load Balancers](https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html).
Type: String
Valid Values: `NONE | PROXY_PROTOCOL_V2_ENFORCED`
Required: No

## See Also
<a name="API_ProxyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ProxyConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ProxyConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ProxyConfig)
