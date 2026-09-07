---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/amazon-eks-control-plane.html
---

# Amazon EKS control plane
<a name="amazon-eks-control-plane"></a>

The Kubernetes control plane managed by Amazon EKS runs inside an EKS-managed VPC. This control plane is single tenant, meaning that for each EKS cluster there is a unique EKS managed VPC and Kubernetes control plane. The EKS control plane comprises the Kubernetes API server nodes and [etcd](https://etcd.io/) cluster. Kubernetes API server nodes run components such as the API server, scheduler, and `kube-controller-manager` in an auto-scaling group. EKS runs a minimum of two API server nodes in distinct Availability Zones within an AWS Region. Likewise, for durability, the etcd server nodes also run in an auto-scaling group that spans three Availability Zones. EKS runs a NAT gateway in each Availability Zone, and API servers and etcd servers run in a private subnet. This architecture protects cluster availability so that an event in a single Availability Zone doesn't affect the EKS cluster's availability.

![EKS control plane architecture with API servers and etcd across three Availability Zones.](https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/images/image4.png)

## Kubernetes API data
<a name="kubernetes-api-data"></a>

Amazon EKS provides default envelope encryption for Kubernetes API data in EKS Auto Mode clusters. Envelope encryption protects the data you store with the Kubernetes API server. For example, envelope encryption applies to the configuration of your Kubernetes cluster, such as `ConfigMaps`. Envelope encryption does not apply to data on nodes or [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs) volumes. This envelope encryption extends across Kubernetes API data.

This provides a managed, default experience that implements defense-in-depth for your Kubernetes applications and doesn't require action on your part.

Amazon EKS uses [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) with [Kubernetes KMS provider v2](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/#configuring-the-kms-provider-kms-v2) for this additional layer of security with an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) and the option for you to bring your own [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) (CMK) from AWS KMS.

## EKS Auto Mode capabilities
<a name="eks-auto-mode-capabilities"></a>

When EKS Auto Mode is enabled for a cluster, an additional set of control plane capabilities are also enabled. In a standard Amazon EKS cluster, the components that perform auto-scaling, manage [Elastic Network Interfaces (ENIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) and Amazon EBS devices run as Kubernetes Pods on nodes in the cluster. With Auto Mode, AWS manages these components and runs them outside of the cluster. This shifts the operational responsibility for the health and patching of these components to AWS and moves the components that require sensitive permissions to operate outside of the cluster.

To manage compute, networking, and storage, EKS Auto Mode requires additional permissions beyond those required in a non-Auto Mode cluster. These are normally provided by adding a [set of policies](https://docs.aws.amazon.com/eks/latest/userguide/auto-cluster-iam-role.html) to the cluster IAM role. However, there is no requirement to attach these specific policies to the cluster role. Custom policies can be used provided they grant sufficient permissions to Auto Mode components.

The [cluster IAM role](https://docs.aws.amazon.com/eks/latest/userguide/auto-cluster-iam-role.html) used by EKS Auto Mode is a service role. A service role is an IAM role that a service assumes to perform actions on your behalf. [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) apply to the actions performed by these roles and can be used to further restrict Auto Mode capabilities, such as [limiting the instance types](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_ec2.html#example-ec2-1) that can be launched. This differs from a service-linked role (SLR), which is a type of role that is linked to an AWS service and is not restricted by SCPs. Auto Mode minimizes its use of SLRs so that SCPs are respected when possible.

**Note**
Additional guidance for adjusting SCPs to allow Auto Mode to function can be found in [Update organization controls for EKS Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/auto-controls.html).
