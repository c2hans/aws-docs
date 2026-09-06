---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/network-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network management
<a name="network-management"></a>

 To set up the SageMaker AI Studio domain, you need to specify the VPC network, subnets, and security groups. When specifying the VPC and subnets, ensure that you allocate IPs considering the usage volume and expected growth that is discussed in the following sections.

## VPC network planning
<a name="vpc-network-planning"></a>

 Customer VPC subnets associated to the SageMaker AI Studio domain must be created with the appropriate Classless Inter-domain Routing (CIDR) range, depending on the following factors:
+  Number of users.
+  Number of apps per user.
+  Number of unique instance types per user.
+  Average number of training instances per user.
+  Expected growth percentage.

SageMaker AI and participating AWS services inject [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (ENI) into the customer VPC subnet for the following use cases:
+  Amazon EFS injects an ENI for an EFS mount target for the SageMaker AI domain (one IP per subnet/Availability Zone attached to the SageMaker AI domain).
+  SageMaker AI Studio injects an ENI for every unique instance used by a user profile or a shared space. For example:
  +  If a user profile runs a *default* Jupyter server app (one ‘system’ instance), a *Data Science* app and a *Base Python* app (both running on an `ml.t3.medium` instance), Studio injects two IP addresses.
  +  If a user profile runs a *default* Jupyter server app (one ‘system’ instance), a *Tensorflow GPU* app (on an `ml.g4dn.xlarge` instance), and a data wrangler app (on an `ml.m5.4xlarge` instance), Studio injects three IP addresses.
+  An ENI for each VPC endpoint across domain VPC subnets/Availability Zones is injected (four IPs for SageMaker AI VPC endpoints; \~six IPs for participating services VPC endpoints such as S3, ECR, and CloudWatch.)
+  If SageMaker AI training and processing jobs are launched with the same VPC configuration, each job needs [two IP addresses per instance](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html#train-vpc-ip).

**Note**
 VPC settings for SageMaker AI Studio, such as subnets and VPC-only traffic, do not get automatically passed on to the training/processing jobs created from SageMaker AI Studio. The user needs to set up VPC settings and network isolation as necessary when calling the Create\*Job APIs. Refer to [Run Training and Inference Containers in Internet-Free Mode](https://docs.aws.amazon.com/sagemaker/latest/dg/mkt-algo-model-internet-free.html) for more information.

 **Scenario: Data scientist runs experiments on two different instance types**

 In this scenario, assume a SageMaker AI domain is set up in VPC-only traffic mode. There are VPC endpoints set up, such as SageMaker AI API, SageMaker AI runtime, Amazon S3, and Amazon ECR.

 A data scientist is running experiments on Studio notebooks, running on two different instance types (for example, `ml.t3.medium` and `ml.m5.large`), and launching two apps in each instance type.

 Assume the data scientist is also simultaneously running a training job with the same VPC configuration on an `ml.m5.4xlarge` instance.

 For this scenario, the SageMaker AI Studio service will inject ENIs as follows:

* Table 1 — ENIs injected into customer VPC for an experimentation scenario *

|   Entity   |   Target   |   ENI injected   |   Notes   |   Level   |
| --- | --- | --- | --- | --- |
|  EFS mount target  |  VPC subnets  |  Three  |  Three AZs/subnets  |  Domain  |
|  VPC endpoints  |  VPC subnets  |  30  |  Three AZs/subnets with 10 VPCE each  |  Domain  |
|  Jupyter Server  |  VPC subnet  |  One  |  One IP per instance  |  User  |
|  KernelGateway app  |  VPC subnet  |  Two  |  One IP per instance type  |  User  |
|  Training  |  VPC subnet  |  Two  |  Two IPs per training instance <br /> Five IPs per training instance if [EFA](https://aws.amazon.com/hpc/efa/) is used  |  User  |

 For this scenario, there are a total of 38 IPs consumed in the customer VPC where 33 IPs are shared across users at the domain level, and five IPs are consumed at the user level. If you have 100 users with similar user profiles in this domain performing these activities concurrently, then you will consume five x 100 = 500 IPs at the user level, on top of the domain level IP consumption, which is 11 IPs per subnet, for a total of 511 IPs. For this scenario, you need to create the VPC subnet CIDR with /22 that will allocate 1024 IP addresses, with room to grow.

## VPC network options
<a name="vpc-network-options"></a>

 A SageMaker AI Studio domain supports configuring the VPC network with one of the following options:
+  Public internet only
+  VPC only

 The **public internet only** option allows SageMaker AI API services to use public internet via the internet gateway provisioned in the VPC, managed by the SageMaker AI service account, as seen in the following diagram:

![Default mode: Internet access via SageMaker AI service account.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/default-mode.png)

 The **VPC only** option disables internet routing from the VPC managed by the SageMaker AI service account, and allows customer to configure the traffic to be routed over VPC endpoints, as seen in the following diagram:

![VPC only mode: No internet access via SageMaker AI service account.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/vpc-only-mode.png)

 For a domain set up in VPC only mode, set up a security group per user profile to ensure complete isolation of underlying instances. Each domain in an AWS account can have its own VPC configuration and internet mode. For more details regarding setting up the VPC network configuration, refer to [Connect SageMaker AI Studio Notebooks in a VPC to External Resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-and-internet-access.html).

## Limitations
<a name="limitations"></a>
+  After a SageMaker AI Studio domain is created, you cannot associate new subnets to the domain.
+  The VPC network type (*public internet only* or *VPC only)* cannot be changed.
