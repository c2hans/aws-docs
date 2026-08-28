---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-networkaclcommonpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy NetworkAclCommonPolicy
<a name="aws-properties-fms-policy-networkaclcommonpolicy"></a>

Defines a Firewall Manager network ACL policy. This is used in the `PolicyOption` of a `SecurityServicePolicyData` for a `Policy`, when the `SecurityServicePolicyData` type is set to `NETWORK_ACL_COMMON`.

For information about network ACLs, see [Control traffic to subnets using network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon Virtual Private Cloud User Guide*.

## Syntax
<a name="aws-properties-fms-policy-networkaclcommonpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-networkaclcommonpolicy-syntax.json"></a>

```
{
  "[NetworkAclEntrySet](#cfn-fms-policy-networkaclcommonpolicy-networkaclentryset)" : {{NetworkAclEntrySet}}
}
```

### YAML
<a name="aws-properties-fms-policy-networkaclcommonpolicy-syntax.yaml"></a>

```
  [NetworkAclEntrySet](#cfn-fms-policy-networkaclcommonpolicy-networkaclentryset): {{
    NetworkAclEntrySet}}
```

## Properties
<a name="aws-properties-fms-policy-networkaclcommonpolicy-properties"></a>

`NetworkAclEntrySet`  <a name="cfn-fms-policy-networkaclcommonpolicy-networkaclentryset"></a>
The definition of the first and last rules for the network ACL policy.
*Required*: Yes
*Type*: [NetworkAclEntrySet](aws-properties-fms-policy-networkaclentryset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
