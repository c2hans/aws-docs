---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-remotepodnetwork.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster RemotePodNetwork
<a name="aws-properties-eks-cluster-remotepodnetwork"></a>

A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.

These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).

It must satisfy the following requirements:
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.

## Syntax
<a name="aws-properties-eks-cluster-remotepodnetwork-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-remotepodnetwork-syntax.json"></a>

```
{
  "[Cidrs](#cfn-eks-cluster-remotepodnetwork-cidrs)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-remotepodnetwork-syntax.yaml"></a>

```
  [Cidrs](#cfn-eks-cluster-remotepodnetwork-cidrs): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-cluster-remotepodnetwork-properties"></a>

`Cidrs`  <a name="cfn-eks-cluster-remotepodnetwork-cidrs"></a>
A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.
These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isn't available for on-premises and edge locations.
Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, ` 10.2.0.0/16`).
It must satisfy the following requirements:
+ Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /32, maximum allowed size is /8. Publicly-routable addresses aren't supported.
+ Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
