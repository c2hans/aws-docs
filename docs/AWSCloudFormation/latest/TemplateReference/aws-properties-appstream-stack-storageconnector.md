---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-storageconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack StorageConnector
<a name="aws-properties-appstream-stack-storageconnector"></a>

A connector that enables persistent storage for users.

## Syntax
<a name="aws-properties-appstream-stack-storageconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-storageconnector-syntax.json"></a>

```
{
  "[ConnectorType](#cfn-appstream-stack-storageconnector-connectortype)" : {{String}},
  "[Domains](#cfn-appstream-stack-storageconnector-domains)" : {{[ String, ... ]}},
  "[ResourceIdentifier](#cfn-appstream-stack-storageconnector-resourceidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-storageconnector-syntax.yaml"></a>

```
  [ConnectorType](#cfn-appstream-stack-storageconnector-connectortype): {{String}}
  [Domains](#cfn-appstream-stack-storageconnector-domains): {{
    - String}}
  [ResourceIdentifier](#cfn-appstream-stack-storageconnector-resourceidentifier): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-storageconnector-properties"></a>

`ConnectorType`  <a name="cfn-appstream-stack-storageconnector-connectortype"></a>
The type of storage connector.
*Required*: Yes
*Type*: String
*Allowed values*: `HOMEFOLDERS | GOOGLE_DRIVE | ONE_DRIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domains`  <a name="cfn-appstream-stack-storageconnector-domains"></a>
The names of the domains for the account.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-appstream-stack-storageconnector-resourceidentifier"></a>
The ARN of the storage connector.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
