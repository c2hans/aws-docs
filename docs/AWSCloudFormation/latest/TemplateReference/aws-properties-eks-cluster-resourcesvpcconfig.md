---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-resourcesvpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster ResourcesVpcConfig
<a name="aws-properties-eks-cluster-resourcesvpcconfig"></a>

An object representing the VPC configuration to use for an Amazon EKS cluster.

**Important**
When updating a resource, you must include these properties if the previous CloudFormation template of the resource had them:
 `EndpointPublicAccess`
 `EndpointPrivateAccess`
 `PublicAccessCidrs`

## Syntax
<a name="aws-properties-eks-cluster-resourcesvpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-resourcesvpcconfig-syntax.json"></a>

```
{
  "[ControlPlaneEgressMode](#cfn-eks-cluster-resourcesvpcconfig-controlplaneegressmode)" : {{String}},
  "[EndpointPrivateAccess](#cfn-eks-cluster-resourcesvpcconfig-endpointprivateaccess)" : {{Boolean}},
  "[EndpointPublicAccess](#cfn-eks-cluster-resourcesvpcconfig-endpointpublicaccess)" : {{Boolean}},
  "[PublicAccessCidrs](#cfn-eks-cluster-resourcesvpcconfig-publicaccesscidrs)" : {{[ String, ... ]}},
  "[SecurityGroupIds](#cfn-eks-cluster-resourcesvpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-eks-cluster-resourcesvpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-eks-cluster-resourcesvpcconfig-syntax.yaml"></a>

```
  [ControlPlaneEgressMode](#cfn-eks-cluster-resourcesvpcconfig-controlplaneegressmode): {{String}}
  [EndpointPrivateAccess](#cfn-eks-cluster-resourcesvpcconfig-endpointprivateaccess): {{Boolean}}
  [EndpointPublicAccess](#cfn-eks-cluster-resourcesvpcconfig-endpointpublicaccess): {{Boolean}}
  [PublicAccessCidrs](#cfn-eks-cluster-resourcesvpcconfig-publicaccesscidrs): {{
    - String}}
  [SecurityGroupIds](#cfn-eks-cluster-resourcesvpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-eks-cluster-resourcesvpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-eks-cluster-resourcesvpcconfig-properties"></a>

`ControlPlaneEgressMode`  <a name="cfn-eks-cluster-resourcesvpcconfig-controlplaneegressmode"></a>
Specifies the control plane egress routing mode for the cluster. If the cluster is set to `AWS_MANAGED`, Amazon EKS manages the egress path from the control plane and you don't need to configure NAT gateways or other routing infrastructure for control plane traffic. If the cluster is set to `CUSTOMER_ROUTED`, you manage the egress path from the control plane in your VPC subnets. You are responsible for ensuring that the control plane can reach required endpoints such as webhook servers and OIDC providers. The default value is `AWS_MANAGED`. Once set to `CUSTOMER_ROUTED`, this setting cannot be changed back to `AWS_MANAGED` on the same cluster.
 [Learn more about control plane egress routing in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-egress.html)
*Required*: No
*Type*: String
*Allowed values*: `AWS_MANAGED | CUSTOMER_ROUTED | CUSTOMER_ISOLATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointPrivateAccess`  <a name="cfn-eks-cluster-resourcesvpcconfig-endpointprivateaccess"></a>
Set this value to `true` to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is `false`, which disables private access for your Kubernetes API server. If you disable private access and you have nodes or AWS Fargate pods in the cluster, then ensure that `publicAccessCidrs` includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointPublicAccess`  <a name="cfn-eks-cluster-resourcesvpcconfig-endpointpublicaccess"></a>
Set this value to `false` to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is `true`, which enables public access for your Kubernetes API server. The endpoint domain name and IP address family depends on the value of the `ipFamily` for the cluster. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicAccessCidrs`  <a name="cfn-eks-cluster-resourcesvpcconfig-publicaccesscidrs"></a>
The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is `0.0.0.0/0` and additionally `::/0` for dual-stack `IPv6` clusters. If you've disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and AWS Fargate`Pod` in the cluster. For more information, see [Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.
Note that the public endpoints are dual-stack for only `IPv6` clusters that are made after October 2024. You can't add `IPv6` CIDR blocks to `IPv4` clusters or `IPv6` clusters that were made before October 2024.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-eks-cluster-resourcesvpcconfig-securitygroupids"></a>
Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use that allow communication between your nodes and the Kubernetes control plane. If you don't specify any security groups, then familiarize yourself with the difference between Amazon EKS defaults for clusters deployed with Kubernetes. For more information, see [Amazon EKS security group considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the * *Amazon EKS User Guide* *.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-eks-cluster-resourcesvpcconfig-subnetids"></a>
Specify subnets for your Amazon EKS nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your nodes and the Kubernetes control plane.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
