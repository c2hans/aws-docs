---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53RecoveryReadiness::ResourceSet R53ResourceRecord
<a name="aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord"></a>

The Amazon Route 53 resource that a DNS target resource record points to.

## Syntax
<a name="aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord-syntax.json"></a>

```
{
  "[DomainName](#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname)" : {{String}},
  "[RecordSetId](#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord-syntax.yaml"></a>

```
  [DomainName](#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname): {{String}}
  [RecordSetId](#cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid): {{String}}
```

## Properties
<a name="aws-properties-route53recoveryreadiness-resourceset-r53resourcerecord-properties"></a>

`DomainName`  <a name="cfn-route53recoveryreadiness-resourceset-r53resourcerecord-domainname"></a>
The DNS target domain name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordSetId`  <a name="cfn-route53recoveryreadiness-resourceset-r53resourcerecord-recordsetid"></a>
The Amazon Route 53 Resource Record Set ID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
