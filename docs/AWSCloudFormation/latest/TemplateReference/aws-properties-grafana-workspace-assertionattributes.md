---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-grafana-workspace-assertionattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Grafana::Workspace AssertionAttributes
<a name="aws-properties-grafana-workspace-assertionattributes"></a>

A structure that defines which attributes in the IdP assertion are to be used to define information about the users authenticated by the IdP to use the workspace.

## Syntax
<a name="aws-properties-grafana-workspace-assertionattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-grafana-workspace-assertionattributes-syntax.json"></a>

```
{
  "[Email](#cfn-grafana-workspace-assertionattributes-email)" : {{String}},
  "[Groups](#cfn-grafana-workspace-assertionattributes-groups)" : {{String}},
  "[Login](#cfn-grafana-workspace-assertionattributes-login)" : {{String}},
  "[Name](#cfn-grafana-workspace-assertionattributes-name)" : {{String}},
  "[Org](#cfn-grafana-workspace-assertionattributes-org)" : {{String}},
  "[Role](#cfn-grafana-workspace-assertionattributes-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-grafana-workspace-assertionattributes-syntax.yaml"></a>

```
  [Email](#cfn-grafana-workspace-assertionattributes-email): {{String}}
  [Groups](#cfn-grafana-workspace-assertionattributes-groups): {{String}}
  [Login](#cfn-grafana-workspace-assertionattributes-login): {{String}}
  [Name](#cfn-grafana-workspace-assertionattributes-name): {{String}}
  [Org](#cfn-grafana-workspace-assertionattributes-org): {{String}}
  [Role](#cfn-grafana-workspace-assertionattributes-role): {{String}}
```

## Properties
<a name="aws-properties-grafana-workspace-assertionattributes-properties"></a>

`Email`  <a name="cfn-grafana-workspace-assertionattributes-email"></a>
The name of the attribute within the SAML assertion to use as the email names for SAML users.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Groups`  <a name="cfn-grafana-workspace-assertionattributes-groups"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for user groups.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Login`  <a name="cfn-grafana-workspace-assertionattributes-login"></a>
The name of the attribute within the SAML assertion to use as the login names for SAML users.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-grafana-workspace-assertionattributes-name"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for SAML users.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Org`  <a name="cfn-grafana-workspace-assertionattributes-org"></a>
The name of the attribute within the SAML assertion to use as the user full "friendly" names for the users' organizations.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-grafana-workspace-assertionattributes-role"></a>
The name of the attribute within the SAML assertion to use as the user roles.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
