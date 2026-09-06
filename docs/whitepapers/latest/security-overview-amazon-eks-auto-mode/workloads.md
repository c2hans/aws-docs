---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-overview-amazon-eks-auto-mode/workloads.html
---

# Workloads
<a name="workloads"></a>

With EKS Auto Mode, customers continue to maintain responsibility for their application containers, including availability, security, and monitoring. Auto Mode provides a solid foundation to build upon, but there are several areas where following EKS best practices can improve the security posture of those workloads.

## Configuration
<a name="configuration"></a>

Because EKS Auto Mode nodes are Kubernetes conformant, standard Pod-level configurations work as expected. For example, the Pod `securityContext` field can be used to give additional permissions to Pods and `volumeMounts` can be used to provide access to the host filesystem. Even then, Pods however still face the restrictions provided by SELinux and a read-only root filesystem on the node. You can use Kubernetes policy enforcement tools like [Kyverno](https://kyverno.io/) or [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/) to limit Pod-level configuration within a cluster. Additional guidance for Pod security can be found in the [EKS Best Practices guide](https://docs.aws.amazon.com/eks/latest/best-practices/pod-security.html).

To vend IAM credentials to Pods within a cluster, EKS Auto Mode nodes include built-in support for [EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html). When a Pod is launched using a Kubernetes service account that is configured with Pod Identity, the Kubernetes control plane injects a set of environment variables into the Pod. These environment variables cause the AWS SDK to request credentials from the Pod Identity component that Auto Mode has preconfigured on the Node. This process involves the AWS SDK fetching the Pod's service account token, assigned by the Kubernetes API server, and exchanging it for IAM credentials via the `eks-auth:AssumeRoleForPodIdentity` API. This is the only permission on the managed [AmazonEKSWorkerNodeMinimalPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEKSWorkerNodeMinimalPolicy.html) policy.

**Note**
[IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (IRSA) can also be configured to provide credentials to Pods, while Pod Identity remains the recommended method.

## Runtime monitoring
<a name="runtime-monitoring"></a>

Runtime monitoring observes and analyzes operating system level, networking, and file events to help you detect potential threats in the workloads in your environment. This can include detection of issues such as container breakouts, creation of reverse shells, or elevation of privileges.

Because EKS Auto Mode nodes are fully Kubernetes conformant, runtime monitoring systems that are compatible with Kubernetes nodes should work with Auto Mode nodes. We recommend using [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/eks-runtime-monitoring-guardduty.html) or a third-party solution that is validated to work with Auto Mode for runtime monitoring. The full list of runtime issues that GuardDuty can detect is available in [GuardDuty Runtime Monitoring finding types](https://docs.aws.amazon.com/guardduty/latest/ug/findings-runtime-monitoring.html).
