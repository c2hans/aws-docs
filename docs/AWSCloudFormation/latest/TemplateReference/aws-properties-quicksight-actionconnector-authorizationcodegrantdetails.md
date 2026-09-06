---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-authorizationcodegrantdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector AuthorizationCodeGrantDetails
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantdetails"></a>

Configuration details for OAuth 2.0 authorization code grant flow.

## Syntax
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantdetails-syntax.json"></a>

```
{
  "[AuthorizationEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-authorizationendpoint)" : {{String}},
  "[ClientId](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientid)" : {{String}},
  "[ClientSecret](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientsecret)" : {{String}},
  "[TokenEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-tokenendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantdetails-syntax.yaml"></a>

```
  [AuthorizationEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-authorizationendpoint): {{String}}
  [ClientId](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientid): {{String}}
  [ClientSecret](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientsecret): {{String}}
  [TokenEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantdetails-tokenendpoint): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantdetails-properties"></a>

`AuthorizationEndpoint`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantdetails-authorizationendpoint"></a>
The authorization endpoint URL for the OAuth flow.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientid"></a>
The client ID for the OAuth application.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantdetails-clientsecret"></a>
The client secret for the OAuth application.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantdetails-tokenendpoint"></a>
The token endpoint URL for obtaining access tokens.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
