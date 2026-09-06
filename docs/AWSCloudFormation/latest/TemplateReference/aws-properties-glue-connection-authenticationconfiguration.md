---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-authenticationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection AuthenticationConfiguration
<a name="aws-properties-glue-connection-authenticationconfiguration"></a>

A structure containing the authentication configuration.

## Syntax
<a name="aws-properties-glue-connection-authenticationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-authenticationconfiguration-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-glue-connection-authenticationconfiguration-authenticationtype)" : {{String}},
  "[BasicAuthenticationCredentials](#cfn-glue-connection-authenticationconfiguration-basicauthenticationcredentials)" : {{BasicAuthenticationCredentials}},
  "[CustomAuthenticationCredentials](#cfn-glue-connection-authenticationconfiguration-customauthenticationcredentials)" : {{Json}},
  "[KmsKeyArn](#cfn-glue-connection-authenticationconfiguration-kmskeyarn)" : {{String}},
  "[OAuth2Properties](#cfn-glue-connection-authenticationconfiguration-oauth2properties)" : {{OAuth2Properties}},
  "[SecretArn](#cfn-glue-connection-authenticationconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-authenticationconfiguration-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-glue-connection-authenticationconfiguration-authenticationtype): {{String}}
  [BasicAuthenticationCredentials](#cfn-glue-connection-authenticationconfiguration-basicauthenticationcredentials): {{
    BasicAuthenticationCredentials}}
  [CustomAuthenticationCredentials](#cfn-glue-connection-authenticationconfiguration-customauthenticationcredentials): {{Json}}
  [KmsKeyArn](#cfn-glue-connection-authenticationconfiguration-kmskeyarn): {{String}}
  [OAuth2Properties](#cfn-glue-connection-authenticationconfiguration-oauth2properties): {{
    OAuth2Properties}}
  [SecretArn](#cfn-glue-connection-authenticationconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-authenticationconfiguration-properties"></a>

`AuthenticationType`  <a name="cfn-glue-connection-authenticationconfiguration-authenticationtype"></a>
A structure containing the authentication configuration.
*Required*: Yes
*Type*: String
*Allowed values*: `BASIC | OAUTH2 | CUSTOM | IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthenticationCredentials`  <a name="cfn-glue-connection-authenticationconfiguration-basicauthenticationcredentials"></a>
Property description not available.
*Required*: No
*Type*: [BasicAuthenticationCredentials](aws-properties-glue-connection-basicauthenticationcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAuthenticationCredentials`  <a name="cfn-glue-connection-authenticationconfiguration-customauthenticationcredentials"></a>
Property description not available.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-glue-connection-authenticationconfiguration-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key used to encrypt sensitive authentication information. This key is used to protect credentials and other sensitive data stored within the authentication configuration.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[a-z0-9-]*:kms:.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Properties`  <a name="cfn-glue-connection-authenticationconfiguration-oauth2properties"></a>
The properties for OAuth2 authentication.
*Required*: No
*Type*: [OAuth2Properties](aws-properties-glue-connection-oauth2properties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-glue-connection-authenticationconfiguration-secretarn"></a>
The secret manager ARN to store credentials.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
