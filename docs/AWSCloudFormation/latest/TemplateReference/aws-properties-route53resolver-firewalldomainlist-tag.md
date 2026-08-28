---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-firewalldomainlist-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallDomainList Tag
<a name="aws-properties-route53resolver-firewalldomainlist-tag"></a>

One tag that you want to add to the specified resource. A tag consists of a `Key` (a name for the tag) and a `Value`.

## Syntax
<a name="aws-properties-route53resolver-firewalldomainlist-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-firewalldomainlist-tag-syntax.json"></a>

```
{
  "[Key](#cfn-route53resolver-firewalldomainlist-tag-key)" : {{String}},
  "[Value](#cfn-route53resolver-firewalldomainlist-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-firewalldomainlist-tag-syntax.yaml"></a>

```
  [Key](#cfn-route53resolver-firewalldomainlist-tag-key): {{String}}
  [Value](#cfn-route53resolver-firewalldomainlist-tag-value): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-firewalldomainlist-tag-properties"></a>

`Key`  <a name="cfn-route53resolver-firewalldomainlist-tag-key"></a>
The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of `Key` might be `account-id`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-route53resolver-firewalldomainlist-tag-value"></a>
The value for the tag. For example, if `Key` is `account-id`, then `Value` might be the ID of the customer account that you're creating the resource for.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
