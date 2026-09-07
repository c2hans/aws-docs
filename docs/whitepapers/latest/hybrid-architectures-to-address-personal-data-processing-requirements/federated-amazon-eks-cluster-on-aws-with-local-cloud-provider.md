---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/federated-amazon-eks-cluster-on-aws-with-local-cloud-provider.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.5 Federated Amazon EKS cluster on AWS with local cloud provider
<a name="federated-amazon-eks-cluster-on-aws-with-local-cloud-provider"></a>

 Requirements addressed:
+  **REQ4** (availability and durability)

 AWS services – [Amazon EKS](https://aws.amazon.com/eks/)

![Federated Amazon EKS cluster on AWS](https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/federated-eks-cluster-on-aws.png)

 Federated Amazon EKS cluster on AWS

 The federated control pod is deployed as a regular pod into Kubernetes cluster. For high availability purposes, we recommend that you make the [Amazon EKS](https://aws.amazon.com/eks/) cluster primary.

 Requirements **REQ2** (data protection) and **Customer-REQ1** (reliable connectivity) can be met using Architecture 1.1: [Hybrid network connectivity from a data center to the AWS Cloud](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md).

 Federation can be done through the [kubefed project](https://pkg.go.dev/sigs.k8s.io/kubefed), which allows you to coordinate the configuration of multiple Kubernetes clusters from a single set of APIs in a hosting cluster.

**Note**
 This architecture is not for Data Residency **(REQ1)**, as kubefed does not support federated management of persistent volumes, so you cannot manage databases in Kubernetes in federated mode.

 Use cases:

1.  **Dynamic capacity scale-out** in the AWS Cloud for stateless workloads (not containing personal data)

1.  **Geo- or latency-sensitive workloads** (such as gaming workloads)

1.  **Data residency** use cases:

   1.  A local-based API application in local a Kubernetes deployment (as part of Federation) with access to a local database

   1.  A cloud-based API application in an Amazon EKS cluster (primary cluster in Federation) with access to an AWS database

1.  **Single point of administration, configuration, or deployment** (shared resources, configurations, API) among multiple geo-based Kubernetes clusters
