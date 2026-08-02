---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-sas-viya-to-the-aws-cloud/costs-and-licenses.html
---

# Costs and licenses
<a name="costs-and-licenses"></a>

The cost of migrating a SAS workload to AWS assumes that you establish a new environment on AWS. This includes accounting for personnel time and effort in addition to provisioning computing resources and licensing software for the new environment.

## Costs
<a name="costs"></a>

SAS Viya is a cloud-native analytics platform on which the latest software offerings from SAS are built and run. SAS Viya offerings are delivered as a set of container images that are deployed with Amazon EKS.

To most accurately estimate the costs of establishing a new SAS Viya environment on AWS, use the [AWS Pricing Calculator](https://calculator.aws/). The calculator helps you estimate the monthly cost of AWS services, based on your expected usage. It is continuously updated with the latest pricing for all AWS services in all Regions and includes support for most AWS services. You can include additional costs, such as inbound-data and outbound-data charges and retrieval fees. You can also select Amazon EC2 with various pricing models, such as On-Demand, Dedicated, and Reserved Instances. We recommend that you use the calculator with the following baseline requirements for a SAS Viya deployment.

### Baseline resource recommendations
<a name="baseline-resource-recommendations.c355a987-9abf-5575-b240-f8ace0f8d76d"></a>

The following table provides baseline resource recommendations for SAS Viya product offerings. The estimates are derived from SAS performance testing and intended for medium-sized deployment, which is defined as 10 concurrent users that access SAS Viya user interfaces. In SAS testing simulations, users manipulated datasets of 10–30 GB. The Amazon EC2 virtual machine instances used an Intel Xeon Platinum 8000 series processor or better. On AWS, the number of vCPUs for an instance is indicated by a number in the instance type name (multiplied by four). For example, the m5n.2xlarge instance type provides 8 vCPUs, which is the equivalent of 4 physical CPU cores.

The following table provides baseline resource requirements per offering.

|
|
| **Offering** | **CAS node group** | **Default node group** | **Additional managed-node groups\*** |
| --- |--- |--- |--- |
| SAS visual analytics and SAS data preparation | RAM: 128 GB per instanceCPU: 16 vCPUs or 8 physical cores per instanceExample: r5dn.4xlargeRecommended minimum for CAS disk cache: 150 GB; ephemeral storageExample number of machines: 4 | RAM: 64 GBCPU: 8 vCPUs or 4 physical coresExample: m5n.2xlargeExample number of machines: 1 | RAM: 64 GB per instanceCPU: 8 vCPUs or 4 physical cores per instanceExample: m5n.2xlargeRecommended minimum ephemeral storage for selected applications: 60 GBExample number of machines: 1 per node group |
| SAS visual machine learning | RAM: 128 GB per instanceCPU: 16 vCPUs or 8 physical cores per instanceExample: r5dn.4xlargeRecommended minimum for CAS disk cache: 600 GB; ephemeral storageExample number of machines: 8 | RAM: 64 GBCPU: 8 vCPUs or 4 physical coresExample: m5.2xlargeExample number of machines: 1 | RAM: 128 GB per instanceCPU: 16 vCPUs or 8 physical cores per instanceExample: r5dn.4xlargeMinimum disk: 2 x 128 GBExample number of machines: 1 per node group |
| SAS visual data science | RAM: 384 GB per instanceCPU: 48 vCPUs or 24 physical cores per instanceExample: r5dn.12xlargeRecommended minimum for CAS disk cache: 1200 GBExample number of machines: 9 | RAM: 64 GBCPU: 8 vCPUs or 4 physical coresExample: m5n.2xlargeExample number of machines: 1 | RAM: 128 GB per instanceCPU: 48 vCPUs or 24 physical coresExample: r5dn.12xlargeMinimum disk: 2 x 128 GBExample number of machines: 1 per node group |

\* In addition to the CAS node group, four managed node groups are recommended to host the remaining SAS Viya workload classes.

These guidelines do not attempt to account for all ordering scenarios but are instead intended to illustrate typical software orders. SAS recommends that you consult with a sizing expert to obtain an official hardware recommendation that is based on your requirements. To request sizing expertise, contact your SAS account representative. For help with finding your SAS account representative, contact SAS at *contactcenter@sas.com*.

## Licenses
<a name="licenses"></a>

Although SAS 9 and SAS Viya 3.x licensing models are based primarily on capacity metrics** **(that is, the number of processing cores), SAS Viya licensing follows a cloud-native model that uses boundless scaling. Core-based licensing does not make sense in the context of a dynamic containerized architecture. In an elastic cloud architecture, customers need the flexibility to fit their supporting infrastructure to their analytic needs in real time. The number and size of containers vary because containers are regularly spun up and down in response to the volume of software use. This fundamental aspect of containerized cloud architectures means that licensing is unrelated to the number of SAS Cloud Analytic Services (CAS) and Programming Runtime Environment (SPRE) cores. But it is related to the number of users, types of users, and total revenue.

Pricing metrics depend on the SAS Viya license offer. Furthermore, SAS and ACCESS products are no longer licensed separately but are included in their respective offerings. For SAS Viya offerings that are priced by user type, authorized users are distinct: data scientists, power users, and viewers. Each user is licensed separately and has its own quantity and price so that the value of users is better aligned with tasks and how customers use the software.

Each licensed user must have a unique ID and authorization to access the software. Unlike the policy for total-user licensing, guest users are prohibited because they do not have authorized user IDs. Additionally, licenses for some user types do not apply to some offerings. The only SAS Viya offering that has a user minimum is SAS Model Manager (on SAS Viya), which requires a minimum of five authorized data scientists.
