---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider CoinbaseCdpConfigurationInput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput"></a>

Coinbase CDP configuration input, containing API credentials used by agents to authenticate with Coinbase's Commerce Developer Platform.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-syntax.json"></a>

```
{
  "[ApiKeyId](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeyid)" : {{String}},
  "[ApiKeySecret](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecret)" : {{String}},
  "[ApiKeySecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretconfig)" : {{SecretReference}},
  "[ApiKeySecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretsource)" : {{String}},
  "[WalletSecret](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecret)" : {{String}},
  "[WalletSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretconfig)" : {{SecretReference}},
  "[WalletSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretsource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-syntax.yaml"></a>

```
  [ApiKeyId](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeyid): {{String}}
  [ApiKeySecret](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecret): {{String}}
  [ApiKeySecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretconfig): {{
    SecretReference}}
  [ApiKeySecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretsource): {{String}}
  [WalletSecret](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecret): {{String}}
  [WalletSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretconfig): {{
    SecretReference}}
  [WalletSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretsource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-properties"></a>

`ApiKeyId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeyid"></a>
The Coinbase CDP API key ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecret`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecret"></a>
The Coinbase CDP API key secret. The value is stored as a secret in AWS Secrets Manager.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the API key secret. This includes the secret ID and the JSON key used to extract the API key secret value from the secret. Required when `apiKeySecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeySecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-apikeysecretsource"></a>
The source type of the API key secret for the Coinbase Developer Platform. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecret`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecret"></a>
The Coinbase CDP wallet secret. The value is stored as a secret in AWS Secrets Manager.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecretConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the wallet secret. This includes the secret ID and the JSON key used to extract the wallet secret value from the secret. Required when `walletSecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WalletSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-coinbasecdpconfigurationinput-walletsecretsource"></a>
The source type of the wallet secret for the Coinbase Developer Platform. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
