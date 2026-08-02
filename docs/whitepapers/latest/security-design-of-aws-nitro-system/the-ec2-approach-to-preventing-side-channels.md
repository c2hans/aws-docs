---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-ec2-approach-to-preventing-side-channels.html
---

# The EC2 approach to preventing side-channels
<a name="the-ec2-approach-to-preventing-side-channels"></a>

 Since its inception, EC2 has consistently taken a conservative approach to designing and operating secure multi-tenant systems for our customers. Our design approach favors simple and reliable abstractions, which provide strong isolation between security domains and limit the sharing of critical system resources across customers. AWS designs our systems to not only provide defense-in-depth against known security threats, but also to avoid impact from classes of potential security issues which do not have known practical exploitation techniques. In addition to the thoroughly tested and well-established security mechanisms we employ in production, AWS is actively engaged with the cutting edge of security research to ensure that we remain not only up-to-date, but are actively looking around corners for security issues on behalf of our customers.

 Research and disclosures in the area of CPU-based side-channels published over the past few years have brought concerns around this topic to the forefront. Side channels are mechanisms that potentially allow revealing secret information in a computer system through the analysis of indirect data gathered from that system. An example of such indirect data may be the amount of time it takes for a system to operate on an input. In some cases, although a system never directly reveals a secret piece of data, an external party may be able to determine the value of that secret through precise analysis of differences in time taken to process specially selected inputs.

**Note**
 A simple example of such a scenario would be a program which receives a password in the form of a string as an input and validates whether that string matches the secret value. This program analyses the provided string one character at a time comparing each character to the corresponding character of the secret and returns an error as soon as it encounters a mismatch. Although the program never provides the requester with the value of the secret, the program “leaks” information about the secret in the form of a different response time for an input that starts with one or more of the same characters as the secret as for one which does not. Through a process of systematic trial and error an observer may be able to measure the time taken to respond to certain inputs in order to determine the value of the secret one character at a time.

 Careful deployment of countermeasures such as those employed by [s2n-tls](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/), the open-source SSL/TLS implementation from AWS, can be used to protect against these forms of side-channel data disclosure.

