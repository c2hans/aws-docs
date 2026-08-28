---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-glueoauth2credentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection GlueOAuth2Credentials
<a name="aws-properties-datazone-connection-glueoauth2credentials"></a>

The GlueOAuth2 credentials of a connection.

## Syntax
<a name="aws-properties-datazone-connection-glueoauth2credentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-glueoauth2credentials-syntax.json"></a>

```
{
  "[AccessToken](#cfn-datazone-connection-glueoauth2credentials-accesstoken)" : {{String}},
  "[JwtToken](#cfn-datazone-connection-glueoauth2credentials-jwttoken)" : {{String}},
  "[RefreshToken](#cfn-datazone-connection-glueoauth2credentials-refreshtoken)" : {{String}},
  "[UserManagedClientApplicationClientSecret](#cfn-datazone-connection-glueoauth2credentials-usermanagedclientapplicationclientsecret)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-glueoauth2credentials-syntax.yaml"></a>

```
  [AccessToken](#cfn-datazone-connection-glueoauth2credentials-accesstoken): {{String}}
  [JwtToken](#cfn-datazone-connection-glueoauth2credentials-jwttoken): {{String}}
  [RefreshToken](#cfn-datazone-connection-glueoauth2credentials-refreshtoken): {{String}}
  [UserManagedClientApplicationClientSecret](#cfn-datazone-connection-glueoauth2credentials-usermanagedclientapplicationclientsecret): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-glueoauth2credentials-properties"></a>

`AccessToken`  <a name="cfn-datazone-connection-glueoauth2credentials-accesstoken"></a>
The access token of a connection.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JwtToken`  <a name="cfn-datazone-connection-glueoauth2credentials-jwttoken"></a>
The jwt token of the connection.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)$`
*Maximum*: `8000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshToken`  <a name="cfn-datazone-connection-glueoauth2credentials-refreshtoken"></a>
The refresh token of the connection.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserManagedClientApplicationClientSecret`  <a name="cfn-datazone-connection-glueoauth2credentials-usermanagedclientapplicationclientsecret"></a>
The user managed client application client secret of the connection.
*Required*: No
*Type*: String
*Pattern*: `^[\x20-\x7E]*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
