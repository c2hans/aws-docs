---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile SingularConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using Singular.

## Syntax
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials-syntax.json"></a>

```
{
  "[ApiKey](#cfn-appflow-connectorprofile-singularconnectorprofilecredentials-apikey)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials-syntax.yaml"></a>

```
  [ApiKey](#cfn-appflow-connectorprofile-singularconnectorprofilecredentials-apikey): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials-properties"></a>

`ApiKey`  <a name="cfn-appflow-connectorprofile-singularconnectorprofilecredentials-apikey"></a>
 A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials--seealso"></a>
+ [SingularConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SingularConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