**Note**
 s2n-tls incorporates and proves using formal methods time-balancing countermeasures to ensure that process timing is negligibly influenced by secrets, and therefore no attacker-observable timing behavior depends on secrets. For more on these countermeasures in s2n-tls and the formal proof of those countermeasures, refer to [SideTrail: Verifying Time-Balancing of Cryptosystems](https://d1.awsstatic.com/Security/pdfs/SideTrail_Verifying_Time_Balancing_of_Cryptosystems.pdf).

 CPU-based [side-channels](https://en.wikipedia.org/wiki/Side-channel_attack) specifically involve the manipulation of the low-level behavior of a system’s processor in certain circumstances, to allow one process running on that system to indirectly ascertain the value of secret data through system resources such as caches, internal buffers, and other stateful data sources which it is not permitted to access directly. Critically, these side-channels center around the sharing of access to low-level hardware resources between two systems.

 AWS has a conservative approach to EC2 tenant-isolation, discussed in the sections that follow, that is designed so that customer instances can never share system resources such as L1/L2 cache or threads running on the same CPU complex. This fundamental design choice rules out the possibility of data leakage from customer instances through CPU-based side-channels which are predicated upon shared access to these resources among tenants.

## Side-channel protections in the broader EC2 service
<a name="side-channel-protections-in-the-broader-ec2-service"></a>

 All EC2 instances include robust protections against side-channels. This includes both instances based on the Nitro System or on the Xen hypervisor. While this section discusses these protections in terms of the Nitro System, these protections are also present in Xen-based EC2 instances.

 Virtualized EC2 instance types fall into two categories:
+  **Fixed performance instances**, in which CPU and memory resources are pre-allocated and dedicated to a virtualized instance for the lifetime of that instance on the host and
+  **Burstable performance instances**, in which CPU and memory resources can be overcommitted in order to support larger numbers of virtualized instances running on a server and in turn offer customers a reduced relative instance cost for applications with low-to-moderate CPU utilization. Refer to [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html).

 In either case, the design and implementation of the Nitro Hypervisor includes multiple protections for potential side channels.

 For fixed performance instances, dedicating resources provides both natural protection against side channels and higher performance compared to other hypervisors. For example, a c5.4xlarge instance is allocated 16 virtual CPUs (eight cores, with each core providing two threads) along with 32 GiB of memory. When an instance is launched, the EC2 control plane instructs the Nitro Controller to allocate the necessary CPU, memory, and I/O resources to support the instance.

 The Nitro Hypervisor is directed by the Nitro Controller to allocate the full complement of physical cores and memory for the instance. These hardware resources are “pinned” to that particular instance. The CPU cores are not used to run other customer workloads, nor are any instance memory pages shared in any fashion across instances— unlike many hypervisors that can consolidate duplicated data and/or instruction pages to conserve physical memory.

Even on small instances, CPU cores are never simultaneously shared among customers via Simultaneous Multi-Threading (SMT). Instances are provided with multiples of either two vCPUs, when the underlying hardware uses SMT, or one vCPU when the underlying hardware does not use SMT (for example, with AWS Graviton and HPC instance types). No sharing of CPU cores means that instances never share CPU core-specific resources, including Level 1 or Level 2 caches. The A1 instance type is a unique exception where the Level 2 cache is not a CPU core-specific resource since it is the Last-Level Cache (LLC) and it is shared amongst instances.

**Note**
Some instance sizes can share some last level cache lines non-simultaneously. EC2 Nitro accurately exposes the underlying CPU topology of the hardware, including last-level (typically L3) cache and non-uniform memory access (NUMA) information, directly through to instances. It is therefore possible for customers to determine by inspection what size instance is allocated the number of CPU cores needed to “fill” exactly one or more of the CPU segments which share an L3 cache; thereby determining whether or not a given instance shares any L3 cache with another instance. L3 cache sharing topologies differ between CPU designs, and may be shared across a core, CPU complex, or Core complex die depending on the processor architecture. For example, in a typical two-socket Intel-based EC2 system, an instance size that is one-half the largest size will fill a CPU core and will not share the L3 cache with another instance

Most CPU side-channel attacks to date have relied on sharing CPU cores via SMT and targeted the L1 caches, which are never shared among instances. Other microarchitectural data disclosures have also relied on sharing CPU cores via SMT or the ability to frequently reschedule and sample data within a single core. Within EC2 Nitro, instances are allocated to dedicated cores for the lifetime of the instance except on burstable instance types where microarchitectural state is flushed when the core is rescheduled.

 As previously mentioned, burstable performance EC2 instances (for example, T3, T3a, and T4g) can utilize overcommitted CPU and memory resources. The CPU resources needed to run burstable performance instances are scheduled according to a credit-based allocation. In that low cost but relatively high-performance family of instances, even the smallest instance types still provide customers with a minimum of two vCPUs (one core, two threads) on processors that utilize SMT.

 It is possible, however, for two burstable performance EC2 instances to run *sequentially* (not simultaneously) on the same core. It is also possible for physical memory pages to be reused, remapped, and swapped in and out as virtual memory pages. However, even burstable instances never share the same core at the same time, and virtual memory pages are never shared across instances.

 The Nitro Hypervisor utilizes a number of safety strategies at each context switch between instances to ensure that all state from the previous instance is removed prior to running another instance on the same core(s). This practice provides strong mitigation against possible side-channel attacks.

 For burstable performance EC2 instances, the Nitro System may employ memory management techniques such as reusing, remapping or swapping physical memory out as virtual memory pages but the system is designed so that virtual memory pages are never shared across instances in the interest of maintaining a strong isolation boundary.

 Finally, burstable performance instances––whether those being targeted or those seeking to detect data through side-channel techniques––may be rescheduled on different cores than previously used, further limiting the possibility of any kind of successful timing-based security issue.

## Additional side-channel benefits of the Nitro System
<a name="additional-side-channel-benefits-of-the-nitro-system"></a>

 In addition to the protections provided by EC2 for both Xen and Nitro, there are some non-obvious but very important benefits in the design of the Nitro System and the Nitro Hypervisor when it comes to side-channel concerns. While, for example, some hypervisors required extensive changes to implement address space isolation as part of the mitigations for the L1 Terminal Fault transient execution side channel attack (for example, refer to [Hyper-V HyperClear Mitigation for L1 Terminal Fault](https://techcommunity.microsoft.com/t5/virtualization/hyper-v-hyperclear-mitigation-for-l1-terminal-fault/ba-p/382429)), the design and implementation of the Nitro System provided natural immunity, because the Nitro Hypervisor’s virtual address space is isolated from memory allocated to customer instances.

 We have also applied what we learned from designing the Nitro System to mitigate emerging threats of CPU-based side channel attacks in the community version of the Xen hypervisor. Refer to [Running Xen Without a Direct Map](https://youtu.be/RKJOwIkCnB4).

 As discussed previously, the Nitro System dramatically decreases the amount of EC2 system code running on the main server processor itself which dramatically narrows the attack surface of the hypervisor and isolates customer I/O data processing from the rest of the system. The AWS code needed to provide the software-defined I/O features of EC2 does not run on the same processors that run customer workloads.

 This compartmentalization and use of dedicated hardware means that customer data processing in I/O subsystems is isolated at the hardware function level, and does not reside in host memory, processor caches, or other internal buffers—unlike general-purpose virtualization software that does mix this data as a side effect of running on the shared host CPUs.

 Underpinning all of these protections is that AWS is at the fore-front of security research and often leads the research and discovery of industry-impacting issues as well as the mitigation and coordination of issues.

## Nitro Enclaves
<a name="nitro-enclaves"></a>

 Nitro Enclaves is a feature of the Nitro System that allows customers to divide their workloads into separate components that need not fully trust each other, as well as a means by which to run highly trusted code and process data to which the customer’s EC2 instance administrators have no access. Its features and benefits are not covered in this paper, but the following is worth noting in this context.

 A Nitro Enclave inherits the same isolation and side-channel mitigations as every other EC2 instance running on the same server processor. The parent instance must allocate a fixed number of vCPUs (the minimum amount equaling one full core) as well as a fixed number of memory pages. That fixed set of CPU and memory resources are subtracted from the parent instance (using the “hot-unplug of hardware resources” feature supported in both Linux and Windows kernels) and then utilized by the Nitro Hypervisor to create another fully protected independent VM environment in which to run the Nitro Enclave image.

 All of the protections discussed above are automatically in place when using Nitro Enclaves since there is no core or memory sharing with the parent instance.

## Closing thoughts on side channels
<a name="closing-thoughts-on-side-channels"></a>

 In summary, careful design decisions in Nitro and the EC2 platform provide a number of very strong mitigations against the possibility of practical side-channel attacks, including removing shared access between instances to the CPU and memory resources which these attacks require. Additionally, customers can optionally choose not to have their instances provisioned on the same hosts as instances belonging to other customers. Moreover, should any future research uncover new challenges, AWS participation in coordinated vulnerability response groups for Linux, KVM, Xen, and other key technologies as well as the Nitro System’s live-update technologies design will allow AWS to react quickly to protect customers from new threats that emerge without disrupting customer workloads. AWS was a member of the small group of companies that worked on [Spectre](https://spectreattack.com/spectre.pdf) and [Meltdown](https://meltdownattack.com/meltdown.pdf) prior to public disclosure, and mitigated all risks in its infrastructure before the public disclosure.

**Note**
 Customers may opt out of sharing compute hardware with other customers by using either the “Dedicated Instances” or the “Dedicated Hosts” features of EC2. These features represent instance placement strategies that result in a single customer being the only customer at any given time with instances scheduled on a particular EC2 physical host. Refer to [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/).

 We continue to work with key partners such as Intel, AMD, and [ARM](https://www.arm.com/) on hardware security research and coordinated vulnerability response and continue to raise the bar with additional innovation for compute isolation. One such example is the open-source Firecracker VMM, which enables serverless container and function-based services such as [AWS Fargate](https://aws.amazon.com/fargate/) and [AWS Lambda](https://aws.amazon.com/lambda/) to benefit from the security, isolation, and consistency of virtualization without compromise on the speed, flexibility, and performance that customers require for these workloads.

**Note**
 [Firecracker](https://firecracker-microvm.github.io/) is a virtualization technology that is purpose-built for creating and managing secure multi-tenant container and function-based services. Firecracker is a virtual machine monitor which manages workloads in lightweight microVMs. It implements a minimal device model that excludes all non-essential functionality and reduces the attack surface area of the microVM. In addition to the security and isolation-optimizations it employs, Firecracker also enables fast boot times—initiating user space or application code in as little as 125ms---and providing a low memory overhead of as little as 5 MiB per microVM.

 Side channel issues are a constantly evolving area of research and resulting innovation and mitigation. We believe that relying on AWS with its deep expertise and continuing focus on this topic is a good place for customers to place their bets when it comes to protection from future risks.

**Note**
 Refer to this [presentation on side channel issues](https://youtu.be/kQ4H6XO-iao) by Eric Brandwine, VP and Distinguished Engineer at AWS. In the presentation he talks about the transition from Xen to Nitro (at 42.40) and the resulting advantages, but also importantly concludes by pointing out that this topic has become one like cryptography, where the most reasonable approach is to rely on deep experts and re-use their work (at 49.29).
