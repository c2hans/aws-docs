---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-connection-authorizationcodeproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Connection AuthorizationCodeProperties
<a name="aws-properties-glue-connection-authorizationcodeproperties"></a>

The set of properties required for the the OAuth2 `AUTHORIZATION_CODE` grant type workflow.

## Syntax
<a name="aws-properties-glue-connection-authorizationcodeproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-connection-authorizationcodeproperties-syntax.json"></a>

```
{
  "[AuthorizationCode](#cfn-glue-connection-authorizationcodeproperties-authorizationcode)" : {{String}},
  "[RedirectUri](#cfn-glue-connection-authorizationcodeproperties-redirecturi)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-connection-authorizationcodeproperties-syntax.yaml"></a>

```
  [AuthorizationCode](#cfn-glue-connection-authorizationcodeproperties-authorizationcode): {{String}}
  [RedirectUri](#cfn-glue-connection-authorizationcodeproperties-redirecturi): {{String}}
```

## Properties
<a name="aws-properties-glue-connection-authorizationcodeproperties-properties"></a>

`AuthorizationCode`  <a name="cfn-glue-connection-authorizationcodeproperties-authorizationcode"></a>
An authorization code to be used in the third leg of the `AUTHORIZATION_CODE` grant workflow. This is a single-use code which becomes invalid once exchanged for an access token, thus it is acceptable to have this value as a request parameter.
*Required*: No
*Type*: String
*Pattern*: `\S+`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RedirectUri`  <a name="cfn-glue-connection-authorizationcodeproperties-redirecturi"></a>
The redirect URI where the user gets redirected to by authorization server when issuing an authorization code. The URI is subsequently used when the authorization code is exchanged for an access token.
*Required*: No
*Type*: String
*Pattern*: `^(https?):\/\/[^\s/$.?#].[^\s]*$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
