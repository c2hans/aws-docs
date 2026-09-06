---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider StripePrivyConfigurationInput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput"></a>

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-description"></a>The `StripePrivyConfigurationInput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-syntax.json"></a>

```
{
  "[AppId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appid)" : {{String}},
  "[AppSecret](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecret)" : {{String}},
  "[AppSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretconfig)" : {{SecretReference}},
  "[AppSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretsource)" : {{String}},
  "[AuthorizationId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationid)" : {{String}},
  "[AuthorizationPrivateKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekey)" : {{String}},
  "[AuthorizationPrivateKeyConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeyconfig)" : {{SecretReference}},
  "[AuthorizationPrivateKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-syntax.yaml"></a>

```
  [AppId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appid): {{String}}
  [AppSecret](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecret): {{String}}
  [AppSecretConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretconfig): {{
    SecretReference}}
  [AppSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretsource): {{String}}
  [AuthorizationId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationid): {{String}}
  [AuthorizationPrivateKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekey): {{String}}
  [AuthorizationPrivateKeyConfig](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeyconfig): {{
    SecretReference}}
  [AuthorizationPrivateKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeysource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-properties"></a>

`AppId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appid"></a>
The app ID provided by Privy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecret`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecret"></a>
The app secret provided by Privy.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecretConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretconfig"></a>
A reference to the AWS Secrets Manager secret that stores the app secret. This includes the secret ID and the JSON key used to extract the app secret value from the secret. Required when `appSecretSource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-appsecretsource"></a>
The source type of the app secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationid"></a>
The authorization ID for the Stripe Privy integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekey"></a>
The authorization private key for the Stripe Privy integration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKeyConfig`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeyconfig"></a>
A reference to the AWS Secrets Manager secret that stores the authorization private key. This includes the secret ID and the JSON key used to extract the authorization private key value from the secret. Required when `authorizationPrivateKeySource` is set to `EXTERNAL`.
*Required*: No
*Type*: [SecretReference](aws-properties-bedrockagentcore-paymentcredentialprovider-secretreference.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKeySource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationinput-authorizationprivatekeysource"></a>
The source type of the authorization private key. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
