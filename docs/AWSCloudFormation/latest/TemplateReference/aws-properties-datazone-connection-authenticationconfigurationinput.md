---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-authenticationconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection AuthenticationConfigurationInput
<a name="aws-properties-datazone-connection-authenticationconfigurationinput"></a>

The authentication configuration of a connection.

## Syntax
<a name="aws-properties-datazone-connection-authenticationconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-authenticationconfigurationinput-syntax.json"></a>

```
{
  "[AuthenticationType](#cfn-datazone-connection-authenticationconfigurationinput-authenticationtype)" : {{String}},
  "[BasicAuthenticationCredentials](#cfn-datazone-connection-authenticationconfigurationinput-basicauthenticationcredentials)" : {{BasicAuthenticationCredentials}},
  "[CustomAuthenticationCredentials](#cfn-datazone-connection-authenticationconfigurationinput-customauthenticationcredentials)" : {{{{{Key}}: {{Value}}, ...}}},
  "[KmsKeyArn](#cfn-datazone-connection-authenticationconfigurationinput-kmskeyarn)" : {{String}},
  "[OAuth2Properties](#cfn-datazone-connection-authenticationconfigurationinput-oauth2properties)" : {{OAuth2Properties}},
  "[SecretArn](#cfn-datazone-connection-authenticationconfigurationinput-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-authenticationconfigurationinput-syntax.yaml"></a>

```
  [AuthenticationType](#cfn-datazone-connection-authenticationconfigurationinput-authenticationtype): {{String}}
  [BasicAuthenticationCredentials](#cfn-datazone-connection-authenticationconfigurationinput-basicauthenticationcredentials): {{
    BasicAuthenticationCredentials}}
  [CustomAuthenticationCredentials](#cfn-datazone-connection-authenticationconfigurationinput-customauthenticationcredentials): {{
    {{Key}}: {{Value}}}}
  [KmsKeyArn](#cfn-datazone-connection-authenticationconfigurationinput-kmskeyarn): {{String}}
  [OAuth2Properties](#cfn-datazone-connection-authenticationconfigurationinput-oauth2properties): {{
    OAuth2Properties}}
  [SecretArn](#cfn-datazone-connection-authenticationconfigurationinput-secretarn): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-authenticationconfigurationinput-properties"></a>

`AuthenticationType`  <a name="cfn-datazone-connection-authenticationconfigurationinput-authenticationtype"></a>
The authentication type of a connection.
*Required*: No
*Type*: String
*Allowed values*: `BASIC | OAUTH2 | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthenticationCredentials`  <a name="cfn-datazone-connection-authenticationconfigurationinput-basicauthenticationcredentials"></a>
The basic authentication credentials of a connection.
*Required*: No
*Type*: [BasicAuthenticationCredentials](aws-properties-datazone-connection-basicauthenticationcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAuthenticationCredentials`  <a name="cfn-datazone-connection-authenticationconfigurationinput-customauthenticationcredentials"></a>
The custom authentication credentials of a connection.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-datazone-connection-authenticationconfigurationinput-kmskeyarn"></a>
The KMS key ARN of a connection.
*Required*: No
*Type*: String
*Pattern*: `^$|arn:aws[a-z0-9-]*:kms:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Properties`  <a name="cfn-datazone-connection-authenticationconfigurationinput-oauth2properties"></a>
The oAuth2 properties of a connection.
*Required*: No
*Type*: [OAuth2Properties](aws-properties-datazone-connection-oauth2properties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-datazone-connection-authenticationconfigurationinput-secretarn"></a>
The secret ARN of a connection.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
