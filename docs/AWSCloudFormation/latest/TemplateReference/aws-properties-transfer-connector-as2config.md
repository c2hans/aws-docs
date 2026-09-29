---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-connector-as2config.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector As2Config
<a name="aws-properties-transfer-connector-as2config"></a>

A structure that contains the parameters for an AS2 connector object.

## Syntax
<a name="aws-properties-transfer-connector-as2config-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-connector-as2config-syntax.json"></a>

```
{
  "[AsyncMdnConfig](#cfn-transfer-connector-as2config-asyncmdnconfig)" : {{ConnectorAsyncMdnConfig}},
  "[BasicAuthSecretId](#cfn-transfer-connector-as2config-basicauthsecretid)" : {{String}},
  "[Compression](#cfn-transfer-connector-as2config-compression)" : {{String}},
  "[EncryptionAlgorithm](#cfn-transfer-connector-as2config-encryptionalgorithm)" : {{String}},
  "[LocalProfileId](#cfn-transfer-connector-as2config-localprofileid)" : {{String}},
  "[MdnResponse](#cfn-transfer-connector-as2config-mdnresponse)" : {{String}},
  "[MdnSigningAlgorithm](#cfn-transfer-connector-as2config-mdnsigningalgorithm)" : {{String}},
  "[MessageSubject](#cfn-transfer-connector-as2config-messagesubject)" : {{String}},
  "[PartnerProfileId](#cfn-transfer-connector-as2config-partnerprofileid)" : {{String}},
  "[PreserveContentType](#cfn-transfer-connector-as2config-preservecontenttype)" : {{String}},
  "[SigningAlgorithm](#cfn-transfer-connector-as2config-signingalgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-connector-as2config-syntax.yaml"></a>

```
  [AsyncMdnConfig](#cfn-transfer-connector-as2config-asyncmdnconfig): {{
    ConnectorAsyncMdnConfig}}
  [BasicAuthSecretId](#cfn-transfer-connector-as2config-basicauthsecretid): {{String}}
  [Compression](#cfn-transfer-connector-as2config-compression): {{String}}
  [EncryptionAlgorithm](#cfn-transfer-connector-as2config-encryptionalgorithm): {{String}}
  [LocalProfileId](#cfn-transfer-connector-as2config-localprofileid): {{String}}
  [MdnResponse](#cfn-transfer-connector-as2config-mdnresponse): {{String}}
  [MdnSigningAlgorithm](#cfn-transfer-connector-as2config-mdnsigningalgorithm): {{String}}
  [MessageSubject](#cfn-transfer-connector-as2config-messagesubject): {{String}}
  [PartnerProfileId](#cfn-transfer-connector-as2config-partnerprofileid): {{String}}
  [PreserveContentType](#cfn-transfer-connector-as2config-preservecontenttype): {{String}}
  [SigningAlgorithm](#cfn-transfer-connector-as2config-signingalgorithm): {{String}}
```

## Properties
<a name="aws-properties-transfer-connector-as2config-properties"></a>

`AsyncMdnConfig`  <a name="cfn-transfer-connector-as2config-asyncmdnconfig"></a>
Configuration settings for asynchronous Message Disposition Notification (MDN) responses. This allows you to configure where asynchronous MDN responses should be sent and which servers should handle them.
*Required*: No
*Type*: [ConnectorAsyncMdnConfig](aws-properties-transfer-connector-connectorasyncmdnconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthSecretId`  <a name="cfn-transfer-connector-as2config-basicauthsecretid"></a>
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
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Compression`  <a name="cfn-transfer-connector-as2config-compression"></a>
Specifies whether the AS2 file is compressed.
*Required*: No
*Type*: String
*Allowed values*: `ZLIB | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionAlgorithm`  <a name="cfn-transfer-connector-as2config-encryptionalgorithm"></a>
The algorithm that is used to encrypt the file.
Note the following:
+ Do not use the `DES_EDE3_CBC` algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm.
+ You can only specify `NONE` if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.
*Required*: No
*Type*: String
*Allowed values*: `AES128_CBC | AES192_CBC | AES256_CBC | NONE | DES_EDE3_CBC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalProfileId`  <a name="cfn-transfer-connector-as2config-localprofileid"></a>
A unique identifier for the AS2 local profile.
*Required*: No
*Type*: String
*Pattern*: `^p-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MdnResponse`  <a name="cfn-transfer-connector-as2config-mdnresponse"></a>
Used for outbound requests (from an AWS Transfer Family connector to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous. Specify either of the following values:
+ `ASYNC`: The system expects an asynchronous MDN response, confirming that the file was transferred successfully (or not).
+ `SYNC`: The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not).
+ `NONE`: Specifies that no MDN response is required.
*Required*: No
*Type*: String
*Allowed values*: `SYNC | ASYNC | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MdnSigningAlgorithm`  <a name="cfn-transfer-connector-as2config-mdnsigningalgorithm"></a>
The signing algorithm for the MDN response.
If set to DEFAULT (or not set at all), the value for `SigningAlgorithm` is used.
*Required*: No
*Type*: String
*Allowed values*: `SHA256 | SHA384 | SHA512 | SHA1 | NONE | DEFAULT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageSubject`  <a name="cfn-transfer-connector-as2config-messagesubject"></a>
Used as the `Subject` HTTP header attribute in AS2 messages that are being sent with the connector.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\u007E\t]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartnerProfileId`  <a name="cfn-transfer-connector-as2config-partnerprofileid"></a>
A unique identifier for the partner profile for the connector.
*Required*: No
*Type*: String
*Pattern*: `^p-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreserveContentType`  <a name="cfn-transfer-connector-as2config-preservecontenttype"></a>
Allows you to use the Amazon S3 `Content-Type` that is associated with objects in S3 instead of having the content type mapped based on the file extension. This parameter is enabled by default when you create an AS2 connector from the console, but disabled by default when you create an AS2 connector by calling the API directly.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SigningAlgorithm`  <a name="cfn-transfer-connector-as2config-signingalgorithm"></a>
The algorithm that is used to sign the AS2 messages sent with the connector.
*Required*: No
*Type*: String
*Allowed values*: `SHA256 | SHA384 | SHA512 | SHA1 | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
