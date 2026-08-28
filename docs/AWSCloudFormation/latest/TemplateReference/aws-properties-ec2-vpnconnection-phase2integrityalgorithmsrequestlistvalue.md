---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPNConnection Phase2IntegrityAlgorithmsRequestListValue
<a name="aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue"></a>

Specifies the integrity algorithm for the VPN tunnel for phase 2 IKE negotiations.

## Syntax
<a name="aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-syntax.json"></a>

```
{
  "[Value](#cfn-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-syntax.yaml"></a>

```
  [Value](#cfn-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-properties"></a>

`Value`  <a name="cfn-ec2-vpnconnection-phase2integrityalgorithmsrequestlistvalue-value"></a>
The integrity algorithm.
*Required*: No
*Type*: String
*Allowed values*: `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
