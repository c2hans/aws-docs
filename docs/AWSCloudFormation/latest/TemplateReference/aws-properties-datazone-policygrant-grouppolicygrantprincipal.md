---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-grouppolicygrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant GroupPolicyGrantPrincipal
<a name="aws-properties-datazone-policygrant-grouppolicygrantprincipal"></a>

The group principal to whom the policy is granted.

## Syntax
<a name="aws-properties-datazone-policygrant-grouppolicygrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-grouppolicygrantprincipal-syntax.json"></a>

```
{
  "[GroupIdentifier](#cfn-datazone-policygrant-grouppolicygrantprincipal-groupidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-grouppolicygrantprincipal-syntax.yaml"></a>

```
  [GroupIdentifier](#cfn-datazone-policygrant-grouppolicygrantprincipal-groupidentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-grouppolicygrantprincipal-properties"></a>

`GroupIdentifier`  <a name="cfn-datazone-policygrant-grouppolicygrantprincipal-groupidentifier"></a>
The ID Of the group of the group principal.
*Required*: Yes
*Type*: String
*Pattern*: `(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+)`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
