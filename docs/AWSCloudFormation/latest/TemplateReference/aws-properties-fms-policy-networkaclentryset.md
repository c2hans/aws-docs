---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-networkaclentryset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy NetworkAclEntrySet
<a name="aws-properties-fms-policy-networkaclentryset"></a>

The configuration of the first and last rules for the network ACL policy, and the remediation settings for each.

## Syntax
<a name="aws-properties-fms-policy-networkaclentryset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-networkaclentryset-syntax.json"></a>

```
{
  "[FirstEntries](#cfn-fms-policy-networkaclentryset-firstentries)" : {{[ NetworkAclEntry, ... ]}},
  "[ForceRemediateForFirstEntries](#cfn-fms-policy-networkaclentryset-forceremediateforfirstentries)" : {{Boolean}},
  "[ForceRemediateForLastEntries](#cfn-fms-policy-networkaclentryset-forceremediateforlastentries)" : {{Boolean}},
  "[LastEntries](#cfn-fms-policy-networkaclentryset-lastentries)" : {{[ NetworkAclEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-fms-policy-networkaclentryset-syntax.yaml"></a>

```
  [FirstEntries](#cfn-fms-policy-networkaclentryset-firstentries): {{
    - NetworkAclEntry}}
  [ForceRemediateForFirstEntries](#cfn-fms-policy-networkaclentryset-forceremediateforfirstentries): {{Boolean}}
  [ForceRemediateForLastEntries](#cfn-fms-policy-networkaclentryset-forceremediateforlastentries): {{Boolean}}
  [LastEntries](#cfn-fms-policy-networkaclentryset-lastentries): {{
    - NetworkAclEntry}}
```

## Properties
<a name="aws-properties-fms-policy-networkaclentryset-properties"></a>

`FirstEntries`  <a name="cfn-fms-policy-networkaclentryset-firstentries"></a>
The rules that you want to run first in the Firewall Manager managed network ACLs.
Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.
You must specify at least one first entry or one last entry in any network ACL policy.
*Required*: No
*Type*: Array of [NetworkAclEntry](aws-properties-fms-policy-networkaclentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceRemediateForFirstEntries`  <a name="cfn-fms-policy-networkaclentryset-forceremediateforfirstentries"></a>
Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.
If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the *AWS Firewall Manager Developer Guide*.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceRemediateForLastEntries`  <a name="cfn-fms-policy-networkaclentryset-forceremediateforlastentries"></a>
Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.
If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the *AWS Firewall Manager Developer Guide*.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastEntries`  <a name="cfn-fms-policy-networkaclentryset-lastentries"></a>
The rules that you want to run last in the Firewall Manager managed network ACLs.
Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.
You must specify at least one first entry or one last entry in any network ACL policy.
*Required*: No
*Type*: Array of [NetworkAclEntry](aws-properties-fms-policy-networkaclentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
