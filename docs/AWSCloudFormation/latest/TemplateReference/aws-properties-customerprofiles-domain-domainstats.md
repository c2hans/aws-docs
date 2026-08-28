---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-domainstats.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain DomainStats
<a name="aws-properties-customerprofiles-domain-domainstats"></a>

Usage-specific statistics about the domain.

## Syntax
<a name="aws-properties-customerprofiles-domain-domainstats-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-domainstats-syntax.json"></a>

```
{
  "[MeteringProfileCount](#cfn-customerprofiles-domain-domainstats-meteringprofilecount)" : {{Number}},
  "[ObjectCount](#cfn-customerprofiles-domain-domainstats-objectcount)" : {{Number}},
  "[ProfileCount](#cfn-customerprofiles-domain-domainstats-profilecount)" : {{Number}},
  "[TotalSize](#cfn-customerprofiles-domain-domainstats-totalsize)" : {{Number}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-domainstats-syntax.yaml"></a>

```
  [MeteringProfileCount](#cfn-customerprofiles-domain-domainstats-meteringprofilecount): {{Number}}
  [ObjectCount](#cfn-customerprofiles-domain-domainstats-objectcount): {{Number}}
  [ProfileCount](#cfn-customerprofiles-domain-domainstats-profilecount): {{Number}}
  [TotalSize](#cfn-customerprofiles-domain-domainstats-totalsize): {{Number}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-domainstats-properties"></a>

`MeteringProfileCount`  <a name="cfn-customerprofiles-domain-domainstats-meteringprofilecount"></a>
The number of profiles that you are currently paying for in the domain. If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectCount`  <a name="cfn-customerprofiles-domain-domainstats-objectcount"></a>
The total number of objects in domain.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileCount`  <a name="cfn-customerprofiles-domain-domainstats-profilecount"></a>
The total number of profiles currently in the domain.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalSize`  <a name="cfn-customerprofiles-domain-domainstats-totalsize"></a>
The total size, in bytes, of all objects in the domain.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
