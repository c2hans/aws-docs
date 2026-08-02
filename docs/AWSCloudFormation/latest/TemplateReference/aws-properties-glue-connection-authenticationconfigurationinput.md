---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-authenticationconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection AuthenticationConfigurationInput
<a name="aws-properties-glue-connection-authenticationconfigurationinput"></a>

A structure containing the authentication configuration in the CreateConnection request.

## Syntax
<a name="aws-properties-glue-connection-authenticationconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-authenticationconfigurationinput-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-glue-connection-authenticationconfigurationinput-authenticationtype)" : {{String}},
  "[BasicAuthenticationCredentials](#cfn-glue-connection-authenticationconfigurationinput-basicauthenticationcredentials)" : {{BasicAuthenticationCredentials}},
  "[CustomAuthenticationCredentials](#cfn-glue-connection-authenticationconfigurationinput-customauthenticationcredentials)" : {{Json}},
  "[KmsKeyArn](#cfn-glue-connection-authenticationconfigurationinput-kmskeyarn)" : {{String}},
  "[OAuth2Properties](#cfn-glue-connection-authenticationconfigurationinput-oauth2properties)" : {{OAuth2PropertiesInput}},
  "[SecretArn](#cfn-glue-connection-authenticationconfigurationinput-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-authenticationconfigurationinput-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-glue-connection-authenticationconfigurationinput-authenticationtype): {{String}}
  [BasicAuthenticationCredentials](#cfn-glue-connection-authenticationconfigurationinput-basicauthenticationcredentials): {{
    BasicAuthenticationCredentials}}
  [CustomAuthenticationCredentials](#cfn-glue-connection-authenticationconfigurationinput-customauthenticationcredentials): {{Json}}
  [KmsKeyArn](#cfn-glue-connection-authenticationconfigurationinput-kmskeyarn): {{String}}
  [OAuth2Properties](#cfn-glue-connection-authenticationconfigurationinput-oauth2properties): {{
    OAuth2PropertiesInput}}
  [SecretArn](#cfn-glue-connection-authenticationconfigurationinput-secretarn): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-authenticationconfigurationinput-properties"></a>

`AuthenticationType`  <a name="cfn-glue-connection-authenticationconfigurationinput-authenticationtype"></a>
A structure containing the authentication configuration in the CreateConnection request.
*Required*: Yes
*Type*: String
*Allowed values*: `BASIC | OAUTH2 | CUSTOM | IAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthenticationCredentials`  <a name="cfn-glue-connection-authenticationconfigurationinput-basicauthenticationcredentials"></a>
The credentials used when the authentication type is basic authentication.
*Required*: No
*Type*: [BasicAuthenticationCredentials](aws-properties-glue-connection-basicauthenticationcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAuthenticationCredentials`  <a name="cfn-glue-connection-authenticationconfigurationinput-customauthenticationcredentials"></a>
The credentials used when the authentication type is custom authentication.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-glue-connection-authenticationconfigurationinput-kmskeyarn"></a>
The ARN of the KMS key used to encrypt the connection. Only taken an as input in the request and stored in the Secret Manager.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[a-z0-9-]*:kms:.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Properties`  <a name="cfn-glue-connection-authenticationconfigurationinput-oauth2properties"></a>
The properties for OAuth2 authentication in the CreateConnection request.
*Required*: No
*Type*: [OAuth2PropertiesInput](aws-properties-glue-connection-oauth2propertiesinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-glue-connection-authenticationconfigurationinput-secretarn"></a>
The secret manager ARN to store credentials in the CreateConnection request.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
