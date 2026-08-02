---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Cluster API server endpoint
<a name="cluster-endpoint"></a>

This topic helps you to enable private access for your Amazon EKS cluster’s Kubernetes API server endpoint and limit, or completely disable, public access from the internet.

When you create a new cluster, Amazon EKS creates an endpoint for the managed Kubernetes API server that you use to communicate with your cluster (using Kubernetes management tools such as `kubectl`). By default, this API server endpoint is public to the internet, and access to the API server is secured using a combination of AWS Identity and Access Management (IAM) and native Kubernetes [Role Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (RBAC). This endpoint is known as the *cluster public endpoint*. Also there is a *cluster private endpoint*. For more information about the cluster private endpoint, see the following section [Cluster private endpoint](#cluster-endpoint-private).

## `IPv6` cluster endpoint format
<a name="cluster-endpoint-ipv6"></a>

EKS creates a unique dual-stack endpoint in the following format for new `IPv6` clusters that are made after October 2024. An *IPv6 cluster* is a cluster that you select `IPv6` in the IP family (`ipFamily`) setting of the cluster.

**Example**
EKS cluster public/private endpoint: `eks-cluster.{{region}}.api.aws`
EKS cluster public/private endpoint: `eks-cluster.{{region}}.api.aws`
EKS cluster public/private endpoint: `eks-cluster.{{region}}.api.amazonwebservices.com.cn`

**Note**
The dual-stack cluster endpoint was introduced in October 2024. For more information about `IPv6` clusters, see [Learn about IPv6 addresses to clusters, Pods, and services](cni-ipv6.md). Clusters made before October 2024 use the following endpoint format instead.

## `IPv4` cluster endpoint format
<a name="cluster-endpoint-ipv4"></a>

EKS creates a unique endpoint in the following format for each cluster that selects `IPv4` in the IP family (ipFamily) setting of the cluster:

**Example**
EKS cluster public/private endpoint `eks-cluster.{{region}}.eks.amazonaws.com`
EKS cluster public/private endpoint `eks-cluster.{{region}}.eks.amazonaws.com`
EKS cluster public/private endpoint `eks-cluster.{{region}}.amazonwebservices.com.cn`

**Note**
Before October 2024, `IPv6` clusters used this endpoint format also. For those clusters, both the public endpoint and the private endpoint have only `IPv4` addresses resolve from this endpoint.

## Cluster private endpoint
<a name="cluster-endpoint-private"></a>

You can enable private access to the Kubernetes API server so that all communication between your nodes and the API server stays within your VPC. You can limit the IP addresses that can access your API server from the internet, or completely disable internet access to the API server.

**Note**
Because this endpoint is for the Kubernetes API server and not a traditional AWS PrivateLink endpoint for communicating with an AWS API, it doesn’t appear as an endpoint in the Amazon VPC console.

When you enable endpoint private access for your cluster, Amazon EKS creates a Route 53 private hosted zone on your behalf and associates it with your cluster’s VPC. This private hosted zone is managed by Amazon EKS, and it doesn’t appear in your account’s Route 53 resources. In order for the private hosted zone to properly route traffic to your API server, your VPC must have `enableDnsHostnames` and `enableDnsSupport` set to `true`, and the DHCP options set for your VPC must include `AmazonProvidedDNS` in its domain name servers list. For more information, see [Updating DNS support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-updating) in the *Amazon VPC User Guide*.

You can define your API server endpoint access requirements when you create a new cluster, and you can update the API server endpoint access for a cluster at any time.

**Note**
The endpoint access controls who can reach the Kubernetes API server. If you also want to manage how egress traffic from the control plane reaches resources in your VPC (such as webhook servers and OIDC providers), see [Configuring control plane egress routing](control-plane-egress.md).

## Modifying cluster endpoint access
<a name="modify-endpoint-access"></a>

Use the procedures in this section to modify the endpoint access for an existing cluster. The following table shows the supported API server endpoint access combinations and their associated behavior.

| Endpoint public access | Endpoint private access | Behavior |
| --- | --- | --- |
| Enabled | Disabled |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html)  |
| Enabled | Enabled |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html)  |
| Disabled | Enabled |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html)  |

 **Endpoint access controls**

Note that each of the following methods to control endpoint access only affect the respective endpoint.

 *Cluster security group*
