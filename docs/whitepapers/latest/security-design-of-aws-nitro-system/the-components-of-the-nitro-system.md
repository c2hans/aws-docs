---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-components-of-the-nitro-system.html
---

# The components of the Nitro System
<a name="the-components-of-the-nitro-system"></a>

 As noted earlier, the Nitro System consists of three primary components:
+  Purpose-built Nitro Cards
+  The Nitro Security Chip
+  The Nitro Hypervisor

## The Nitro Cards
<a name="the-nitro-cards"></a>

 A modern EC2 server is made up of a main system board and one or more Nitro Cards. The system main board contains the host CPUs ([Intel](https://aws.amazon.com/intel/), [AMD](https://aws.amazon.com/ec2/amd/), or [Graviton](https://aws.amazon.com/ec2/graviton/) processors) and memory. *Nitro Cards* are dedicated hardware components with powerful 64-bit processing capabilities and specialized Application Specific Integrated Circuits (“ASICs”) that operate independently from the system main board that runs all customer compute environments, including code and data processing operations.

 The Nitro Cards implement all the outward-facing control interfaces used by the EC2 service to provision and manage compute, memory, and storage. They also provide all I/O interfaces, such as those needed to provide software-defined networking, Amazon EBS storage, and instance storage. This means that all the components that interact with the outside world of the EC2 service beyond the main system board—whether logically inbound or outbound—run on self-contained computing devices which are physically separate from the system main board on which customer workloads run.

 The Nitro System is designed to provide strong logical isolation between the host components and the Nitro Cards, and this physical isolation between the two provides a firm and reliable boundary which contributes to that design. While logically isolated and physically separate, Nitro Cards typically are contained within the same physical server enclosure as a host’s system main board and share its power supply, along with its [PCIe](https://en.wikipedia.org/wiki/PCI_Express) interface.

**Note**
 In the case of the EC2 mac1.metal and mac2.metal instances. A Nitro Controller is colocated with a Mac Mini in a common metal enclosure, and the two are connected together with Thunderbolt. Refer to [Amazon EC2 Mac Instances](https://aws.amazon.com/ec2/instance-types/mac/).

 The main components of the Nitro Cards are AWS-designed System on a Chip (SoC) package that run purpose-built firmware. AWS has carefully driven the design and implementation process of the hardware and firmware of these cards. The hardware is designed from the ground up by Annapurna Labs, the team responsible for the AWS in-house silicon designs. The firmware for these cards is developed and maintained by dedicated AWS engineering teams.

**Note**
Annapurna Labs was acquired by Amazon in 2015 after a successful partnership in the initial phases of the development of key AWS Nitro System technologies. Annapurna is responsible not only for making AWS Nitro System hardware, but also for the AWS custom Arm-based Graviton processors, the [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) and [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) hardware accelerator chips for ML training and inference, [AWS Nitro SSD](https://aws.amazon.com/blogs/aws/aws-nitro-ssd-high-performance-storage-for-your-i-o-intensive-applications/), and [Aqua](https://aws.amazon.com/blogs/aws/new-aqua-advanced-query-accelerator-for-amazon-redshift/) (advanced query accelerator) for [Amazon Redshift](https://aws.amazon.com/redshift/).

 The critical control firmware on the Nitro Cards can be live-updated, using cryptographically signed software packages. Nitro Cards can be updated independently of other components of the Nitro System, including of one another and of any updateable components on the system main board in order to deploy new features and security updates. Nitro Cards update with nearly imperceptible impact on customer workloads and without the relaxing of any of the security controls of the Nitro System.

 The Nitro Cards are physically connected to the system main board and its processors via PCIe, but are otherwise logically isolated from the system main board that runs customer workloads. A Nitro System can contain one or more Nitro Cards; if there is more than one, they are connected through an internal network within a server enclosure. This network provides a private communication channel between Nitro Cards that is independent of the system mainboard, as well as a private connection to the Baseboard Management Controller (BMC), if one is present in the server design.

### The Nitro Controller
<a name="the-nitro-controller"></a>

 The primary Nitro Card is called the Nitro Controller. The Nitro Controller provides the hardware root of trust for the overall system. It is responsible for managing all other components of the server system, including the firmware loaded onto the other components of the system. Firmware for the system as a whole is stored on an encrypted solid state drive (SSD) that is attached directly to the Nitro Controller. The encryption key for the SSD is designed to be protected by the combination of a Trusted Platform Module (TPM) and the secure boot features of the SoC. This section describes the secure boot design for the Nitro Controller as implemented in the most recent versions of the hardware and its role as the trusted interface between a server and the network.

**Note**
In the case of AWS Outpost deployments, a Nitro Security Key is also used along with a TPM and the secure boot features of the SoC to protect the encryption key for the SSD, which is connected directly to the Nitro Controller.

#### The Nitro Controller secure boot design
<a name="the-nitro-controller-secure-boot-design"></a>

 The secure boot process of the SoC in the Nitro Controller starts with its boot ROM and then extends a chain of trust by measuring and verifying early stages firmware stored in flash attached to the Nitro Controller. As the system initialization progresses, a [trusted platform module](https://trustedcomputinggroup.org/resource/trusted-platform-module-tpm-summary/) (TPM) is used to record the initial boot code measurements, and then to extend measurements to additional system firmware. The cryptographic keys embedded in the tamper-resistant TPM are used to digitally sign the complete set of known good system measurements. This digitally signed file is then compared to all subsequent system measurements at each reboot to detect any unexpected changes.

 If no changes are detected, additional decryption keys encrypted by keys locked in the TPM are used to decrypt additional data in the system to allow the boot process to continue. If changes are detected, the additional data is not decrypted and the system is immediately removed from service and will therefore not host customer workloads.

 The preceding steps detail the process by which the Nitro Controller establishes the integrity and validity of system software on boot. For secure boot design to be truly secure, each stage of SoC boot code must not only be valid and unmodified, but also functionally correct as implemented. This is especially true of the static ROM code that is a part of the physical manufacturing of the device. To that end, AWS has [applied formal methods](https://link.springer.com/chapter/10.1007/978-3-319-96142-2_28) to verify the memory safety properties of early-stage boot code in our designs.

#### The Nitro Controller as interface between EC2 servers and the network
<a name="the-nitro-controller-as-interface-between-ec2-servers-and-the-network"></a>

 The Nitro Controller is the exclusive gateway between the physical server and the control planes for EC2, Amazon EBS, and [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC). While logically distinct, and composed of multiple sub-component microservices, these three control planes are hereafter generally referred to as the *EC2 control plane*.

**Note**
Within AWS, a common design pattern is to split a system into services that are responsible for processing customer requests (the data plane), and services that are responsible for managing and vending customer configuration by, for example, creating, deleting and modifying resources (the control plane). Amazon EC2 is an example of an architecture that includes a data plane and a control plane. The data plane consists of EC2 physical servers where customers’ EC2 instances run. The control plane consists of a number of services responsible for communicating with the data plane, and performing functions such as relaying commands to launch or terminate an instance or ingesting operational telemetry.

![A diagram depicting Nitro System control architecture.](http://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/images/control-architecture.png)

 The Nitro Controller presents to the dedicated EC2 control plane network a set of strongly authenticated and encrypted networked APIs for system management. Every API action is logged and all attempts to call an API are cryptographically authenticated and authorized using a fine-grained access control model. Each control plane component is authorized only for the set of operations needed for it to complete its business purpose. Using formal methods, we've proven that the network-facing API of the control message parsing implementation of the Nitro Controller is free from memory safety errors in the face of any configuration file and any network input.

### Nitro Cards for I/O
<a name="nitro-cards-for-io"></a>

 In addition to the Nitro Controller, some systems use additional specialized Nitro Cards to perform specific functions. These subordinate Nitro Cards share the same SoC and base firmware designs as the Nitro Controller. These Nitro Cards are designed with additional hardware and specialized firmware applications as required for their specific functions. These include, for example, the Nitro Card for VPC, the Nitro Card for EBS, and the Nitro Card for Local [NVMe](https://en.wikipedia.org/wiki/NVM_Express) Storage.

 These cards implement data encryption for networking and storage using hardware offload engines with secure key storage integrated in the SoC. These hardware engines provide encryption of both local NVMe storage and remote EBS volumes without practical impact on their performance. The last three versions of the Nitro Card for VPC, including those used on all newly released instance types, transparently encrypt all VPC traffic to other EC2 instances running on hosts also equipped with encryption-compatible Nitro Cards, without performance impact.

**Note**
 AWS provides [secure and private connectivity](https://d1.awsstatic.com/whitepapers/compliance/AWS_Logical_Separation_Handbook.pdf#%5B%7B%22num%22%3A25%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C69%2C708%2C0%5D) between EC2 instances of all types. In addition, some instance types use the offload capabilities of the underlying Nitro System hardware to automatically and transparently encrypt and anonymize in-transit traffic between instances, using AES-256-GCM. There is no impact on network performance. To support this additional in-transit traffic encryption between instances the instances must be supported instance types, in the same Region, and in the same VPC or peered VPCs. The traffic must not pass through a virtual network device or service such as a load balancer or transit gateway. For additional information and a list of supported instance types, refer to [Encryption in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit).

 The encryption keys used for EBS, local instance storage, and for VPC networking are only ever present in plaintext in the protected volatile memory of the Nitro Cards; they are inaccessible to both AWS operators as well as any customer code running on the host system’s main processors. Nitro Cards provide hardware programming interfaces over the PCIe connection to the main server processor—NVMe for block storage (EBS and instance store), Elastic Network Adapter (ENA) for networking, a serial port for out-of-band OS console logging and debugging, and so on.

**Note**
EC2 provides customers with access to [instance console output](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html#instance-console-console-output) for troubleshooting. The Nitro System also enables customers to connect to a [serial console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html) session for interactive troubleshooting of boot, network configuration, and other issues. “Out-of-band” in this context refers to the ability for customers to obtain information or interact with their instances through a channel which is separate from the instance itself or its network connection.

 When a system is configured to use the Nitro Hypervisor, each PCIe function provided by a Nitro Card is sub-divided into virtual functions using single-root input/output virtualization (SR-IOV) technology. This facilitates assignment of hardware interfaces directly to VMs. Customer data (content that customers transfer to us for processing, storage, or hosting) moves directly between instances and these virtualized I/O devices provided by the Nitro Cards. This minimizes the set of software and hardware components involved in the I/O, resulting in lower costs, higher performance, and greater security.

## The Nitro Security Chip
<a name="the-nitro-security-chip"></a>

 The Nitro Controller and other Nitro Cards together operate as one domain in a Nitro System and the system main board with its Intel, AMD, or Graviton processors, on which customer workloads run makes up the second. While the Nitro Controller and its secure boot process provide the hardware root of trust in a Nitro System, an additional component is used to extend that trust and control over the system main board. The Nitro Security Chip is the link between those two domains that extends the control of the Nitro Controller to the system main board, making it a subordinate component of the system, thus extending the Nitro Controller chain of trust to cover it. The following sections detail how the Nitro Controller and Nitro Security Chip function together to achieve this goal.

### The Nitro Security Chip protection of system hardware
<a name="the-nitro-security-chip-protection-of-system-hardware"></a>

 The Nitro Security Chip is a device integrated into the server’s system main board. At runtime, it intercepts and moderates all operations to local non-volatile storage devices and low speed system management bus interfaces (such as Serial Peripheral Interface (SPI) and [I2C](https://en.wikipedia.org/wiki/I%C2%B2C))—in other words, to all firmware.

 The Nitro Security Chip is also situated between the BMC and the main system CPU on its high-speed PCI connection, which enables this interface to be logically firewalled on production systems. The Nitro Security Chip is controlled by the Nitro Controller. The Nitro Controller, through its control of the Nitro Security Chip, is therefore able to mediate and validate updates to the firmware, or programing of other non-volatile devices, on the system mainboard or Nitro Cards of a system.

 A common industry practice is to rely on a hypervisor to protect these system hardware assets, but when no hypervisor is present—such as when EC2 is used in bare metal mode—an alternative mechanism is required to ensure that users cannot manipulate system firmware. The Nitro Security Chip provides the critical security function of ensuring that the main system CPUs cannot update firmware in bare metal mode. Moreover, when the Nitro System is running with the Nitro Hypervisor, the Nitro Security Chip also provides defense in depth in addition to the protections for system hardware assets provided by the hypervisor.

### The Nitro Security Chip at system boot or reset
<a name="the-nitro-security-chip-at-system-boot-or-reset"></a>

 The Nitro Security Chip also provides a second critical security function during system boot or reset. It controls the physical reset pins of the server system main board, including its CPUs and the BMC, if present. This enables the Nitro Controller to complete its own secure boot process, then verify the integrity of the basic input/output system (BIOS), BMC, and all other system firmware before instructing the Nitro Security Chip to release the main CPUs and BMC from being held in reset. Only then can the CPUs and BMC begin their boot process using the BIOS and firmware that have just been validated by the Nitro Controller.

## The Nitro Hypervisor
<a name="the-nitro-hypervisor"></a>

 The Nitro Hypervisor is a limited and carefully designed component that has been intentionally minimized and purpose built with the capabilities needed to perform its assigned functions, and no more. The Nitro Hypervisor is designed to receive virtual machine management commands (start, stop, and so on) sent from the Nitro Controller, to partition memory and CPU resources by utilizing hardware virtualization features of the server processor, and to assign [SR-IOV](https://en.wikipedia.org/wiki/Single-root_input/output_virtualization) virtual functions provided by Nitro hardware interfaces (NVMe block storage for EBS and instance storage, Elastic Network Adapter (ENA) for network, and so on) through PCIe to the appropriate VM.

**Note**
 While the Nitro architecture is unique in that it does not require the use of a hypervisor to provide software-defined infrastructure, in most customer scenarios, virtualization is valuable because it allows very large servers to be subdivided for simultaneous use as multiple instances (VMs) as well as other advantages such as faster provisioning. Hypervisors are required in virtualized configurations to provide isolation, scheduling, and management of the guests and the system. Therefore, the Nitro Hypervisor plays a critical role in securing a Nitro-based EC2 server in those common scenarios.

 Some instance types built on the Nitro System include hardware accelerators, both built by AWS and by third parties (such as graphics processing units, or GPUs). The Nitro Hypervisor is also responsible for assigning these hardware devices to VM, recovering from hardware errors, and performing other functions that cannot be performed through an out-of-band management interface.

 Within the Nitro Hypervisor, there is, by design, no networking stack, no general-purpose file system implementations, and no peripheral device driver support. The Nitro Hypervisor has been designed to include only those services and features which are strictly necessary for its task; it is not a general-purpose system and includes neither a shell nor any type of interactive access mode. The small size and relative simplicity of the Nitro Hypervisor is itself a significant security benefit compared to conventional hypervisors.

 The Nitro Hypervisor code is a managed, cryptographically signed firmware-like component stored on the encrypted local storage attached to the Nitro Controller, and is therefore chained to the hardware root of trust of the Nitro Controller. When a system is configured to use the Nitro Hypervisor, the Nitro Controller directly loads a known-good copy of the hypervisor code onto the system main board in a manner similar to firmware.

**Note**
 The mechanism for this hypervisor injection process is the use of a read-only NVMe device provided by the Nitro Controller to the main board as the system *boot drive.*

 Offloading data processing and I/O virtualization to discrete hardware, and reducing the set of responsibilities of the hypervisor running on the host CPU, is central to the Nitro System design. It not only provides improved performance and stronger security through isolation, it also enables the bare metal instance type feature of EC2 because the hypervisor is now an optional discrete component that is no longer needed in order to provide I/O virtualization, system management, or monitoring.

**Note**
 The Nitro System enables what is effectively “bare metal” performance by running nearly all the functionality of the virtualization system on the Nitro cards rather than on the host’s system mainboard CPUs. Refer to [Bare metal performance with the AWS Nitro System](https://aws.amazon.com/blogs/hpc/bare-metal-performance-with-the-aws-nitro-system/).

 The meticulous exclusion of non-essential features from the Nitro Hypervisor eliminates entire classes of bugs that other hypervisors can suffer from, such as remote networking attacks or driver-based privilege escalations. Even in the unlikely event of a bug being present in the Nitro Hypervisor that allows access to privileged code, it still presents an inhospitable environment to any potential attacker due to the lack of standard operating system features such as interactive shells, filesystems, common user space utilities, or access to resources that could facilitate lateral movement within the larger infrastructure.

 For example, as previously noted, the Nitro Hypervisor has no networking stack and no access to the EC2 network. Instead, the Nitro Controller and other Nitro Cards mediate all access of any kind to the outside network, whether the main server processor is running the Nitro Hypervisor or running in bare metal mode. Moreover, as discussed in detail next, the passive communications design of Nitro means any attempted “outreach” from code running in the context of the hypervisor to the Nitro Cards will be denied and alarmed.

### Update process for the Nitro Hypervisor
<a name="update-process-for-the-nitro-hypervisor"></a>

 A crucial aspect of maintaining system security is routine updates. The Nitro Hypervisor allows for full system live update. When a new version of the Nitro Hypervisor is available, the full running hypervisor code is replaced in-place while preserving customer EC2 instances with near-imperceptible performance impact to those instances. These update processes are designed such that at no time do any of the security protocols or defenses of the Nitro System need to be dropped or relaxed. This overall live update capability is designed to provide zero downtime for customers’ instances, while ensuring that not only new features but also security updates can be applied regularly and rapidly.

The decoupling of customer instance downtime from Nitro System component updates eliminates the need for the EC2 service to carefully balance tradeoffs between customer experience and potential security impact when planning system updates, thereby yielding improved security outcomes.
