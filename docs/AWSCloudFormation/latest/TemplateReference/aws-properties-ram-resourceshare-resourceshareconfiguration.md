---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ram-resourceshare-resourceshareconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::ResourceShare ResourceShareConfiguration
<a name="aws-properties-ram-resourceshare-resourceshareconfiguration"></a>

The configuration of the resource share

## Syntax
<a name="aws-properties-ram-resourceshare-resourceshareconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ram-resourceshare-resourceshareconfiguration-syntax.json"></a>

```
{
  "[ExclusiveAccountAccess](#cfn-ram-resourceshare-resourceshareconfiguration-exclusiveaccountaccess)" : {{Boolean}},
  "[RetainSharingOnAccountLeaveOrganization](#cfn-ram-resourceshare-resourceshareconfiguration-retainsharingonaccountleaveorganization)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ram-resourceshare-resourceshareconfiguration-syntax.yaml"></a>

```
  [ExclusiveAccountAccess](#cfn-ram-resourceshare-resourceshareconfiguration-exclusiveaccountaccess): {{Boolean}}
  [RetainSharingOnAccountLeaveOrganization](#cfn-ram-resourceshare-resourceshareconfiguration-retainsharingonaccountleaveorganization): {{Boolean}}
```

## Properties
<a name="aws-properties-ram-resourceshare-resourceshareconfiguration-properties"></a>

`ExclusiveAccountAccess`  <a name="cfn-ram-resourceshare-resourceshareconfiguration-exclusiveaccountaccess"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetainSharingOnAccountLeaveOrganization`  <a name="cfn-ram-resourceshare-resourceshareconfiguration-retainsharingonaccountleaveorganization"></a>
Specifies whether the consumer account retains access to the resource share after leaving the organization.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
