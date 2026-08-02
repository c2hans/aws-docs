---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/traditional-virtualization-primer.html
---

# Traditional virtualization primer
<a name="traditional-virtualization-primer"></a>

 Virtualization, at a high level, enables a single physical computer system to run multiple operating systems at once. A virtualization system (“host”) implements translation, emulation, and restriction functions that allow it to provide one or more virtualized operating systems (“guest”) with virtual representations of their own self-contained hardware (“virtual machines” or “VMs”). One of the primary benefits of virtualization is the ability to make efficient use of a single powerful server by dividing its resources among multiple virtual machines each of which is allocated an amount of resources which is optimal for its assigned tasks.

**Note**
 The discussion of virtualization in this section provides a generalized high-level introduction to the topic and does not dive into topics such as Paravirtualization, in which guest software must be modified to run in the virtualized environment. For a more detailed primer on virtualization technologies, refer to [this presentation on virtualization technologies](https://www.youtube.com/watch?v=R-n4dDGfQd4) by Anthony Liguori, VP and Distinguished Engineer at AWS.

 The core component responsible for managing the lifecycle and operation of guest virtual machines (VMs) in a virtualization system is called a virtual machine monitor (VMM), or *hypervisor*. For a statistical majority of operations it performs, a guest runs instructions natively on the system’s physical CPU without any involvement by the VMM. For example, when a guest seeks to compute the sum or product of two values, it can communicate directly with the CPU hardware of the system to issue the requisite machine code instructions.

 There are, however, some classes of sensitive or privileged instructions, such as reading or writing from CPU control registers, that a guest should not be allowed to run directly on the CPU hardware to maintain the stability and isolation of the system as a whole. When a guest tries to issue one of these instructions to the CPU, instead of running, the instruction is redirected to the VMM, which emulates a permitted result for the instruction, and then returns control back to the guest as if the instruction had been performed on the CPU natively.

 A VMM itself is a relatively simple piece of software. However, a virtualization host requires more than the core functionality of a VMM to provide guests with access to devices such as network interfaces, storage drives, and input peripherals. To provide these features, hosts rely on additional software components called *device models*. Device models communicate with the system’s shared physical I/O hardware and emulate the state and behavior of one or more unique virtual device interfaces exposed to guest VMs.

 Hypervisors typically employ a general-purpose operating system to interface with a variety of system hardware, run device models, and run other management software for the virtualization system. This operating system is commonly implemented as a special privileged virtual machine which, for example, the [Xen Project calls the system’s dom0](https://wiki.xenproject.org/wiki/Dom0), and [Hyper-V calls the system’s root/parent partition](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/reference/hyper-v-architecture). In early generation EC2 instances, this took the form of a special Amazon Linux VM running as what in Xen terminology is called *domain 0*, or *dom0*.

![A diagram depicting classical virtualization architecture.](http://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/images/virtualization-architecture.png)
