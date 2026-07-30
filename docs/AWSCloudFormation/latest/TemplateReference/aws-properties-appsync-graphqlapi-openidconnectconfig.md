---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-openidconnectconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi OpenIDConnectConfig
<a name="aws-properties-appsync-graphqlapi-openidconnectconfig"></a>

The `OpenIDConnectConfig` property type specifies the optional authorization configuration for using an OpenID Connect compliant service with your GraphQL endpoint for an AWS AppSync GraphQL API.

`OpenIDConnectConfig` is a property of the [AWS::AppSync::GraphQLApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html) property type.

## Syntax
<a name="aws-properties-appsync-graphqlapi-openidconnectconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-openidconnectconfig-syntax.json"></a>

```
{
  "[AuthTTL](#cfn-appsync-graphqlapi-openidconnectconfig-authttl)" : {{Number}},
  "[ClientId](#cfn-appsync-graphqlapi-openidconnectconfig-clientid)" : {{String}},
  "[IatTTL](#cfn-appsync-graphqlapi-openidconnectconfig-iatttl)" : {{Number}},
  "[Issuer](#cfn-appsync-graphqlapi-openidconnectconfig-issuer)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-openidconnectconfig-syntax.yaml"></a>

```
  [AuthTTL](#cfn-appsync-graphqlapi-openidconnectconfig-authttl): {{Number}}
  [ClientId](#cfn-appsync-graphqlapi-openidconnectconfig-clientid): {{String}}
  [IatTTL](#cfn-appsync-graphqlapi-openidconnectconfig-iatttl): {{Number}}
  [Issuer](#cfn-appsync-graphqlapi-openidconnectconfig-issuer): {{String}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-openidconnectconfig-properties"></a>

`AuthTTL`  <a name="cfn-appsync-graphqlapi-openidconnectconfig-authttl"></a>
The number of milliseconds that a token is valid after being authenticated.
*Required*: No
*Type*: Number
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ClientId`  <a name="cfn-appsync-graphqlapi-openidconnectconfig-clientid"></a>
The client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`IatTTL`  <a name="cfn-appsync-graphqlapi-openidconnectconfig-iatttl"></a>
The number of milliseconds that a token is valid after it's issued to a user.
*Required*: No
*Type*: Number
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Issuer`  <a name="cfn-appsync-graphqlapi-openidconnectconfig-issuer"></a>
The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
