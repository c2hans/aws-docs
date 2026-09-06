---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/eks.html
---

# Amazon Elastic Kubernetes Service
<a name="eks"></a>

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes. In Kubernetes, *secrets* help you manage sensitive information, such as user certificates, passwords, or API keys. By default, these secrets are stored unencrypted in the API server's underlying data store, which is called [etcd](https://etcd.io/docs/v3.5/faq/). On Amazon EKS, the Amazon Elastic Block Store (Amazon EBS) volumes for `etcd` nodes are encrypted with [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html). Any user with API access or access to `etcd` can retrieve or modify a secret. Additionally, anyone who is authorized to create a pod in a namespace can use that access to read any secret in that namespace. You can encrypt these secrets at rest in Amazon EKS by using AWS KMS keys, either AWS managed keys or customer managed keys. An alternative approach to using `etcd` is using [AWS Secrets and Config Provider (ASCP)](https://github.com/aws/secrets-store-csi-driver-provider-aws) (GitHub repository). ASCP integrates with IAM and resource-based policies to limit and restrict access to secrets only within specific Kubernetes pods inside a cluster.

You can use the following AWS storage services with Kubernetes:
+ For Amazon EBS, you can use the in-tree storage driver or the [Amazon EBS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html). Both include parameters for encrypting volumes and supplying a customer managed key.
+ For Amazon Elastic File System (Amazon EFS), you can use the [Amazon EFS CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html) with support for both dynamic and static provisioning.

Consider the following encryption best practices for this service:
+ If you are using `etcd`, which stores secret objects unencrypted by default, do the following to help protect secrets:
  + [Encrypt secret data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) (Kubernetes documentation).
  + Use AWS KMS for envelope encryption of Kubernetes secrets. This allows you to encrypt your secrets with a unique data key. You can use an AWS KMS key encryption key to encrypt the data key. You can automatically rotate the key encryption key on a recurring schedule. With the AWS KMS plugin for Kubernetes, all Kubernetes secrets are stored in `etcd` in ciphertext. They can only be decrypted by the Kubernetes API server. For more information, see [Using Amazon EKS encryption provider support for defense in depth](https://aws.amazon.com/blogs/containers/using-eks-encryption-provider-support-for-defense-in-depth/) and [Encrypt Kubernetes secrets with AWS KMS on existing clusters](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html).
  + Enable or configure authorization through role-based access control (RBAC) rules that restrict reading and writing the secret. Restrict permissions to create new secrets or replace existing ones. For more information, see [Authorization overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) (Kubernetes documentation).
  + If you are defining multiple containers in a pod and only one of those containers needs access to a secret, define the volume mount so that the other containers do not have access to that secret. Secrets that are mounted as volumes are instantiated as `tmpfs` volumes and are automatically removed from the node when the pod is deleted. You could also use environment variables, but we don't recommend this approach because the values of environment variables can appear in logs. For more information, see [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) (Kubernetes documentation).
  + When possible, avoid granting access to `watch` and `list` requests for secrets within a namespace. In the Kubernetes API, these requests are powerful because they allow the client to inspect the values of every secret in that namespace.
  + Allow only cluster administrators to access `etcd`, including read-only access.
  + If there are multiple `etcd` instances, ensure `etcd` is using TLS for communication between `etcd` peers.
+ If you are using ASCP, do the following to help protect secrets:
  + Use [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) to limit secret access to only authorized pods.
  + Enable encryption of Kubernetes secrets by using the [AWS Encryption Provider](https://github.com/kubernetes-sigs/aws-encryption-provider) (GitHub repository) to implement envelope encryption with a customer managed KMS key.
+ To help mitigate the risk of data leaks from environment variables, we recommend you use the [AWS Secrets Manager and Config Provider for Secret Store CSI Driver](https://github.com/aws/secrets-store-csi-driver-provider-aws) (GitHub). This driver allows you to make secrets stored in Secrets Manager and parameters stored in Parameter Store appear as files mounted in Kubernetes pods.
**Note**
AWS Fargate is not supported.
+ Create an Amazon CloudWatch metrics filter and alarm to send alerts for administrator-specified operations, such as secret deletion or use of a secret version in the waiting period to be deleted. For more information, see [Creating an alarm based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html).
