---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-workteam-oidcmemberdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workteam OidcMemberDefinition
<a name="aws-properties-sagemaker-workteam-oidcmemberdefinition"></a>

A list of user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of `Groups`, you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.

## Syntax
<a name="aws-properties-sagemaker-workteam-oidcmemberdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-workteam-oidcmemberdefinition-syntax.json"></a>

```
{
  "[OidcGroups](#cfn-sagemaker-workteam-oidcmemberdefinition-oidcgroups)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-workteam-oidcmemberdefinition-syntax.yaml"></a>

```
  [OidcGroups](#cfn-sagemaker-workteam-oidcmemberdefinition-oidcgroups): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-workteam-oidcmemberdefinition-properties"></a>

`OidcGroups`  <a name="cfn-sagemaker-workteam-oidcmemberdefinition-oidcgroups"></a>
A list of OpenID Connect (OIDC) groups for the work team member definition.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `63 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
