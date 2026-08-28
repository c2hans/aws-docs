---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-identitypool-cognitoidentityprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::IdentityPool CognitoIdentityProvider
<a name="aws-properties-cognito-identitypool-cognitoidentityprovider"></a>

`CognitoIdentityProvider` is a property of the [AWS::Cognito::IdentityPool](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html) resource that represents an Amazon Cognito user pool and its client ID.

## Syntax
<a name="aws-properties-cognito-identitypool-cognitoidentityprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-identitypool-cognitoidentityprovider-syntax.json"></a>

```
{
  "[ClientId](#cfn-cognito-identitypool-cognitoidentityprovider-clientid)" : {{String}},
  "[ProviderName](#cfn-cognito-identitypool-cognitoidentityprovider-providername)" : {{String}},
  "[ServerSideTokenCheck](#cfn-cognito-identitypool-cognitoidentityprovider-serversidetokencheck)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cognito-identitypool-cognitoidentityprovider-syntax.yaml"></a>

```
  [ClientId](#cfn-cognito-identitypool-cognitoidentityprovider-clientid): {{String}}
  [ProviderName](#cfn-cognito-identitypool-cognitoidentityprovider-providername): {{String}}
  [ServerSideTokenCheck](#cfn-cognito-identitypool-cognitoidentityprovider-serversidetokencheck): {{Boolean}}
```

## Properties
<a name="aws-properties-cognito-identitypool-cognitoidentityprovider-properties"></a>

`ClientId`  <a name="cfn-cognito-identitypool-cognitoidentityprovider-clientid"></a>
The client ID for the Amazon Cognito user pool.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderName`  <a name="cfn-cognito-identitypool-cognitoidentityprovider-providername"></a>
The provider name for an Amazon Cognito user pool. For example: `cognito-idp.us-east-2.amazonaws.com/us-east-2_123456789`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideTokenCheck`  <a name="cfn-cognito-identitypool-cognitoidentityprovider-serversidetokencheck"></a>
TRUE if server-side token validation is enabled for the identity provider’s token.
After you set the `ServerSideTokenCheck` to TRUE for an identity pool, that identity pool checks with the integrated user pools to make sure the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.
If the user is signed out or deleted, the identity pool returns a 400 Not Authorized error.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
