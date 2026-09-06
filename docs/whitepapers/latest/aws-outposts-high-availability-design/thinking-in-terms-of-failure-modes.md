---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/thinking-in-terms-of-failure-modes.html
---

# Thinking in terms of failure modes
<a name="thinking-in-terms-of-failure-modes"></a>

When designing a highly available application or system you must consider what components might fail, what impact component failures will have on the system as well as your application [RPO/RTO](https://aws.amazon.com/blogs/mt/establishing-rpo-and-rto-targets-for-cloud-applications/) goals, and what mechanisms you can implement to mitigate or eliminate the impact of component failures. Does your application run on a single server, in a single rack, or in a single data center? What will happen when a server, rack, or data center experiences a temporary or permanent failure? What happens when there is a failure in a critical sub-system like networking or within the application itself? These are failure modes.

 You should consider the failure modes in this section when planning your Outposts and application deployments. The sections that follow will review how to mitigate these failure modes to provide an increased level of high availability for your application environment.

## Failure mode 1: Network
<a name="failure-mode-1-network"></a>

 An Outpost deployment depends on a resilient connection to its parent Region for management and monitoring. Network disruptions may be caused by a variety of failures such as operator errors, equipment failures, and service provider outages. An Outpost, which may be comprised of one or more racks connected together at the site, is considered disconnected when it cannot communicate with the Region via the Service Link.

 Redundant network paths can help mitigate the risk of disconnect events. You should map application dependencies and network traffic to understand the impact disconnect events will have on workload operations. Plan sufficient network redundancy to meet your application availability requirements.

 During a disconnect event, instances running on an Outpost continue to run and are accessible from on-premises networks through the Outpost Local Gateway (LGW). Local workloads and services may be impaired or fail if they rely on services in the Region. Mutating requests (like starting or stopping instances on the Outpost), control plane operations, and service telemetry (for example, CloudWatch metrics) will fail while the Outpost is disconnected from the Region. CloudWatch metrics will be spooled locally on your Outpost for short periods of network disconnect, and will be sent to the Region for review when the service link connection is re- established.

## Failure mode 2: Instances
<a name="failure-mode-2-instances"></a>

 Amazon EC2 instances may become impaired or fail if the server they are running on has an issue or if the instance experiences an operating system or application failure. How applications handle these types of failures depends on the application architecture. Monolithic applications typically use application or system features for recovery while modular service oriented or [microservices](https://aws.amazon.com/microservices) architectures typically replace failed components to maintain service availability.

You can replace failed instances with new instances using automated mechanisms like Amazon EC2 Auto Scaling groups. Instance auto recovery can restart instances that fail due to server failures provided there is sufficient spare capacity available on the remaining servers and the service link is still connected.

## Failure mode 3: Compute
<a name="failure-mode-3-compute-and-storage-servers"></a>

 Servers can fail or become impaired and may need to be taken out of operation (temporarily or permanently) for a variety of reasons, such as component failures and scheduled maintenance operations. How services on Outposts rack handle server failures and impairments varies and can depend on how customers configure high availability options.

 You should order sufficient compute capacity to support an `N+M` availability model, where `N` is the required capacity and `M` is the spare capacity provisioned to accommodate server failures.

 Hardware replacements for failed servers are provided as part of the fully managed AWS Outposts rack service. AWS actively monitors the health of all servers and networking devices in an Outpost deployment. If there is a need to perform physical maintenance, AWS will schedule a time to visit your site to replace failed components. Provisioning spare capacity allows you to keep your workloads resilient against host failures while unhealthy servers are taken out of service and replaced.

## Failure mode 4: Racks or data centers
<a name="failure-mode-4-racks-or-data-centers"></a>

 Rack failures may occur due to a total loss of power to racks or due to environmental failures like loss of cooling or physical damage to the data center from a flood or earthquake. Deficiencies in data center power distribution architectures or errors during standard data center power maintenance can result in loss of power to one or more racks or even the entire data center.

 These scenarios can be mitigated by deploying infrastructure to multiple data center floors or locations that are independent from one another within the same campus or metro area.

 Taking this approach with AWS Outposts rack will require careful consideration for how applications are architected and distributed to run across multiple separate logical Outposts to maintain application availability.

## Failure mode 5: AWS Availability Zone or Region
<a name="failure-mode-5-aws-availability-zone-or-region"></a>

 Each Outpost is anchored to a specific Availability Zone (AZ) within an AWS Region. Failures within the anchor AZ or parent Region could cause the loss of Outpost management and mutability and may disrupt network communication between the Outpost and the Region.

 Similar to network failures, AZ or Region failures may cause the Outpost to become disconnected from the Region. The instances running on an Outpost continue to run and are accessible from on-premises networks through the Outpost Local Gateway (LGW) and may be impaired or fail if they rely on services in the Region, as described previously.

 To mitigate the impact of AWS AZ and Region failures, you can deploy multiple Outposts each anchored to a different AZ or Region. You may then design your workload to operate in a distributed multi-Outpost deployment model using many of the similar [mechanisms and architectural patterns](https://docs.aws.amazon.com/whitepapers/latest/fault-tolerant-components/high-availability-building-blocks.html) that you use to design and deploy on AWS today.

The control plane of the services that run on AWS Outposts resides in the Region to which it is anchored, generating a dependency both on Zonal services such as Amazon EC2 and Amazon EBS and on Regional services such as Amazon RDS, Elastic Load Balancing and Amazon EKS. In Outposts, applications can be deployed under the concept of [static stability](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/static-stability.html) to help improve resilience to control plane impairments.
