---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-connectionalias-connectionaliasassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::ConnectionAlias ConnectionAliasAssociation
<a name="aws-properties-workspaces-connectionalias-connectionaliasassociation"></a>

Describes a connection alias association that is used for cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Syntax
<a name="aws-properties-workspaces-connectionalias-connectionaliasassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-connectionalias-connectionaliasassociation-syntax.json"></a>

```
{
  "[AssociatedAccountId](#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid)" : {{String}},
  "[AssociationStatus](#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus)" : {{String}},
  "[ConnectionIdentifier](#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier)" : {{String}},
  "[ResourceId](#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-connectionalias-connectionaliasassociation-syntax.yaml"></a>

```
  [AssociatedAccountId](#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid): {{String}}
  [AssociationStatus](#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus): {{String}}
  [ConnectionIdentifier](#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier): {{String}}
  [ResourceId](#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid): {{String}}
```

## Properties
<a name="aws-properties-workspaces-connectionalias-connectionaliasassociation-properties"></a>

`AssociatedAccountId`  <a name="cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid"></a>
The identifier of the AWS account that associated the connection alias with a directory.
*Required*: No
*Type*: String
*Pattern*: `^\d{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssociationStatus`  <a name="cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus"></a>
The association status of the connection alias.
*Required*: No
*Type*: String
*Allowed values*: `NOT_ASSOCIATED | PENDING_ASSOCIATION | ASSOCIATED_WITH_OWNER_ACCOUNT | ASSOCIATED_WITH_SHARED_ACCOUNT | PENDING_DISASSOCIATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionIdentifier`  <a name="cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier"></a>
The identifier of the connection alias association. You use the connection identifier in the DNS TXT record when you're configuring your DNS routing policies.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-workspaces-connectionalias-connectionaliasassociation-resourceid"></a>
The identifier of the directory associated with a connection alias.
*Required*: No
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
