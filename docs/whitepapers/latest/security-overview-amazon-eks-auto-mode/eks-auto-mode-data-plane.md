---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/eks-auto-mode-data-plane.html
---

# EKS Auto Mode data plane
<a name="eks-auto-mode-data-plane"></a>

The EKS Auto Mode data plane consists primarily of the Auto Mode nodes, the compute that your workloads run directly on. The data plane is built to give you full flexibility and control with respect to the types of workloads that can be run and the instances that they run on while still delegating operational responsibility for the scaling and health of that data plane to AWS.

## EC2 managed instances
<a name="ec2-managed-instances"></a>

EKS Auto Mode uses [EC2 managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html) to provide the compute that backs an Auto Mode node. These nodes have built-in IAM-enforced restrictions that block operations on the EC2 instances that could compromise the ability of AWS to operate the nodes. For example, it's not possible to change the instance profile of a node or attach or detach ENIs. Instead, the instance role is controlled using the [NodeClass](https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html) and ENI management is performed by a networking capability that is managed by AWS and hosted on AWS infrastructure. These restrictions are applied regardless of the IAM identity and its permissions. Even the AWS account root user is unable to circumvent these constraints.

The IAM-enforced restrictions extend past the EC2 instance itself. It also includes the Amazon EBS volumes that are attached to the instance at launch, ENIs, and the launch templates used for launching those managed instances.

EC2 managed instances does not provide Amazon EKS additional permissions to EKS Auto Mode nodes. The permissions that Amazon EKS uses to manage those instances are still granted only by the cluster service role and EKS SLR.

By building on top of EC2 managed instances, the EC2 features that customers are familiar with work as expected. With EKS Auto Mode, customers can continue to use capacity reservations and savings plans. Auto Mode allows full control over the instance types that are launched, providing access to the broad range of EC2 instance types including accelerated types for machine learning inferencing and training use cases.

## Instance configuration
<a name="instance-configuration"></a>

EKS Auto Mode enforces a few best practices related to security during instance launch. Because the instances are EC2 managed instances, they cannot be changed at runtime. This includes the configuration for [Instance Metadata Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) (IMDS) and encryption of the root and data Amazon EBS volumes.

IMDS is configured to use IMDSv2 (token required) with a hop limit of one, which is the maximum number of hops that the metadata token can travel. This blocks non-host-network Pods from accessing IMDS, through which it could access the node's IAM credentials.

On EKS Auto Mode nodes, the root and data Amazon EBS volumes are encrypted and configured to be deleted upon termination of the instance. Optionally the NodeClass `ephemeralStorage.kmsKeyID` setting can be used to specify the encryption key to be used.

## Node role and access entry
<a name="node-role-and-access-entry"></a>

