---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin OAuth2ClientCredentialConfiguration
<a name="aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration"></a>

Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

## Syntax
<a name="aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration-syntax.json"></a>

```
{
  "[AuthorizationUrl](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-authorizationurl)" : {{String}},
  "[RoleArn](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-rolearn)" : {{String}},
  "[SecretArn](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-secretarn)" : {{String}},
  "[TokenUrl](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-tokenurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration-syntax.yaml"></a>

```
  [AuthorizationUrl](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-authorizationurl): {{String}}
  [RoleArn](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-rolearn): {{String}}
  [SecretArn](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-secretarn): {{String}}
  [TokenUrl](#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-tokenurl): {{String}}
```

## Properties
<a name="aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration-properties"></a>

`AuthorizationUrl`  <a name="cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-authorizationurl"></a>
The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.
*Required*: No
*Type*: String
*Pattern*: `^(https?|ftp|file)://([^\s]*)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-rolearn"></a>
The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-secretarn"></a>
The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}$`
*Minimum*: `0`
*Maximum*: `1284`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TokenUrl`  <a name="cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-tokenurl"></a>
The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.
*Required*: No
*Type*: String
*Pattern*: `^(https?|ftp|file)://([^\s]*)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
