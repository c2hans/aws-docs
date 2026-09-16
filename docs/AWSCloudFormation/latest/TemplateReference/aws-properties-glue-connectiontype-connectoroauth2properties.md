---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connectiontype-connectoroauth2properties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::ConnectionType ConnectorOAuth2Properties
<a name="aws-properties-glue-connectiontype-connectoroauth2properties"></a>

<a name="aws-properties-glue-connectiontype-connectoroauth2properties-description"></a>The `ConnectorOAuth2Properties` property type specifies Property description not available. for an [AWS::Glue::ConnectionType](aws-resource-glue-connectiontype.md).

## Syntax
<a name="aws-properties-glue-connectiontype-connectoroauth2properties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connectiontype-connectoroauth2properties-syntax.json"></a>

```
{
  "[AuthorizationCodeProperties](#cfn-glue-connectiontype-connectoroauth2properties-authorizationcodeproperties)" : {{ConnectorAuthorizationCodeProperties}},
  "[ClientCredentialsProperties](#cfn-glue-connectiontype-connectoroauth2properties-clientcredentialsproperties)" : {{ClientCredentialsProperties}},
  "[JWTBearerProperties](#cfn-glue-connectiontype-connectoroauth2properties-jwtbearerproperties)" : {{JWTBearerProperties}},
  "[OAuth2GrantType](#cfn-glue-connectiontype-connectoroauth2properties-oauth2granttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connectiontype-connectoroauth2properties-syntax.yaml"></a>

```
  [AuthorizationCodeProperties](#cfn-glue-connectiontype-connectoroauth2properties-authorizationcodeproperties): {{
    ConnectorAuthorizationCodeProperties}}
  [ClientCredentialsProperties](#cfn-glue-connectiontype-connectoroauth2properties-clientcredentialsproperties): {{
    ClientCredentialsProperties}}
  [JWTBearerProperties](#cfn-glue-connectiontype-connectoroauth2properties-jwtbearerproperties): {{
    JWTBearerProperties}}
  [OAuth2GrantType](#cfn-glue-connectiontype-connectoroauth2properties-oauth2granttype): {{String}}
```

## Properties
<a name="aws-properties-glue-connectiontype-connectoroauth2properties-properties"></a>

`AuthorizationCodeProperties`  <a name="cfn-glue-connectiontype-connectoroauth2properties-authorizationcodeproperties"></a>
Property description not available.
*Required*: No
*Type*: [ConnectorAuthorizationCodeProperties](aws-properties-glue-connectiontype-connectorauthorizationcodeproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientCredentialsProperties`  <a name="cfn-glue-connectiontype-connectoroauth2properties-clientcredentialsproperties"></a>
Property description not available.
*Required*: No
*Type*: [ClientCredentialsProperties](aws-properties-glue-connectiontype-clientcredentialsproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JWTBearerProperties`  <a name="cfn-glue-connectiontype-connectoroauth2properties-jwtbearerproperties"></a>
Property description not available.
*Required*: No
*Type*: [JWTBearerProperties](aws-properties-glue-connectiontype-jwtbearerproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OAuth2GrantType`  <a name="cfn-glue-connectiontype-connectoroauth2properties-oauth2granttype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CLIENT_CREDENTIALS | JWT_BEARER | AUTHORIZATION_CODE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
