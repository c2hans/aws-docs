---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector ClientCredentialsGrantDetails
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails"></a>

Configuration details for OAuth2 client credentials grant flow, including client ID, client secret, token endpoint, and optional scopes.

## Syntax
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails-syntax.json"></a>

```
{
  "[ClientId](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientid)" : {{String}},
  "[ClientSecret](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientsecret)" : {{String}},
  "[TokenEndpoint](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-tokenendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails-syntax.yaml"></a>

```
  [ClientId](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientid): {{String}}
  [ClientSecret](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientsecret): {{String}}
  [TokenEndpoint](#cfn-quicksight-actionconnector-clientcredentialsgrantdetails-tokenendpoint): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails-properties"></a>

`ClientId`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientid"></a>
The client identifier issued to the client during the registration process with the authorization server.
*Required*: Yes
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSecret`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantdetails-clientsecret"></a>
The client secret issued to the client during the registration process with the authorization server.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenEndpoint`  <a name="cfn-quicksight-actionconnector-clientcredentialsgrantdetails-tokenendpoint"></a>
The authorization server endpoint used to obtain access tokens via the client credentials grant flow.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
