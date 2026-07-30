---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider CoinbaseCdpConfigurationOutput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput"></a>

Coinbase CDP configuration output, containing the Coinbase CDP API key ID and the Amazon Resource Names (ARNs) of the secrets that store the API key secret and wallet secret.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-syntax.json"></a>

```
{
  "[ApiKeyId](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeyid)" : {{String}},
  "[ApiKeySecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretarn)" : {{SecretInfo}},
  "[ApiKeySecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretjsonkey)" : {{String}},
  "[ApiKeySecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretsource)" : {{String}},
  "[WalletSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretarn)" : {{SecretInfo}},
  "[WalletSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretjsonkey)" : {{String}},
  "[WalletSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretsource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-syntax.yaml"></a>

```
  [ApiKeyId](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeyid): {{String}}
  [ApiKeySecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretarn): {{
    SecretInfo}}
  [ApiKeySecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretjsonkey): {{String}}
  [ApiKeySecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretsource): {{String}}
  [WalletSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretarn): {{
    SecretInfo}}
  [WalletSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretjsonkey): {{String}}
  [WalletSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretsource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-properties"></a>

`ApiKeyId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeyid"></a>
The Coinbase CDP API key ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretarn"></a>
Information about the secret in AWS Secrets Manager that stores the Coinbase CDP API key secret.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretjsonkey"></a>
The JSON key used to extract the API key secret value from the AWS Secrets Manager secret.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-apikeysecretsource"></a>
The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecretArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretarn"></a>
Information about the secret in AWS Secrets Manager that stores the Coinbase CDP wallet secret.
*Required*: No
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecretJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretjsonkey"></a>
The JSON key used to extract the wallet secret value from the AWS Secrets Manager secret.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationoutput-walletsecretsource"></a>
The source type of the wallet secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