[EKS access entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) is the recommended mechanism to grant an IAM principal access to the Kubernetes API. Each access entry has a type, Kubernetes username, and list of Kubernetes groups. Depending on the access entry type, the username and groups might not be configurable. Some access entry types can optionally have an association created with [access policies](https://docs.aws.amazon.com/eks/latest/userguide/access-policy-permissions.html). These access policies provide further permissions to the IAM principal, beyond what might be granted based on the Kubernetes username and group.

The standard EKS Auto Mode node access entry is of type `EC2`, which has a Kubernetes username of `system:node:{{SessionName}}` and is in the `system:nodes` group with the `AmazonEKSAutoNodePolicy` access policy attached. When using an EC2 instance profile to assign an IAM role to an EC2 instance, the `SessionName` is automatically set to the instance ID, leading to a Kubernetes username of `system:node:i-1234567890abcdef0` which corresponds to a Kubernetes node name of just the instance ID, `i-1234567890abcdef0`.

The default Amazon EKS Auto Mode IAM role uses a new [AmazonEKSWorkerNodeMinimalPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSWorkerNodeMinimalPolicy.html) policy. This policy removes nine different permissions from the previous [AmazonEKSWorkerNodePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSWorkerNodePolicy.html) , retaining only the permissions required for EKS Auto Mode nodes to operate. The [AmazonEC2ContainerRegistryPullOnly](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerRegistryPullOnly) policy, while generally useful, was also created while building Auto Mode to further reduce the number of Elastic Container Registry (ECR) permissions made available to nodes compared to the existing [AmazonEC2ContainerRegistryReadOnly](https://docs.aws.amazon.com/AmazonECR/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonEC2ContainerRegistryReadOnly) policy. Lastly, Auto Mode nodes use the EC2 instance ID as the Kubernetes node name. Because the instance ID is reliably determined through [IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), the node role no longer needs permissions to call `ec2:DescribeInstances` to discover the private DNS name.

## Node operating system
<a name="node-operating-system"></a>

The operating system for EKS Auto Mode nodes is a custom variant of [Bottlerocket](https://aws.amazon.com/bottlerocket/). Bottlerocket was selected as the underlying operating system for Auto Mode nodes because it is optimized and built specifically for running containers and has several security enhancements over a general-purpose operating system. It enforces cryptographic integrity checks for the root file system and mandatory access controls using SELinux to reduce the attack surface in the event of container escape. The reduced number of packages in Bottlerocket minimizes the surface area for potential security issues and reduces the effort required by many compliance programs to keep hosts updated with the latest security patches.

In Bottlerocket, most non-privileged pods will automatically have their own SELinux multi-category security (MCS) label applied to them. This MCS label is unique to each Pod and is designed to protect against a process in one pod manipulating a process in another Pod or on the host. Even if a labeled Pod runs as root and has access to the host filesystem, it will be unable to manipulate files, make sensitive system calls on the host, or access the container runtime.

The EKS Auto Mode Bottlerocket variant hardens the standard Bottlerocket configuration by disabling features like [host containers](https://bottlerocket.dev/en/os/1.41.x/concepts/host-containers/), which while useful in the standard Bottlerocket distribution are not used in Auto Mode. In addition, remote access services like SSH and the [AWS Systems Manager](https://aws.amazon.com/ssm) agent are not available on Auto Mode nodes. While direct remote access isn't allowed, it is still possible to troubleshoot the node in multiple ways.
+ [NodeDiagnostic resource](https://docs.aws.amazon.com/eks/latest/userguide/auto-get-logs.html) – The NodeDiagnostic custom resource definition (CRD) is a Kubernetes-native method of fetching system logs and information from an EKS Auto Mode node. The collected logs are uploaded automatically to an [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3) bucket. By design, a pre-signed Amazon S3 URL is used, which enables collecting logs from nodes without requiring that S3 permissions be added to the node role. The ability to collect logs is controlled by limiting access to create the NodeDiagnostic object through standard Kubernetes role-based access control (RBAC).
+ [Console output](https://docs.aws.amazon.com/eks/latest/userguide/auto-troubleshoot.html#auto-node-console) logs – Auto Mode periodically writes system information to the Amazon EC2 console, which can be useful for debugging issues related to permissions or network configuration issues that stop the node from joining the cluster.
+ [Debug containers](https://docs.aws.amazon.com/eks/latest/userguide/auto-troubleshoot.html#auto-node-debug-logs) – Because Auto Mode is Kubernetes conformant, standard debug containers can be used to inspect and fetch system logs on the node.

**Note**
EKS Auto Mode nodes are Kubernetes conformant and because of this it's possible to run Pods on Auto Mode nodes that provide an SSH service or run the SSM agent. In this case, the remote access session is to the Pod itself and resides within the container boundary.

The EKS Auto Mode variant of Bottlerocket is built on the core open source Bottlerocket distribution but adds several Auto Mode specific packages to handle things like the OS level configuration of network interfaces that have been attached to the instance by the AWS managed networking component. When launching instance types with Neuron or NVIDIA accelerators, a specific version of the Auto Mode operating system is used that contains the appropriate drivers and Kubernetes device plugins to make these nodes compatible with accelerated workloads without requiring further software installation or configuration.

## Node patching
<a name="node-patching"></a>

Auto Mode nodes are updated by replacing the instance with a new instance running the latest Auto Mode AMI. This process allows workloads to gracefully migrate from the unpatched node to the patched node following Pod Disruption Budgets (PDBs) that govern the workload availability in addition to the disruption controls configured at the NodePool level.

The Auto Mode AMIs undergo a rigorous testing process prior to being released. This includes:
+ Common vulnerabilities and exposures (CVE) scanning of included components
+ Full Kubernetes node conformance tests
+ Component functional testing (for example, validating that pods can obtain IAM credentials through EKS Pod Identity)
+ Security related testing (for example, testing that the node has only the expected services listening)
+ Functional testing of compatibility with both Neuron and NVIDIA accelerators

Auto Mode AMIs are rolled out using standard AWS best practices for [safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/). These deployments are built around an internal AWS construct called a *pipeline*, which automates the build and deployment process and provides automated alarm monitoring, testing, and other validation of safety. The process begins by deploying the newly built and tested AMI to a small subset of EKS Auto Mode clusters in a single Region, with a bake time to detect potential issues. As confidence in the AMI stability grows, it is gradually rolled out to more clusters in larger waves and across more Regions, while reducing the bake time between deployments. There is additional gating included in the deployment pipeline so that by default a new AMI is made available no more than once per week.

The default EKS Auto Mode NodePools allow nodes to be replaced through *drift* after a new AMI has been made available for their EKS cluster. Customers optionally can create their own NodePool disruption windows to control when and how quickly nodes are updated.

The [built-in](https://docs.aws.amazon.com/eks/latest/userguide/set-builtin-node-pools.html) EKS Auto Mode NodePools have a configured node expiration of 14 days, but customers can create their own NodePools to raise or lower this value. To receive patches as soon as they are made available, NodePools should not use the `disruption.budgets[].schedule` setting, which restricts the time windows that a node can be replaced.

If PDBs or NodePool disruption controls do not allow a node to be replaced before the 21-day maximum node lifetime has been reached, the node will be disrupted regardless. This helps make sure that nodes periodically receive security patches and updates, and that a misconfigured PDB or other failing workload can't indefinitely stop a node from being replaced.

## Compute
<a name="compute"></a>

When using EKS Auto Mode, the AWS managed compute capability is responsible for the auto-scaling of Kubernetes worker nodes. Scaling configuration is performed using the standard [Karpenter](https://karpenter.sh/) concepts of a [NodePool](https://docs.aws.amazon.com/eks/latest/userguide/create-node-pool.html) and [NodeClass](https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html). The NodePool is a standard Karpenter NodePool. The NodeClass is Auto Mode specific, which is the Karpenter mechanism for cloud provider specific extensions.

EKS Auto Mode supports two [built-in](https://docs.aws.amazon.com/eks/latest/userguide/set-builtin-node-pools.html) NodePools, named `system` and `general-purpose` that can optionally be enabled. The `system` NodePool has a `CriticalAddonsOnly` taint and is designed to separate cluster-critical applications from other workloads. The `general-purpose` NodePool has no taints and is designed to run other non-accelerated workloads in your cluster. The built-in NodePools, by virtue of being created and configured using the `eks:CreateCluster` and `eks:UpdateClusterConfig` API calls, allow infrastructure as code (IaC) tooling to create EKS clusters that can run workloads immediately after cluster creation without requiring further interaction with the Kubernetes API to create a NodePool and NodeClass.

## Storage
<a name="storage"></a>

EKS Auto Mode nodes launch with two attached Amazon EBS volumes that share the instance's lifetime. The first is the root volume which contains the Bottlerocket operating system, while the second is the data volume that contains ephemeral data such as Pod logs, container images, and so on. Both volumes are encrypted by default with EKS Auto Mode using an AWS managed key. Optionally, customers can [configure](https://docs.aws.amazon.com/eks/latest/userguide/auto-kms.html) a CMK to be used for encryption of these volumes.

The block storage capability of EKS Auto Mode used for persistent volumes backed by Amazon EBS can [optionally be configured](https://docs.aws.amazon.com/eks/latest/userguide/create-storage-class.html) to encrypt those EBS volumes by default, including with a CMK.

## Networking
<a name="networking"></a>

The managed networking capability of EKS Auto Mode runs on AWS infrastructure and is responsible for two separate activities. First, it handles the lifetime and attachment of ENIs to the managed instance as needed to handle the Pods scheduled to the node. Second, it handles the lifetime and configuration of load balancers that are required to support the `IngressClass` with a controller of type `eks.amazonaws.com/alb`.

The [NodeClass](https://docs.aws.amazon.com/eks/latest/userguide/create-node-class.html) controls the subnets and security groups that are used for Auto Mode nodes and Pods running on those nodes through the `subnetSelectorTerms`, `securityGroupSelectorTerms`, `podSubnetSelectorTerms`, and `podSecurityGroupSelectorTerms`. The `subnetSelectorTerms` and `securityGroupSelectorTerms` settings are required. If only these settings are provided, both the node and Pods will share the same subnets and security groups. The node IP and subsequent Pod IP addresses will be allocated from the primary ENI and additional ENIs will be dynamically created and attached to the node to support Pods as needed.

![Node ENIs connecting to node and pod IPs, with security groups applied to primary and secondary ENIs.](http://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/images/image5.png)

If `podSubnetSelectorTerms` and `podSecurityGroupSelectorTerms` are also configured, then only the node's IP will come from the primary ENI. Pod IPs will come from secondary ENIs and use the specified security groups. This mode of operations allows segregating the node IP addresses from Pod IP addresses, primarily to allow using separate security groups to control traffic flow for nodes and Pods differently. Because the primary ENI is reserved for only the node IP address, when operating in this configuration the result is reduced Pod density on Auto Mode nodes.

After being [enabled](https://docs.aws.amazon.com/eks/latest/userguide/auto-net-pol.html) on the cluster, Pod-to-Pod traffic can be controlled by using standard Kubernetes [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). These policies are enforced by a networking component on the node using [eBPF](https://ebpf.foundation/).

The EKS Auto Mode NodeClass also offers several settings for more advanced networking use cases:
+ `advancedNetworking.httpsProxy` and `advancedNetworking.noProxy` – Controls the `HTTPS_PROXY` and `NO_PROXY` settings for containerd and kubelet.
+ `certificateBundles` – Certificate bundles for custom certificate authorities (CA) to be trusted by the node. This is most often used when pulling container images from a private container registry that uses self-signed certificates.
+ `advancedNetworking.associatePublicIPAddress` – Controls the setting of the `AssociatePublicIpAddress` property on the launch template used for launching EKS Auto Mode nodes. This setting will need to be set to false if SCPs require it to allow Auto Mode to launch EC2 instances.

## Node component Kubernetes RBAC
<a name="node-component-kubernetes-rbac"></a>

Several of the built-in node components require access to the Kubernetes API server to function. For example, the DNS component needs to list services and the node monitoring component needs to access NodeDiagnostic resources to respond to [log collection requests](https://docs.aws.amazon.com/eks/latest/userguide/auto-get-logs.html). This access is provided by the [AmazonEKSAutoNodePolicy](https://docs.aws.amazon.com/eks/latest/userguide/access-policy-permissions.html) access policy.

Instead of providing the union of all permissions to the kubelet RBAC identity through this access policy, a more restrictive approach was taken. The components begin by using the kubelet's identity and then use standard Kubernetes [impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) to assume an identity with only the specific permissions that the component needs. After this identity assumption has occurred, the component only has the new permissions. This will be visible in the Kubernetes audit logs by the addition of an `impersonatedUser` property on the audit event:

```
"impersonatedUser": {
    "username": "eks-auto:component-name",
    "groups": [
        "system:authenticated"
    ]
}
```
