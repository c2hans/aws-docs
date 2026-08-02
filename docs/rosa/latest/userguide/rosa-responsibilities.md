---
source_url: https://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html
---

# Overview of responsibilities for ROSA
<a name="rosa-responsibilities"></a>

This documentation outlines the responsibilities of Amazon Web Services (AWS), Red Hat, and customers for the Red Hat OpenShift Service on AWS (ROSA) managed service. For more information about ROSA and its components, see [Policies and service definition](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition) in the Red Hat documentation.

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model) defines AWS responsibility for protecting the infrastructure that runs all of the services offered in the AWS Cloud, including ROSA. AWS infrastructure includes the hardware, software, networking, and facilities that run AWS Cloud services. This AWS responsibility is commonly referred to as the “security of the cloud”. To operate ROSA as a fully managed service, Red Hat and the customer are responsible for the elements of the service that the AWS responsibility model defines as “security in the cloud”.

Red Hat is responsible for the ongoing management and security of the ROSA cluster infrastructure, the underlying application platform, and the operating system. While ROSA clusters are hosted on AWS resources in the customer AWS accounts, they are accessed remotely by ROSA service components and Red Hat site reliability engineers (SREs) through IAM roles that the customer creates. Red Hat uses this access to manage the deployment and capacity of all control plane and infrastructure nodes on the cluster, and maintain versions for the control plane nodes, infrastructure nodes, and worker nodes.

Red Hat and the customer share responsibility for ROSA network management, cluster logging, cluster versioning, and capacity management. While Red Hat manages the ROSA service, the customer is fully responsible for managing and securing any applications, workloads, and data deployed to ROSA.

## Overview
<a name="responsibility-overview"></a>

The following table provides an overview of AWS, Red Hat, and customer responsibilities for Red Hat OpenShift Service on AWS.

**Note**
If the `cluster-admin` role is added to a user, see the responsibilities and exclusion notes in the [Red Hat Enterprise Agreement Appendix 4 (Online Subscription Services)](https://www.redhat.com/en/about/appendices).

|  **Resource**  |  **Incident and operations management**  |  **Change management**  |  **Access and identity authorization**  |  **Security and regulation compliance**  |  **Disaster recovery**  |
| --- | --- | --- | --- | --- | --- |
|  **Customer data**  | Customer | Customer | Customer | Customer | Customer |
|  **Customer applications**  | Customer | Customer | Customer | Customer | Customer |
|  **Developer services**  | Customer | Customer | Customer | Customer | Customer |
|  **Platform monitoring**  | Red Hat | Red Hat | Red Hat | Red Hat | Red Hat |
|  **Logging**  | Red Hat | Red Hat and customer | Red Hat and customer | Red Hat and customer | Red Hat |
|  **Application networking**  | Red Hat and customer | Red Hat and customer | Red Hat and customer | Red Hat | Red Hat |
|  **Cluster networking**  | Red Hat | Red Hat and customer | Red Hat and customer | Red Hat | Red Hat |
|  **Virtual networking management**  | Red Hat and customer | Red Hat and customer | Red Hat and customer | Red Hat and customer | Red Hat and customer |
|  **Virtual compute management (control plane, infrastructure, and worker nodes)**  | Red Hat | Red Hat | Red Hat | Red Hat | Red Hat |
|  **Cluster version**  | Red Hat | Red Hat and customer | Red Hat | Red Hat | Red Hat |
|  **Capacity management**  | Red Hat | Red Hat and customer | Red Hat | Red Hat | Red Hat |
|  **Virtual storage management**  | Red Hat | Red Hat | Red Hat | Red Hat | Red Hat |
|  ** AWS software (public AWS services)**  |  AWS  |  AWS  |  AWS  |  AWS  |  AWS  |
|  **Hardware/AWS global infrastructure**  |  AWS  |  AWS  |  AWS  |  AWS  |  AWS  |

## Tasks for shared responsibilities by area
<a name="responsibility-tasks-by-area"></a>

 AWS, Red Hat, and customers share responsibility for the monitoring and maintenance of ROSA components. This documentation defines ROSA service responsibilities by area and task.

### Incident and operations management
<a name="incident-ops-management"></a>

 AWS is responsible for protecting the hardware infrastructure that runs all of the services offered in the AWS Cloud. Red Hat is responsible for managing the service components necessary for default platform networking. The customer is responsible for incident and operations management of customer application data and any custom networking the customer may have configured.

|  **Resource**  |  **Service responsibilities**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Application networking**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual networking management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual storage management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  ** AWS software (public AWS services)**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Hardware/AWS global infrastructure**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |

### Change management
<a name="change-management"></a>

 AWS is responsible for protecting the hardware infrastructure that runs all of the services offered in the AWS Cloud. Red Hat is responsible for enabling changes to the cluster infrastructure and services that the customer will control, as well as maintaining versions for the control plane nodes, infrastructure nodes, and worker nodes. The customer is responsible for initiating infrastructure changes. The customer is also responsible for installing and maintaining optional services, networking configurations on the cluster, and changes to customer data and applications.

|  **Resource**  |  **Service responsibilities**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Logging**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Application networking**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Cluster networking**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual networking management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual compute management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Cluster version**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Capacity management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual storage management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  ** AWS software (public AWS services)**  |  ** AWS ** <br /> **Compute** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Storage** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Networking** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Hardware/AWS global infrastructure**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |

### Access and identity authorization
<a name="access-identity-auth"></a>

Access and identity authorization includes responsibilities for managing authorized access to clusters, applications, and infrastructure resources. This includes tasks such as providing access control mechanisms, authentication, authorization, and managing access to resources.

|  **Resource**  |  **Service responsibilities**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Logging**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Application networking**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Cluster networking**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual networking management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual compute management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual storage management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  ** AWS software (public AWS services)**  |  ** AWS ** <br /> **Compute** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Storage** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Networking** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Hardware/AWS global infrastructure**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |

### Security and regulation compliance
<a name="security-regulation-compliance"></a>

The following are the responsibilities and controls related to compliance:

|  **Resource**  |  **Service responsibilities**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Logging**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual networking management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual compute management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual storage management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  ** AWS software (public AWS services)**  |  ** AWS ** <br /> **Compute** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Storage** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Networking** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Hardware/AWS global infrastructure**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |

### Disaster recovery
<a name="disaster-recovery"></a>

Disaster recovery includes data and configuration backup, data replication and configuration of the disaster recovery environment, and failover on disaster events.

|  **Resource**  |  **Service responsibilities**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Virtual networking management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual compute management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Virtual storage management**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  ** AWS software (public AWS services)**  |  ** AWS ** <br /> **Compute** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Storage** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> **Networking** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Hardware/AWS global infrastructure**  |  ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |

## Customer responsibilities for data and applications
<a name="customer-responsibilities"></a>

The customer is responsible for the applications, workloads, and data that they deploy to Red Hat OpenShift Service on AWS. However, AWS and Red Hat provide various tools to help the customer manage data and applications on the platform.

|  **Resource**  |  **How AWS and Red Hat helps**  |  **Customer responsibilities**  |
| --- | --- | --- |
|  **Customer data**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
|  **Customer applications**  |  **Red Hat** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html)<br /> ** AWS ** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |  **Customer** [See the AWS documentation website for more details](http://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html) |
