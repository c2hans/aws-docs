---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-imagebuilder-domainjoininfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::ImageBuilder DomainJoinInfo
<a name="aws-properties-appstream-imagebuilder-domainjoininfo"></a>

The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.

## Syntax
<a name="aws-properties-appstream-imagebuilder-domainjoininfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-imagebuilder-domainjoininfo-syntax.json"></a>

```
{
  "[DirectoryName](#cfn-appstream-imagebuilder-domainjoininfo-directoryname)" : {{String}},
  "[OrganizationalUnitDistinguishedName](#cfn-appstream-imagebuilder-domainjoininfo-organizationalunitdistinguishedname)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-imagebuilder-domainjoininfo-syntax.yaml"></a>

```
  [DirectoryName](#cfn-appstream-imagebuilder-domainjoininfo-directoryname): {{String}}
  [OrganizationalUnitDistinguishedName](#cfn-appstream-imagebuilder-domainjoininfo-organizationalunitdistinguishedname): {{String}}
```

## Properties
<a name="aws-properties-appstream-imagebuilder-domainjoininfo-properties"></a>

`DirectoryName`  <a name="cfn-appstream-imagebuilder-domainjoininfo-directoryname"></a>
The fully qualified name of the directory (for example, corp.example.com).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OrganizationalUnitDistinguishedName`  <a name="cfn-appstream-imagebuilder-domainjoininfo-organizationalunitdistinguishedname"></a>
The distinguished name of the organizational unit for computer accounts.
*Required*: No
*Type*: String
*Maximum*: `2000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
