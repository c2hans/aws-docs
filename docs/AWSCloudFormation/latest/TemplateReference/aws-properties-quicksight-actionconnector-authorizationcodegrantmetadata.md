---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector AuthorizationCodeGrantMetadata
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata"></a>

Metadata for OAuth 2.0 authorization code grant authentication.

## Syntax
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata-syntax.json"></a>

```
{
  "[AuthorizationCodeGrantCredentialsDetails](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialsdetails)" : {{AuthorizationCodeGrantCredentialsDetails}},
  "[AuthorizationCodeGrantCredentialsSource](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialssource)" : {{String}},
  "[BaseEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-baseendpoint)" : {{String}},
  "[RedirectUrl](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-redirecturl)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata-syntax.yaml"></a>

```
  [AuthorizationCodeGrantCredentialsDetails](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialsdetails): {{
    AuthorizationCodeGrantCredentialsDetails}}
  [AuthorizationCodeGrantCredentialsSource](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialssource): {{String}}
  [BaseEndpoint](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-baseendpoint): {{String}}
  [RedirectUrl](#cfn-quicksight-actionconnector-authorizationcodegrantmetadata-redirecturl): {{String}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata-properties"></a>

`AuthorizationCodeGrantCredentialsDetails`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialsdetails"></a>
The detailed credentials configuration for authorization code grant.
*Required*: No
*Type*: [AuthorizationCodeGrantCredentialsDetails](aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationCodeGrantCredentialsSource`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantmetadata-authorizationcodegrantcredentialssource"></a>
The source of the authorization code grant credentials.
*Required*: No
*Type*: String
*Allowed values*: `PLAIN_CREDENTIALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseEndpoint`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantmetadata-baseendpoint"></a>
The base URL endpoint for the external service.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedirectUrl`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantmetadata-redirecturl"></a>
The redirect URL for the OAuth authorization flow.
*Required*: Yes
*Type*: String
*Pattern*: `^https://.*`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
