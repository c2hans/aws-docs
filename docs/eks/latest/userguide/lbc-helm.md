---
source_url: https://docs.aws.amazon.com/eks/latest/userguide/lbc-helm.html
---

 **Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Install AWS Load Balancer Controller with Helm

**Tip**
 [Register](https://awsworkshop.io/eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el) for upcoming Amazon EKS workshops.

**Tip**
With Amazon EKS Auto Mode, you don’t need to install or upgrade networking add-ons. Auto Mode includes pod networking and load balancing capabilities.
For more information, see [Automate cluster infrastructure with EKS Auto Mode](automode.md).

This topic describes how to install the AWS Load Balancer Controller using Helm, a package manager for Kubernetes, and `eksctl`. The controller is installed with default options. For more information about the controller, including details on configuring it with annotations, see the [AWS Load Balancer Controller Documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) on GitHub.

The controller needs IAM permissions to manage Elastic Load Balancing resources. This topic grants them with EKS Pod Identity, which doesn’t need an OpenID Connect (OIDC) provider and lets you reuse one IAM role across clusters without editing its trust policy. If the controller runs on Fargate, use IAM roles for service accounts (IRSA) instead, because EKS Pod Identity doesn’t support Fargate. For more information, see [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md) and [IAM roles for service accounts](iam-roles-for-service-accounts.md).

In the following steps, replace the example values with your own values.

## Prerequisites
<a name="lbc-prereqs"></a>

Before starting this tutorial, you must complete the following steps:
+ Create an Amazon EKS cluster. To create one, see [Get started with Amazon EKS](getting-started.md).
+ Install [Helm](https://helm.sh/docs/intro/install/) on your local machine.
+ Install `eksctl` version `0.215.0` or later. For more information, see [Installation](https://eksctl.io/installation/) in the `eksctl` documentation.
+ If you use EKS Pod Identity, install the Amazon EKS Pod Identity Agent add-on on your cluster. For more information, see [Set up the Amazon EKS Pod Identity Agent](pod-id-agent-setup.md).
+ Make sure that your Amazon VPC CNI plugin for Kubernetes, `kube-proxy`, and CoreDNS add-ons are at the minimum versions listed in [Service account tokens](service-accounts.md#boundserviceaccounttoken-validated-add-on-versions).
+ If you plan to use the Gateway API with the AWS Load Balancer Controller, install the standard Gateway API CRDs on your cluster. This requires version 2.13.0 or later of the controller. The Helm chart includes the AWS extension Gateway API CRDs, but not the standard Gateway API CRDs. For installation commands and version requirements, see [Gateway API](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/gateway/gateway/) on GitHub. If your cluster uses EKS Auto Mode with the Gateway API enabled, check who manages these CRDs before you install them. For more information, see [Considerations](#lbc-considerations).
+ Learn about AWS Elastic Load Balancing concepts. For more information, see the [Elastic Load Balancing User Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/).
+ Learn about Kubernetes [service](https://kubernetes.io/docs/concepts/services-networking/service/) and [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) resources.

### Considerations
<a name="lbc-considerations"></a>

Before proceeding with the configuration steps on this page, consider the following:
+ The IAM policy and role (`AmazonEKSLoadBalancerControllerRole`) can be reused across multiple EKS clusters in the same AWS account.
+ If the role already exists, don’t create it again. With EKS Pod Identity, create a Pod Identity association on the new cluster that references the existing role with `--role-arn` instead of `--role-name`. The role’s trust policy must allow the `pods.eks.amazonaws.com` service principal. For more information, see [Assign an IAM role to a Kubernetes service account](pod-id-association.md).
+ With IRSA, the OIDC provider ARN in the role’s trust policy is specific to each cluster. To install the controller on a new cluster with an existing `AmazonEKSLoadBalancerControllerRole`, update the role’s trust policy to include the new cluster’s OIDC provider, and create a service account with the role annotation. To determine whether you already have an OIDC provider, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md).
+ EKS Auto Mode supports the Gateway API without the AWS Load Balancer Controller. If your cluster uses EKS Auto Mode with the Gateway API enabled, the cluster’s Gateway API CRD setting decides who owns the Gateway API CRDs. These CRDs are cluster-wide, so only one party owns them at a time. With the **Managed** setting, AWS installs and owns the standard Gateway API CRDs and the AWS extension CRDs (`LoadBalancerConfiguration`, `TargetGroupConfiguration`, and `ListenerRuleConfiguration`). Don’t install or upgrade these CRDs yourself, including with the commands in the AWS Load Balancer Controller Gateway API guide. With the **Unmanaged** setting, you own the CRDs, and you install and upgrade them yourself. For more information, see [Enable the Gateway API on your cluster](auto-configure-gateway-api.md#auto-configure-gateway-api-crds).

## Step 1: Create the IAM role
<a name="lbc-helm-iam"></a>

The following steps refer to the AWS Load Balancer Controller **v3.6.3** release version. For more information about all releases, see the [AWS Load Balancer Controller Release Page](https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/) on GitHub.

1. Download an IAM policy for the AWS Load Balancer Controller that allows it to make calls to AWS APIs on your behalf. Use the command for the partition your cluster is in.
**Example**

------
#### [  AWS  ]

   ```shell
   curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v3.6.3/docs/install/iam_policy.json
   ```

------
#### [  AWS GovCloud (US) ]

   ```shell
   curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v3.6.3/docs/install/iam_policy_us-gov.json
   ```

------
#### [ China ]

   ```shell
   curl -o iam_policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v3.6.3/docs/install/iam_policy_cn.json
   ```

------

1. Create an IAM policy using the policy downloaded in the previous step.

   ```shell
   aws iam create-policy \
       --policy-name AWSLoadBalancerControllerIAMPolicy \
       --policy-document file://iam_policy.json
   ```
**Note**
If you view the policy in the AWS Management Console, the console shows warnings for the **ELB** service, but not for the **ELB v2** service. This happens because some of the actions in the policy exist for **ELB v2**, but not for **ELB**. You can ignore the warnings for **ELB**.

1. Create the IAM role and the Kubernetes service account for the controller. Replace {{my-cluster}} with the name of your cluster, {{111122223333}} with your account ID, and {{region-code}} with the AWS Region that your cluster is in.
**Example**

------
#### [ EKS Pod Identity ]

   1. Run the following command. It creates the IAM role with the policy attached, creates the `aws-load-balancer-controller` service account, and creates a Pod Identity association between them.

      ```shell
      eksctl create podidentityassociation \
          --cluster {{my-cluster}} \
          --namespace kube-system \
          --service-account-name aws-load-balancer-controller \
          --permission-policy-arns arn:aws:iam::[.replaceable]111122223333:policy/AWSLoadBalancerControllerIAMPolicy \
          --role-name AmazonEKSLoadBalancerControllerRole \
          --create-service-account \
          --region {{region-code}}
      ```

------
#### [ IRSA ]

   1. Make sure that your cluster has an IAM OIDC provider. For more information, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md).

   1. Run the following command. It creates the IAM role with the policy attached and creates the `aws-load-balancer-controller` service account with the role annotation.

      ```shell
      eksctl create iamserviceaccount \
          --cluster {{my-cluster}} \
          --namespace kube-system \
          --name aws-load-balancer-controller \
          --role-name AmazonEKSLoadBalancerControllerRole \
          --attach-policy-arn arn:aws:iam::[.replaceable]111122223333:policy/AWSLoadBalancerControllerIAMPolicy \
          --override-existing-serviceaccounts \
          --region {{region-code}} \
          --approve
      ```

------

## Step 2: Install AWS Load Balancer Controller
<a name="lbc-helm-install"></a>

1. Add the `eks-charts` Helm chart repository. AWS maintains [this repository](https://github.com/aws/eks-charts) on GitHub.

   ```shell
   helm repo add eks https://aws.github.io/eks-charts
   ```

1. Update your local repo to make sure that you have the most recent charts.

   ```shell
   helm repo update eks
   ```

1. Install the AWS Load Balancer Controller.

   If you’re deploying the controller to Amazon EC2 nodes that have [restricted access to the Amazon EC2 instance metadata service (IMDS)](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html#_identities_and_credentials_for_eks_pods_recommendations), or if you’re deploying to Fargate or Amazon EKS Hybrid Nodes, then add the following flags to the `helm` command that follows:
   +  `--set region={{region-code}} `
   +  `--set vpcId={{vpc-xxxxxxxx}} `

     Replace {{my-cluster}} with the name of your cluster. The command uses the `aws-load-balancer-controller` service account that you created in the previous step, so it sets `serviceAccount.create` to `false`. Since controller v3.0.0, the Helm chart version matches the controller version.

     For more information about configuring the Helm chart, see [values.yaml](https://github.com/aws/eks-charts/blob/master/stable/aws-load-balancer-controller/values.yaml) on GitHub.

     ```shell
     helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
       -n kube-system \
       --set clusterName={{my-cluster}} \
       --set serviceAccount.create=false \
       --set serviceAccount.name=aws-load-balancer-controller \
       --version 3.6.3
     ```

**Important**
The deployed chart doesn’t receive security updates automatically. You need to manually upgrade to a newer chart when it becomes available. To upgrade, change `install` to `upgrade` in the previous command, and set `--version` to the new chart version.

The `helm install` command automatically installs the custom resource definitions (CRDs) for the controller. The `helm upgrade` command doesn’t. Before you run `helm upgrade`, install the latest CRDs with the following command:

```shell
curl -O https://raw.githubusercontent.com/aws/eks-charts/master/stable/aws-load-balancer-controller/crds/crds.yaml
kubectl apply -f crds.yaml
```

The `crds.yaml` file doesn’t include the AWS extension Gateway API CRDs (`LoadBalancerConfiguration`, `TargetGroupConfiguration`, and `ListenerRuleConfiguration`). The Helm chart includes them in a separate `gateway-crds.yaml` file, which `helm install` installs and `helm upgrade` doesn’t. If you use the Gateway API and run `helm upgrade`, also run the following command:

```shell
curl -O https://raw.githubusercontent.com/aws/eks-charts/master/stable/aws-load-balancer-controller/crds/gateway-crds.yaml
kubectl apply -f gateway-crds.yaml
```

On an EKS Auto Mode cluster where AWS manages the Gateway API CRDs, don’t apply `gateway-crds.yaml`. For more information, see [Considerations](#lbc-considerations).

## Step 3: Verify that the controller is installed
<a name="lbc-helm-verify"></a>

1. Verify that the controller is installed.

   ```shell
   kubectl get deployment -n kube-system aws-load-balancer-controller
   ```

   An example output is as follows.

   ```bash
   NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
   aws-load-balancer-controller   2/2     2            2           84s
   ```

   You receive the previous output if you deployed using Helm. If you deployed using the Kubernetes manifest, you only have one replica.

1. Before using the controller to provision AWS resources, your cluster must meet specific requirements. For more information, see [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md) and [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md).