The cluster security group controls two types of connections: connections to the *kubelet API* and the private endpoint. The connections to the `kubelet` API are used in the `kubectl attach`, `kubectl cp`, `kubectl exec`, `kubectl logs`, and `kubectl port-forward` commands. The cluster security group doesn’t affect the public endpoint.

 *Public access CIDRs*
The *public access CIDRs* control access to the public endpoint by a list of CIDR blocks. Note that the public access CIDRs don’t affect the private endpoint. The public access CIDRs behave differently on the `IPv6` clusters and `IPv4` clusters depending on the date they were created, which the following describes:

 **CIDR blocks in the public endpoint (`IPv6` cluster)**

You can add `IPv6` and `IPv4` CIDR blocks to the public endpoint of an `IPv6` cluster, because the public endpoint is dual-stack. This only applies to new clusters with the `ipFamily` set to `IPv6` that you made in October 2024 or later. You can identify these clusters by the new endpoint domain name `api.aws`.

 **CIDR blocks in the public endpoint (`IPv4` cluster)**

You can add `IPv4` CIDR blocks to the public endpoint of an `IPv4` cluster. You can’t add `IPv6` CIDR blocks to the public endpoint of an `IPv4` cluster. If you try, EKS returns the following error message: `The following CIDRs are invalid in publicAccessCidrs`

 **CIDR blocks in the public endpoint (`IPv6` cluster made before October 2024)**

You can add `IPv4` CIDR blocks to the public endpoint of the old `IPv6` clusters that you made before October 2024. You can identify these clusters by the `eks.amazonaws.com` endpoint. You can’t add `IPv6` CIDR blocks to the public endpoint of these old `IPv6` clusters that you made before October 2024. If you try, EKS returns the following error message: `The following CIDRs are invalid in publicAccessCidrs`

## Accessing a private only API server
<a name="private-access"></a>

If you have disabled public access for your cluster’s Kubernetes API server endpoint, you can only access the API server from within your VPC or a [connected network](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html). Here are a few possible ways to access the Kubernetes API server endpoint:

 **Connected network**
Connect your network to the VPC with an [AWS transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) or other [connectivity](https://docs.aws.amazon.com/aws-technical-content/latest/aws-vpc-connectivity-options/introduction.html) option and then use a computer in the connected network. You must ensure that your Amazon EKS control plane security group contains rules to allow ingress traffic on port 443 from your connected network.

 **Amazon EC2 bastion host**
You can launch an Amazon EC2 instance into a public subnet in your cluster’s VPC and then log in via SSH into that instance to run `kubectl` commands. For more information, see [Linux bastion hosts on AWS](https://aws.amazon.com/quickstart/architecture/linux-bastion/). You must ensure that your Amazon EKS control plane security group contains rules to allow ingress traffic on port 443 from your bastion host. For more information, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md).
When you configure `kubectl` for your bastion host, be sure to use AWS credentials that are already mapped to your cluster’s RBAC configuration, or add the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-principal) that your bastion will use to the RBAC configuration before you remove endpoint public access. For more information, see [Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md) and [Unauthorized or access denied (`kubectl`)](troubleshooting.md#unauthorized).

 ** AWS Cloud9 IDE**
 AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. You can create an AWS Cloud9 IDE in your cluster’s VPC and use the IDE to communicate with your cluster. For more information, see [Creating an environment in AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html). You must ensure that your Amazon EKS control plane security group contains rules to allow ingress traffic on port 443 from your IDE security group. For more information, see [View Amazon EKS security group requirements for clusters](sec-group-reqs.md).
When you configure `kubectl` for your AWS Cloud9 IDE, be sure to use AWS credentials that are already mapped to your cluster’s RBAC configuration, or add the IAM principal that your IDE will use to the RBAC configuration before you remove endpoint public access. For more information, see [Grant IAM users and roles access to Kubernetes APIs](grant-k8s-access.md) and [Unauthorized or access denied (`kubectl`)](troubleshooting.md#unauthorized).

 ** AWS CloudShell**
Choose **Connect** on the cluster details page in the Amazon EKS console. For private clusters, CloudShell launches a VPC environment that can reach your cluster’s private API server endpoint. For more information, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](create-kubeconfig.md).

📝 [Edit this page on GitHub](https://github.com/search?q=repo%3Aawsdocs%2Famazon-eks-user-guide+%5B%23cluster-endpoint%5D&type=code)
