---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/mapping-etsi-mano-to-kubernetes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Mapping ETSI MANO to Kubernetes
<a name="mapping-etsi-mano-to-kubernetes"></a>

 In this section, we depict the high-level mapping of Kubernetes objects and functions to ETSI MANO architecture, with the following sections going in detail over each of the components:
+  Virtual Infrastructure Manager (VIM)
+  Virtual Network Function Manager (VNFM)
+  NFV Orchestrator (NFVO) and its mapping to Kubernetes in detail

## High-level mapping architecture
<a name="high-level-mapping-architecture"></a>

 The traditional ETSI MANO framework was developed in the context of virtual machines (VM). The following figure indicates ETSI MANO architecture along with major functions performed by each of its components. Network slice management and its associated functions such as Network Slice Subnet Management Function (NSSMF) and Network Function Management Function (NFMF) are part of [3GPP](https://www.3gpp.org/) specifications and are beyond the realm of MANO framework; however, they are shown in the figure to provide complete view of network and service management.

![A diagram depicting the traditional ETSI MANO framework as defined in the context of virtual machines along with 3GPP management functions..](https://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/images/etsi-mano-framework.jpg)

## Mapping VIM and VNFM to Kubernetes
<a name="mapping-vim-and-vnfm-to-kubernetes"></a>

 In this section, we focus on the VIM and VNFM functional blocks of the ETSI MANO architecture and its functions, and then map to equivalent cloud-native constructs.

 Following are the requirements that the MANO architecture puts on VIM:
+  Manage lifecycle of virtual resources in an NFVI domain. Create, maintain, and tear down VMs from physical resources in an NFVI domain:
+  Keep inventory of VMs associated with physical resources.
+  Performance and fault management of hardware, software and virtual resources.
+  Exposes physical and virtual resources to other management systems through northbound APIs.

 In Kubernetes context, VIM is responsible for placing Pods and containers on nodes that can be bare-metal machine or a virtualization platform themselves. In this regard, the second and third requirements are out of scope of Kubernetes-based VIM in a cloud operational environment, specifically when we consider features such as automatic scaling node groups provided by managed Kubernetes solutions such as EKS. The functionality of the first and last requirements are also provided by services such as managed node groups and automatic scaling node groups in EKS.

 VNFM performs the following tasks:
+  **Manage life cycle of VNFs** — VNFM creates, maintains, and ends VNF instances, which are installed on the Virtual Machines (VMs) that the VIM creates and manages).
+  **Fault, configuration, accounting, performance, and security** **(FCAPS)** — Management of VNFs. VNFM doesn’t deal with application specific FCAPS, but generic FCAPS dealing with virtualization.
+  **Scale up/scale down VNFs which results in scaling up and scaling down of CPU usage** — While the original VNFs were mostly scaled vertically, in the cloud model, there are two kinds of scaling: horizontal and vertical. Horizontal scaling is often the preferred mode of operation.

 When applications are containerized (instead of virtualized), they are referred to as a containerized network function (CNF). In Kubernetes, containerized applications are run as Pods. Kubernetes manages the lifecycle of Pods, and scales them up and down using changes in deployments as specified constraints in configurations such as minimum, maximum, and desired number of replicas.

 Operation and management of infrastructure and platform is intrinsically provided by common cloud tools such as AWS CloudWatch, K8 config-maps. Due to scale, organization and security issues, one Kubernetes cluster is generally not sufficient for a telecom network operator, and a multi-cluster infra management solution is needed. There are many open-source and vendor provided solutions to manage multiple Kubernetes clusters. In AWS, this multi-cluster control plane management is provided by the EKS main control plane, which ensure that all clusters are healthy and scale as needed. The EKS dashboard provides a single pane of glass to manage multiple clusters, though each cluster does have its own API endpoint to which kubectl and helm commands are directed.

 From the description and analysis for VIM and VNFM, it might seem like there is a good correlation between ETSI requirements and Kubernetes. However, ETSI MANO differs from the Kubernetes model in that the VNFM maintains a detailed view of deployed virtualization aspect of its associated VNFs, and exposes it northbound to NFVO. In Kubernetes, that information is not exposed. Kubernetes doesn’t expose its internal workings and placement to the upper layers. The only way to control the operations is by clearly defined intents (which can include labels, tags, selectors, and so on), which forces the application to interact only through intents and object definitions.

When mapping ETSI MANO to Kubernetes and the cloud, it is important to re-interpret the ETSI MANO architecture to avoid sharing details of the lower layers, such as EC2 instances, to upper layers. With powerful functionalities such as managed node groups and automatic scaling constructs in AWS, the NFVO should not be affected by lower-level changes.

## NFVO: functions and mapping
<a name="nfvo-functions-and-mapping"></a>

 NFVO is the brain and heart of ETSI orchestration. Before exploring its mapping to Kubernetes, the following points are worth mentioning about VNFs:
+  A VNF can’t bring itself to service.
+  Every VNF needs to be managed and orchestrated.
+  A network service (NS) is composed of one of more VNFs. NS is onboarded on NFVO.
+  An NS lifecycle is managed by NFVO.
+  VNF lifecycle is managed by VNFM, which is responsible for bringing VNF into existence following the templates in VNF descriptor.
+  VNF scaling can be invoked by NFVO, by [element manager](https://en.wikipedia.org/wiki/Element_management_system) (EM), or the VNF can ask to scale itself based on VNF load.

 Due to these characteristics of VNFs, the following functions are required of NFVO:
+  Manage/coordinate the resources from different VIMs, when there are multiple VIMs (that may be in the same or different physical resources), NFVO calls northbound APIs of VIM instead of engaging with the NFVI resources directly.
+  Manage/coordinate the creation of a service that involves multiple VNFs that might be managed by different VNFMs. In NFVO parlance, this is sometimes called service orchestration. Often, this is a source of confusion because in the cloud model, a service might represent an application.
+  Manage topology of the network services instances (also called VNF forwarding graphs).

 In particular, NFVO is responsible to track scale status, virtualized resources used, and connectivity to VIMs to manage the resources of VNFs. In ETSI MANO, some of the functionalities done by VNFM are controlled by NFVO in imperative way by mechanisms such as request and grant, where VNFM asks explicit permissions from NFVO for some of its operations. This required NFVO to micro-manage some of VNFM operations, which it should have ignored.

 To be fair, ETSI IFA029 specification did translate VIM and VNFM architecture and requirements into a container framework by creating new terms Container Infrastructure Service (CIS), Container Infrastructure Service Management (CISM) and Container Infrastructure Service Instance (CISI). However, IFA029 didn’t get sufficient exposure, partly due to the difficulty in interpreting the new abstraction for containerized platforms, instead of directly describing functionalities in well-known Kubernetes terms. This required additional effort in reading and translating IFA029 to Kubernetes. Because the Kubernetes framework has become a standard for telecom network equipment providers (NEPs) and ISVs to use for their functions, in this whitepaper, we chose to directly translate requirements to Kubernetes. When we need specific product details, we have used Amazon EKS and associated services.

 In light of the previous discussions, in the following diagram, we propose a way to map the same ETSI defined functions to corresponding Kubernetes and associated objects. Notice that the mapping is not 1-1, and Kubernetes and associated services such as ECR and [Helm](https://helm.sh/) cover more than one element of the ETSI MANO architecture.

![A diagram depicting the ETSI MANO Framework and Kubernetes and associated constructs.](https://docs.aws.amazon.com/whitepapers/latest/ETSI-NFVO-compliant-orchestration-in-kubernetes/images/etsi-mano-framework2.png)

 This creates some difficulties in applying understandings gained from ETSI MANO NFV to Kubernetes operational environments. Some of these difficulties are discussed next.

## Framework mapping challenges
<a name="framework-mapping-challenges"></a>

 As outlined earlier, the main difficulty in mapping ETSI MANO model to Kubernetes framework is that the first takes the declarative approach to imperative operations, whereas the later takes the declarative approach to an intent-based framework. ETSI MANO specifies direct procedures between NFVO and VNFM and VIM, whereas Kubernetes performs all communication among its components as well as on north and southbound interfaces by artifacts, APIs and manifests with specification of the desired final state of operation. This paper next discusses in detail the impact of this difference in approaches.

 The ETSI MANO architecture uses lifecycle operation granting, where ETSI VNFM asks NFVO before initiating changes within the defined parameters. Kubernetes doesn’t ask the orchestrator whether to scale in, scale out, where to place, and so on. In the Kubernetes style of operation, NFVO only needs to define the desired end state in declarative ways by defining artifacts, such as deployment and service YAML files, and then Kubernetes schedules ensures operation within the specified range. When needed, Kubernetes can also use the cluster automatic scaler to request additional resources from an underlying cloud infrastructure to meet the additional needs of a Kubernetes workload within its realm of operations.

 Lifecycle operation granting duplicates the work and breaks the hierarchical model. In the cloud-native world, NFVO indication of the desired state of operation should be implemented using intent-driven Kubernetes constructs and changes to Deployment and so on, instead of implementing the procedural model between the NFVO and VNFM.

 The Kubernetes scheduler, along with constructs such as AWS Auto Scaling groups in EKS are well equipped to efficiently manage demand on resources, and NFVO should leave it to them to manage in the Kubernetes framework. With Kubernetes, the big, closed control loop has been replaced with multiple small, declarative control loops that gives it the power and flexibility to become a standard in the cloud-native world.

Another complexity is the configuration of VNFs once they are instantiated. Configuration is coupled in ETSI MANO where the VNFM, while instantiating VNF, also takes the responsibility for interacting with the element manager to configure the VNF. Kubernetes doesn’t have built-in mechanisms for application configuration, although with capabilities such as [lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/), [init](https://www.initse.com/ende/home/) containers, [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/), and [Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), you can build an efficient devops way of configuring CNFs during or after CNF instantiation.

 Service function chaining is a higher level of abstraction built on top of individual network and service functions that applies ordering constraints to the packet or flow of packets based on the result of some classification upstream. The networking world relies extensively on service function chaining to fulfill important tasks such as insertion of firewall or deep packet inspection in the path of some flows. The difficulties in defining a good service chaining solution stem from apparently simple but harder to implement requirements, such as being lightweight, allowing for easy debugging, and not adding unnecessary encapsulation overhead while steering traffic to the next service in the chain without packet modification. Some of the services are stateful, which implies that the packet should not only follow the service but also the exact instantiated service function that had served the earlier packet in the flow. These requirements have been hard to implement in the VNF world and also in the Kubernetes world. More research and work are needed to solve service chaining issues in a true intent-driven way.

The last but not least important aspect is service assurance, meaning how the system deals with failures and performance impact. Due to the Kubernetes intent-based framework and its ability to take care of Pod failures, many of the failures and performance issues can be taken care of at the Kubernetes level, and operation support system (OSS) and business support system (BSS) don’t need to have control to recover from those failures. However, you do need a mechanism to track service KPIs from the OSS/BSS perspective. There isn't really a Kubernetes-native standard, but there are some popular standards that have emerged (such as [Prometheus](https://prometheus.io/) and [OpenTelemetry](https://opentelemetry.io/)) that do collect metrics, and on which service KPI solutions can be built. Service assurance itself is a big area of study but we will not go into further details in this paper.

 Next, we’ll examine the impact of orchestration on achieving business and technical requirements of a CSP.
