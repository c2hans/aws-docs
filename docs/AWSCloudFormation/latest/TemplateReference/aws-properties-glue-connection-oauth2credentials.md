---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-oauth2credentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection OAuth2Credentials
<a name="aws-properties-glue-connection-oauth2credentials"></a>

The credentials used when the authentication type is OAuth2 authentication.

## Syntax
<a name="aws-properties-glue-connection-oauth2credentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-oauth2credentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-glue-connection-oauth2credentials-accesstoken)" : {{String}},
  "[JwtToken](#cfn-glue-connection-oauth2credentials-jwttoken)" : {{String}},
  "[RefreshToken](#cfn-glue-connection-oauth2credentials-refreshtoken)" : {{String}},
  "[UserManagedClientApplicationClientSecret](#cfn-glue-connection-oauth2credentials-usermanagedclientapplicationclientsecret)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-oauth2credentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-glue-connection-oauth2credentials-accesstoken): {{String}}
  [JwtToken](#cfn-glue-connection-oauth2credentials-jwttoken): {{String}}
  [RefreshToken](#cfn-glue-connection-oauth2credentials-refreshtoken): {{String}}
  [UserManagedClientApplicationClientSecret](#cfn-glue-connection-oauth2credentials-usermanagedclientapplicationclientsecret): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-oauth2credentials-properties"></a>

`AccessToken`  <a name="cfn-glue-connection-oauth2credentials-accesstoken"></a>
The access token used when the authentication type is OAuth2.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwtToken`  <a name="cfn-glue-connection-oauth2credentials-jwttoken"></a>
The JSON Web Token (JWT) used when the authentication type is OAuth2.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-glue-connection-oauth2credentials-refreshtoken"></a>
The refresh token used when the authentication type is OAuth2.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserManagedClientApplicationClientSecret`  <a name="cfn-glue-connection-oauth2credentials-usermanagedclientapplicationclientsecret"></a>
The client application client secret if the client application is user managed.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
