---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_As2ConnectorConfig.html
---

# As2ConnectorConfig
<a name="API_As2ConnectorConfig"></a>

Contains the details for an AS2 connector object. The connector object is used for AS2 outbound processes, to connect the AWS Transfer Family customer with the trading partner.

## Contents
<a name="API_As2ConnectorConfig_Contents"></a>

 ** AsyncMdnConfig **   <a name="TransferFamily-Type-As2ConnectorConfig-AsyncMdnConfig"></a>
Configuration settings for asynchronous Message Disposition Notification (MDN) responses. This allows you to configure where asynchronous MDN responses should be sent and which servers should handle them.
Type: [As2AsyncMdnConnectorConfig](API_As2AsyncMdnConnectorConfig.md) object
Required: No

 ** BasicAuthSecretId **   <a name="TransferFamily-Type-As2ConnectorConfig-BasicAuthSecretId"></a>
Provides Basic authentication support to the AS2 Connectors API. To use Basic authentication, you must provide the name or Amazon Resource Name (ARN) of a secret in AWS Secrets Manager.
The default value for this parameter is `null`, which indicates that Basic authentication is not enabled for the connector.
If the connector should use Basic authentication, the secret needs to be in the following format:
 `{ "Username": "user-name", "Password": "user-password" }`
Replace `user-name` and `user-password` with the credentials for the actual user that is being authenticated.
Note the following:
+ You are storing these credentials in Secrets Manager, *not passing them directly* into this API.
+ If you are using the API, SDKs, or CloudFormation to configure your connector, then you must create the secret before you can enable Basic authentication. However, if you are using the AWS management console, you can have the system create the secret for you.
If you have previously enabled Basic authentication for a connector, you can disable it by using the `UpdateConnector` API call. For example, if you are using the CLI, you can run the following command to remove Basic authentication:
 `update-connector --connector-id my-connector-id --as2-config 'BasicAuthSecretId=""'`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** Compression **   <a name="TransferFamily-Type-As2ConnectorConfig-Compression"></a>
Specifies whether the AS2 file is compressed.
Type: String
Valid Values: `ZLIB | DISABLED`
Required: No

 ** EncryptionAlgorithm **   <a name="TransferFamily-Type-As2ConnectorConfig-EncryptionAlgorithm"></a>
The algorithm that is used to encrypt the file.
Note the following:
+ Do not use the `DES_EDE3_CBC` algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm.
+ You can only specify `NONE` if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.
Type: String
Valid Values: `AES128_CBC | AES192_CBC | AES256_CBC | DES_EDE3_CBC | NONE`
Required: No

 ** LocalProfileId **   <a name="TransferFamily-Type-As2ConnectorConfig-LocalProfileId"></a>
A unique identifier for the AS2 local profile.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** MdnResponse **   <a name="TransferFamily-Type-As2ConnectorConfig-MdnResponse"></a>
Used for outbound requests (from an AWS Transfer Family connector to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous. Specify either of the following values:
+  `ASYNC`: The system expects an asynchronous MDN response, confirming that the file was transferred successfully (or not).
+  `SYNC`: The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not).
+  `NONE`: Specifies that no MDN response is required.
Type: String
Valid Values: `SYNC | NONE | ASYNC`
Required: No

 ** MdnSigningAlgorithm **   <a name="TransferFamily-Type-As2ConnectorConfig-MdnSigningAlgorithm"></a>
The signing algorithm for the MDN response.
If set to DEFAULT (or not set at all), the value for `SigningAlgorithm` is used.
Type: String
Valid Values: `SHA256 | SHA384 | SHA512 | SHA1 | NONE | DEFAULT`
Required: No

 ** MessageSubject **   <a name="TransferFamily-Type-As2ConnectorConfig-MessageSubject"></a>
Used as the `Subject` HTTP header attribute in AS2 messages that are being sent with the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u007E\t]+`
Required: No

 ** PartnerProfileId **   <a name="TransferFamily-Type-As2ConnectorConfig-PartnerProfileId"></a>
A unique identifier for the partner profile for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `p-([0-9a-f]{17})`
Required: No

 ** PreserveContentType **   <a name="TransferFamily-Type-As2ConnectorConfig-PreserveContentType"></a>
Allows you to use the Amazon S3 `Content-Type` that is associated with objects in S3 instead of having the content type mapped based on the file extension. This parameter is enabled by default when you create an AS2 connector from the console, but disabled by default when you create an AS2 connector by calling the API directly.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SigningAlgorithm **   <a name="TransferFamily-Type-As2ConnectorConfig-SigningAlgorithm"></a>
The algorithm that is used to sign the AS2 messages sent with the connector.
Type: String
Valid Values: `SHA256 | SHA384 | SHA512 | SHA1 | NONE`
Required: No

## See Also
<a name="API_As2ConnectorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/As2ConnectorConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/As2ConnectorConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/As2ConnectorConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
