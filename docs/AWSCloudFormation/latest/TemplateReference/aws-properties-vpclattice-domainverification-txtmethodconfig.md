---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-domainverification-txtmethodconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::DomainVerification TxtMethodConfig
<a name="aws-properties-vpclattice-domainverification-txtmethodconfig"></a>

Configuration for TXT record-based domain verification method.

## Syntax
<a name="aws-properties-vpclattice-domainverification-txtmethodconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-domainverification-txtmethodconfig-syntax.json"></a>

```
{
  "[name](#cfn-vpclattice-domainverification-txtmethodconfig-name)" : {{String}},
  "[value](#cfn-vpclattice-domainverification-txtmethodconfig-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-domainverification-txtmethodconfig-syntax.yaml"></a>

```
  [name](#cfn-vpclattice-domainverification-txtmethodconfig-name): {{String}}
  [value](#cfn-vpclattice-domainverification-txtmethodconfig-value): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-domainverification-txtmethodconfig-properties"></a>

`name`  <a name="cfn-vpclattice-domainverification-txtmethodconfig-name"></a>
The name of the TXT record that must be created for domain verification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`value`  <a name="cfn-vpclattice-domainverification-txtmethodconfig-value"></a>
The value that must be added to the TXT record for domain verification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
