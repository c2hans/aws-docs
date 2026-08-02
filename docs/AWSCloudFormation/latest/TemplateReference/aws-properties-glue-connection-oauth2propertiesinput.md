---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-oauth2propertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection OAuth2PropertiesInput
<a name="aws-properties-glue-connection-oauth2propertiesinput"></a>

A structure containing properties for OAuth2 in the CreateConnection request.

## Syntax
<a name="aws-properties-glue-connection-oauth2propertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-oauth2propertiesinput-syntax.json"></a>

```
{
  "[AuthorizationCodeProperties](#cfn-glue-connection-oauth2propertiesinput-authorizationcodeproperties)" : {{AuthorizationCodeProperties}},
  "[OAuth2ClientApplication](#cfn-glue-connection-oauth2propertiesinput-oauth2clientapplication)" : {{OAuth2ClientApplication}},
  "[OAuth2Credentials](#cfn-glue-connection-oauth2propertiesinput-oauth2credentials)" : {{OAuth2Credentials}},
  "[OAuth2GrantType](#cfn-glue-connection-oauth2propertiesinput-oauth2granttype)" : {{String}},
  "[TokenUrl](#cfn-glue-connection-oauth2propertiesinput-tokenurl)" : {{String}},
  "[TokenUrlParametersMap](#cfn-glue-connection-oauth2propertiesinput-tokenurlparametersmap)" : {{Json}}
}
```

### YAML
<a name="aws-properties-glue-connection-oauth2propertiesinput-syntax.yaml"></a>

```
  [AuthorizationCodeProperties](#cfn-glue-connection-oauth2propertiesinput-authorizationcodeproperties): {{
    AuthorizationCodeProperties}}
  [OAuth2ClientApplication](#cfn-glue-connection-oauth2propertiesinput-oauth2clientapplication): {{
    OAuth2ClientApplication}}
  [OAuth2Credentials](#cfn-glue-connection-oauth2propertiesinput-oauth2credentials): {{
    OAuth2Credentials}}
  [OAuth2GrantType](#cfn-glue-connection-oauth2propertiesinput-oauth2granttype): {{String}}
  [TokenUrl](#cfn-glue-connection-oauth2propertiesinput-tokenurl): {{String}}
  [TokenUrlParametersMap](#cfn-glue-connection-oauth2propertiesinput-tokenurlparametersmap): {{Json}}
```

## Properties
<a name="aws-properties-glue-connection-oauth2propertiesinput-properties"></a>

`AuthorizationCodeProperties`  <a name="cfn-glue-connection-oauth2propertiesinput-authorizationcodeproperties"></a>
The set of properties required for the the OAuth2 `AUTHORIZATION_CODE` grant type.
*Required*: No
*Type*: [AuthorizationCodeProperties](aws-properties-glue-connection-authorizationcodeproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2ClientApplication`  <a name="cfn-glue-connection-oauth2propertiesinput-oauth2clientapplication"></a>
The client application type in the CreateConnection request. For example, `AWS_MANAGED` or `USER_MANAGED`.
*Required*: No
*Type*: [OAuth2ClientApplication](aws-properties-glue-connection-oauth2clientapplication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2Credentials`  <a name="cfn-glue-connection-oauth2propertiesinput-oauth2credentials"></a>
The credentials used when the authentication type is OAuth2 authentication.
*Required*: No
*Type*: [OAuth2Credentials](aws-properties-glue-connection-oauth2credentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OAuth2GrantType`  <a name="cfn-glue-connection-oauth2propertiesinput-oauth2granttype"></a>
The OAuth2 grant type in the CreateConnection request. For example, `AUTHORIZATION_CODE`, `JWT_BEARER`, or `CLIENT_CREDENTIALS`.
*Required*: No
*Type*: String
*Allowed values*: `AUTHORIZATION_CODE | CLIENT_CREDENTIALS | JWT_BEARER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrl`  <a name="cfn-glue-connection-oauth2propertiesinput-tokenurl"></a>
The URL of the provider's authentication server, to exchange an authorization code for an access token.
*Required*: No
*Type*: String
*Pattern*: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrlParametersMap`  <a name="cfn-glue-connection-oauth2propertiesinput-tokenurlparametersmap"></a>
A map of parameters that are added to the token `GET` request.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
