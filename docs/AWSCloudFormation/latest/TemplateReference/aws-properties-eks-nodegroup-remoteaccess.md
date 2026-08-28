---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-remoteaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup RemoteAccess
<a name="aws-properties-eks-nodegroup-remoteaccess"></a>

An object representing the remote access configuration for the managed node group.

## Syntax
<a name="aws-properties-eks-nodegroup-remoteaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-remoteaccess-syntax.json"></a>

```
{
  "[Ec2SshKey](#cfn-eks-nodegroup-remoteaccess-ec2sshkey)" : {{String}},
  "[SourceSecurityGroups](#cfn-eks-nodegroup-remoteaccess-sourcesecuritygroups)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-remoteaccess-syntax.yaml"></a>

```
  [Ec2SshKey](#cfn-eks-nodegroup-remoteaccess-ec2sshkey): {{String}}
  [SourceSecurityGroups](#cfn-eks-nodegroup-remoteaccess-sourcesecuritygroups): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-nodegroup-remoteaccess-properties"></a>

`Ec2SshKey`  <a name="cfn-eks-nodegroup-remoteaccess-ec2sshkey"></a>
The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group. For more information, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*. For Windows, an Amazon EC2 SSH key is used to obtain the RDP password. For more information, see [Amazon EC2 key pairs and Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances*.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceSecurityGroups`  <a name="cfn-eks-nodegroup-remoteaccess-sourcesecuritygroups"></a>
The security group IDs that are allowed SSH access (port 22) to the nodes. For Windows, the port is 3389. If you specify an Amazon EC2 SSH key but don't specify a source security group when you create a managed node group, then the port on the nodes is opened to the internet (`0.0.0.0/0`). For more information, see [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon Virtual Private Cloud User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
