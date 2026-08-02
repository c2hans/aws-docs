---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/amazon-eks-secrets.html
---

# Accessing and managing secrets for Amazon EKS
<a name="amazon-eks-secrets"></a>

[Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes. Amazon EKS uses [Base64](https://en.wikipedia.org/wiki/Base64) (Wikipedia) encoding to help protect sensitive data.  *Encoding* is designed to prevent data modification during transit between systems, and *encryption* is designed to prevent unauthorized access to the data. Base64 encoding is not sufficient to help protect data from unauthorized access. Use AWS Secrets Manager to help protect sensitive data in Amazon EKS.

The following image shows Amazon EKS deployed on an [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance, which acts as a Kubernetes worker node. You can use a container storage interface (CSI) driver to retrieve secrets from Secrets Manager.  For more information, see [How to use AWS Secrets & Configuration Provider with your Kubernetes Secrets Store CSI driver](https://aws.amazon.com/blogs/security/how-to-use-aws-secrets-configuration-provider-with-kubernetes-secrets-store-csi-driver/) in the AWS Security Blog.

![Amazon EKS deployed on Amazon EC2.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/images/guide-img/e6185df2-3707-4018-a94c-6edc793f0353/images/90c2c92b-0dd3-409e-8f22-8c33f4b38e1f.png)

The following image shows Amazon EKS deployed on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html). You can use the open source [External Secrets Operator API](https://github.com/external-secrets/external-secrets) (GitHub) to retrieve secrets from Secrets Manager. For more information, see [Leverage AWS secrets stores from EKS Fargate with External Secrets Operator](https://aws.amazon.com/blogs/containers/leverage-aws-secrets-stores-from-eks-fargate-with-external-secrets-operator/) in the AWS Containers Blog.

![Amazon EKS deployed on AWS Fargate.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/images/guide-img/e6185df2-3707-4018-a94c-6edc793f0353/images/79e0f20a-c152-4a6b-8c0e-76fd96e4f86e.png)
