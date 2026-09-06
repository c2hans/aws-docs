---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/example-dropboxs-hybrid-cloud-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Example: Dropbox’s hybrid cloud architecture
<a name="example-dropboxs-hybrid-cloud-architecture"></a>

 Dropbox built a hybrid cloud with AWS, enabling the use cases of distributed data processing, cloud bursting, disaster recovery, and geographical expansion.

 The following figure provides a view of the technical architecture for Dropbox’s hybrid software stack built with AWS.

![Dropbox’s hybrid software stack](http://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/images/dropbox-hybrid-sw-stack.png)

* Dropbox’s hybrid software stack *

 Dropbox’s machine management service provides host management capabilities for on-premises infrastructure, as well as a common set of tools for systems management for infrastructure in both AWS and on-premises, such as device inventory, software management, installation, patching, remote command execution, service discovery, and more. Additionally, Dropbox’s monitoring services provide unified metrics and logging service for the hybrid cloud.

 Further up the hybrid stack, Dropbox’s compute, storage, and database hybrid services leverage the core services, and provide the management interfaces for provisioning, managing, and operating infrastructure on the hybrid cloud.

 Using these infrastructure and core services, Dropbox’s developers are provided with a unified set of interfaces and tools to provision, operate, and manage infrastructure and services on the hybrid cloud with AWS. Dropbox has implemented distributed data processing in the hybrid cloud to leverage AWS innovation for several workloads such as data lake and analytics, machine learning infrastructure, document previews, audit logging, and more. Dropbox leverages the scale and agility provided by AWS through deployments of [Dropbox Paper](https://www.dropbox.com/paper) and [Dropbox HelloSign](https://www.dropbox.com/business/hellosign) products on AWS. Additionally, Dropbox has deployed their application services in AWS Regions in Frankfurt, Tokyo, and Sydney, using their hybrid architecture for geographic expansion. Details of Dropbox’s hybrid cloud strategy and implementation are described in [Dropbox’s re:Invent presentation](https://www.youtube.com/watch?v=1_hKrGjYteQ).
