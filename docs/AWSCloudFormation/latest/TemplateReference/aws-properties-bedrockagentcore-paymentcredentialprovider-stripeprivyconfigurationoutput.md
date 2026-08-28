---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentCredentialProvider StripePrivyConfigurationOutput
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput"></a>

<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-description"></a>The `StripePrivyConfigurationOutput` property type specifies Property description not available. for an [AWS::BedrockAgentCore::PaymentCredentialProvider](aws-resource-bedrockagentcore-paymentcredentialprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-syntax.json"></a>

```
{
  "[AppId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appid)" : {{String}},
  "[AppSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretarn)" : {{SecretInfo}},
  "[AppSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretjsonkey)" : {{String}},
  "[AppSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretsource)" : {{String}},
  "[AuthorizationId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationid)" : {{String}},
  "[AuthorizationPrivateKeyArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyarn)" : {{SecretInfo}},
  "[AuthorizationPrivateKeyJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyjsonkey)" : {{String}},
  "[AuthorizationPrivateKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-syntax.yaml"></a>

```
  [AppId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appid): {{String}}
  [AppSecretArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretarn): {{
    SecretInfo}}
  [AppSecretJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretjsonkey): {{String}}
  [AppSecretSource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretsource): {{String}}
  [AuthorizationId](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationid): {{String}}
  [AuthorizationPrivateKeyArn](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyarn): {{
    SecretInfo}}
  [AuthorizationPrivateKeyJsonKey](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyjsonkey): {{String}}
  [AuthorizationPrivateKeySource](#cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeysource): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-properties"></a>

`AppId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appid"></a>
The app ID provided by Privy.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecretArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretarn"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecretJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretjsonkey"></a>
The JSON key used to extract the app secret value from the AWS Secrets Manager secret.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppSecretSource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-appsecretsource"></a>
The source type of the app secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationId`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationid"></a>
The authorization ID for the Stripe Privy integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKeyArn`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyarn"></a>
Property description not available.
*Required*: Yes
*Type*: [SecretInfo](aws-properties-bedrockagentcore-paymentcredentialprovider-secretinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKeyJsonKey`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeyjsonkey"></a>
The JSON key used to extract the authorization private key value from the AWS Secrets Manager secret.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationPrivateKeySource`  <a name="cfn-bedrockagentcore-paymentcredentialprovider-stripeprivyconfigurationoutput-authorizationprivatekeysource"></a>
The source type of the authorization private key. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in AWS Secrets Manager.
*Required*: No
*Type*: String
*Allowed values*: `MANAGED | EXTERNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
