---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-education-hybrid-multicloud/cloud-bursting.html
---

# Cloud bursting for research computing
<a name="cloud-bursting"></a>

The research computing group at an R1 (Doctoral Universities – Very High Research Activity) research institution in the US had been running on-premises high performance computing (HPC) clusters with the Slurm scheduler for many years. Except for a few weeks of scheduled maintenance, the clusters were running at 80-95 percent utilization rate with most of their queues full.

The increasing number of research activities at the institution introduced capacity and capability challenges. A few high-profile researchers were always performing long-running simulations on certain queues, which increased the wait time for other users. Newly hired faculty needed to run large numbers of weather simulations to build a novel artificial intelligence and machine learning (AI/ML) model for weather forecasting, but they required more capacity than was available. The research computing group was also getting more requests for the latest graphics processing units (GPUs) to train machine learning models. Even with funding for new GPUs, the team would need to wait months to get approval for expanding rack space in the data center.

Many researchers were unwilling to delete old data, so local storage capacity was also a challenge. A more scalable, long-term storage option was needed to free up valuable, high-performance storage on premises.

The cloud addresses these challenges with hybrid compute and storage solutions that let you *burst* research computing into the cloud when on-premises capacity isn't enough. The following architecture diagram illustrates a few compute and storage bursting approaches, using tools such as [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/) and [AWS Storage Gateway](https://aws.amazon.com/storagegateway/)[.](https://aws.amazon.com/hpc/parallelcluster/)

![Architecture for cloud bursting for research computing](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-education-hybrid-multicloud/images/guide-img/72d1214e-0148-413e-9e71-1a181ad4845c/images/22283d97-4eef-4c82-bd6b-03ba484f75e2.png)

This architecture follows these recommendations:
+ **Select a primary, strategic cloud provider. **This architecture uses one primary cloud provider to avoid being restricted by the least common denominator approach. This way, the institution can take advantage of the innovation and native compute and storage services that the primary cloud provider offers. The research computing team can focus on optimizing workloads in the environment provided by the primary cloud provider, not how to work in different cloud environments.
+ **Establish security and governance requirements for each cloud service provider. **Each service and tool used in this architecture can be configured to meet the research computing team's security and governance requirements, including private connectivity, data encryption in transit and at rest, activity logging, and more.
+ **Adopt cloud-native, managed services wherever possible and practical. **This architecture provides the ability to use managed storage and compute services as well as tools to simplify cluster management. This way, the research computing team doesn't have to worry about managing clusters or underlying infrastructure on their own, which can be complex and time-consuming.
+ **Implement hybrid architectures when existing, on-premises investments incentivize continued use. **This architecture allows the institution to continue using its on-premises resources and take advantage of the cloud to increase capacity and expand computing power on demand. With the cloud, the institution can right-size the compute type to maximize price-performance and access the latest technology to promote innovation without a large upfront investment in additional on-premises hardware.
