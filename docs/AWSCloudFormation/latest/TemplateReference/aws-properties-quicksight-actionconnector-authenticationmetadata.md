---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-authenticationmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector AuthenticationMetadata
<a name="aws-properties-quicksight-actionconnector-authenticationmetadata"></a>

Union type containing authentication metadata for different authentication methods.

## Syntax
<a name="aws-properties-quicksight-actionconnector-authenticationmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-authenticationmetadata-syntax.json"></a>

```
{
  "[ApiKeyConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-apikeyconnectionmetadata)" : {{APIKeyConnectionMetadata}},
  "[AuthorizationCodeGrantMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-authorizationcodegrantmetadata)" : {{AuthorizationCodeGrantMetadata}},
  "[BasicAuthConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-basicauthconnectionmetadata)" : {{BasicAuthConnectionMetadata}},
  "[ClientCredentialsGrantMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-clientcredentialsgrantmetadata)" : {{ClientCredentialsGrantMetadata}},
  "[IamConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-iamconnectionmetadata)" : {{IAMConnectionMetadata}},
  "[NoneConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-noneconnectionmetadata)" : {{NoneConnectionMetadata}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-authenticationmetadata-syntax.yaml"></a>

```
  [ApiKeyConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-apikeyconnectionmetadata): {{
    APIKeyConnectionMetadata}}
  [AuthorizationCodeGrantMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-authorizationcodegrantmetadata): {{
    AuthorizationCodeGrantMetadata}}
  [BasicAuthConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-basicauthconnectionmetadata): {{
    BasicAuthConnectionMetadata}}
  [ClientCredentialsGrantMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-clientcredentialsgrantmetadata): {{
    ClientCredentialsGrantMetadata}}
  [IamConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-iamconnectionmetadata): {{
    IAMConnectionMetadata}}
  [NoneConnectionMetadata](#cfn-quicksight-actionconnector-authenticationmetadata-noneconnectionmetadata): {{
    NoneConnectionMetadata}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-authenticationmetadata-properties"></a>

`ApiKeyConnectionMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-apikeyconnectionmetadata"></a>
API key authentication metadata.
*Required*: No
*Type*: [APIKeyConnectionMetadata](aws-properties-quicksight-actionconnector-apikeyconnectionmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthorizationCodeGrantMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-authorizationcodegrantmetadata"></a>
OAuth 2.0 authorization code grant authentication metadata.
*Required*: No
*Type*: [AuthorizationCodeGrantMetadata](aws-properties-quicksight-actionconnector-authorizationcodegrantmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BasicAuthConnectionMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-basicauthconnectionmetadata"></a>
Basic authentication metadata using username and password.
*Required*: No
*Type*: [BasicAuthConnectionMetadata](aws-properties-quicksight-actionconnector-basicauthconnectionmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientCredentialsGrantMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-clientcredentialsgrantmetadata"></a>
OAuth 2.0 client credentials grant authentication metadata.
*Required*: No
*Type*: [ClientCredentialsGrantMetadata](aws-properties-quicksight-actionconnector-clientcredentialsgrantmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamConnectionMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-iamconnectionmetadata"></a>
IAM role-based authentication metadata for AWS services.
*Required*: No
*Type*: [IAMConnectionMetadata](aws-properties-quicksight-actionconnector-iamconnectionmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoneConnectionMetadata`  <a name="cfn-quicksight-actionconnector-authenticationmetadata-noneconnectionmetadata"></a>
No authentication metadata for services that don't require authentication.
*Required*: No
*Type*: [NoneConnectionMetadata](aws-properties-quicksight-actionconnector-noneconnectionmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
