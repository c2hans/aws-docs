---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-oauth2clientapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection OAuth2ClientApplication
<a name="aws-properties-datazone-connection-oauth2clientapplication"></a>

The OAuth2Client application.

## Syntax
<a name="aws-properties-datazone-connection-oauth2clientapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-oauth2clientapplication-syntax.json"></a>

```
{
  "[AWSManagedClientApplicationReference](#cfn-datazone-connection-oauth2clientapplication-awsmanagedclientapplicationreference)" : {{String}},
  "[UserManagedClientApplicationClientId](#cfn-datazone-connection-oauth2clientapplication-usermanagedclientapplicationclientid)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-connection-oauth2clientapplication-syntax.yaml"></a>

```
  [AWSManagedClientApplicationReference](#cfn-datazone-connection-oauth2clientapplication-awsmanagedclientapplicationreference): {{String}}
  [UserManagedClientApplicationClientId](#cfn-datazone-connection-oauth2clientapplication-usermanagedclientapplicationclientid): {{String}}
```

## Properties
<a name="aws-properties-datazone-connection-oauth2clientapplication-properties"></a>

`AWSManagedClientApplicationReference`  <a name="cfn-datazone-connection-oauth2clientapplication-awsmanagedclientapplicationreference"></a>
The AWS managed client application reference in the OAuth2Client application.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserManagedClientApplicationClientId`  <a name="cfn-datazone-connection-oauth2clientapplication-usermanagedclientapplicationclientid"></a>
The user managed client application client ID in the OAuth2Client application.
*Required*: No
*Type*: String
*Pattern*: `^\S+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
