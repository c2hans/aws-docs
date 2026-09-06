---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-oauthclientdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service OAuthClientDetails
<a name="aws-properties-devopsagent-service-oauthclientdetails"></a>

OAuth client credentials shared by Dynatrace and ServiceNow service types.

## Syntax
<a name="aws-properties-devopsagent-service-oauthclientdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-oauthclientdetails-syntax.json"></a>

```
{
  "[ClientId](#cfn-devopsagent-service-oauthclientdetails-clientid)" : {{String}},
  "[ClientName](#cfn-devopsagent-service-oauthclientdetails-clientname)" : {{String}},
  "[ClientSecret](#cfn-devopsagent-service-oauthclientdetails-clientsecret)" : {{String}},
  "[ExchangeParameters](#cfn-devopsagent-service-oauthclientdetails-exchangeparameters)" : {{Json}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-oauthclientdetails-syntax.yaml"></a>

```
  [ClientId](#cfn-devopsagent-service-oauthclientdetails-clientid): {{String}}
  [ClientName](#cfn-devopsagent-service-oauthclientdetails-clientname): {{String}}
  [ClientSecret](#cfn-devopsagent-service-oauthclientdetails-clientsecret): {{String}}
  [ExchangeParameters](#cfn-devopsagent-service-oauthclientdetails-exchangeparameters): {{Json}}
```

## Properties
<a name="aws-properties-devopsagent-service-oauthclientdetails-properties"></a>

`ClientId`  <a name="cfn-devopsagent-service-oauthclientdetails-clientid"></a>
The OAuth client ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientName`  <a name="cfn-devopsagent-service-oauthclientdetails-clientname"></a>
A friendly name for the OAuth client.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-devopsagent-service-oauthclientdetails-clientsecret"></a>
The OAuth client secret.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExchangeParameters`  <a name="cfn-devopsagent-service-oauthclientdetails-exchangeparameters"></a>
Additional parameters for the OAuth token exchange request.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
