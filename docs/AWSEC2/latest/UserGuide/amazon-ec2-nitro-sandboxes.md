---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nitro-sandboxes.html
---

# Isolate workloads with AWS Nitro Sandboxes
<a name="amazon-ec2-nitro-sandboxes"></a>

An *AWS Nitro Sandbox* is a lightweight virtual machine, or child VM, that you can run alongside your workload on almost any Amazon EC2 instance. Nitro Sandboxes are built on the same AWS Nitro technology that isolates every Amazon EC2 instance. You don't rely on the guest operating system to hold the boundary. Instead, you trust Nitro, a minimized hypervisor that AWS maintains and patches. Nitro isolates each Nitro Sandbox from the parent instance, from other Nitro Sandboxes, and from AWS operators. As a result, you can isolate a workload even from your own operators, meaning the people and software that administer the parent instance. The parent contributes vCPU and memory. Nitro keeps the workload isolated and can attest to the code it runs.

Nitro Sandboxes build on the same foundations as AWS Nitro Enclaves, but they provide the parent instance with mechanisms to implement a wide variety of virtual hardware, such as virtual network and virtual block devices. The parent instance can use them to proxy Elastic Network Adapter (ENA) interfaces or Amazon EBS volumes into the Nitro Sandbox. As a result, a Nitro Sandbox can use ordinary networking and block storage. Standard virtual machine monitors (VMMs) manage it from the parent instance. Nitro Sandboxes run on Intel, AMD, and AWS Graviton processors.

Nitro Sandboxes suit a wide range of workloads that share an Amazon EC2 instance and need their own virtual machine boundary, such as agentic workloads that run untrusted code, multi-tenant containers, Kubernetes pods, and Amazon ECS tasks. You should use [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html) for small, tightly scoped jobs, because an enclave connects to its parent instance through a single local vsock channel that keeps the exposed surface small. [Nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) is best for workloads that must run their own hypervisor, like Windows Subsystem for Linux, and you want full control of that hypervisor. If you want to run workloads that stay isolated between tenants, and don't want to manage servers or networking, use [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-microvms-guide.html) to offload your infrastructure management. For guidance on choosing Nitro Sandboxes for a given workload, see [When to use Nitro Sandboxes](#nitro-sandboxes-when-to-use) below.

**Topics**
+ [How it works](#nitro-sandboxes-how-it-works)
+ [Confidential and direct modes](#nitro-sandboxes-modes)
+ [Supported features](#nitro-sandboxes-features)
+ [When to use Nitro Sandboxes](#nitro-sandboxes-when-to-use)
+ [Run a Nitro Sandbox on an Amazon EC2 instance](#nitro-sandboxes-run-on-ec2)
+ [Launch, resize, and attach storage to a Nitro Sandbox](#nitro-sandboxes-launch-size-storage)
+ [Considerations and limitations](#nitro-sandboxes-considerations)

## How it works
<a name="nitro-sandboxes-how-it-works"></a>

A Nitro Sandbox runs as a first-level, hardware-virtualized guest alongside your instance. The parent instance provides the Nitro Sandbox with vCPU, memory, and I/O, while the Nitro System enforces the isolation boundary and provides cryptographic attestation. Nitro Sandboxes are isolated from each other and from the parent instance. No matter what runs inside a Nitro Sandbox, it can't access another Nitro Sandbox or the parent.

You select a mode (confidential or direct) and a VMM when you create a Nitro Sandbox. For the difference between the modes, see [Confidential and direct modes](#nitro-sandboxes-modes). For the VMM options and how Firecracker drives a Nitro Sandbox, see [How Firecracker works](#nitro-sandboxes-firecracker).

## Confidential and direct modes
<a name="nitro-sandboxes-modes"></a>

Every Nitro Sandbox runs in one of two modes. You choose the mode when you create a Nitro Sandbox, and you can't change it while the Nitro Sandbox is running:

Confidential mode (default)
The Nitro System moves the Nitro Sandbox's memory out of the parent instance, so the parent can't read it, and the Nitro Sandbox can produce an attestation of the code it is running. The Nitro Sandbox includes a Nitro Security Module (NSM) for attestation, and virtio device queues use dedicated shared memory regions so that devices work without exposing the rest of guest memory. Use confidential mode for any workload that processes secrets, including protection from your own operators.
In confidential mode, a workload can prove that it is running unmodified code before it receives secrets. You verify this attestation with an external service, commonly AWS KMS, by adding a condition to an AWS KMS key policy so that the service releases secrets only to a Nitro Sandbox whose measurements match the values you expect.

Direct mode
The parent shares the Nitro Sandbox's memory instead of taking exclusive ownership of it. There is no attestation, and the parent retains access to the Nitro Sandbox's memory. Direct mode is simpler and offers higher I/O throughput, although it is not confidential. Its trust model is equivalent to a standard nested virtual machine. Use direct mode when the Nitro Sandbox and the parent are operated by the same trusted party.

## Supported features
<a name="nitro-sandboxes-features"></a>

A Nitro Sandbox presents a standard virtio-pci device model to the guest, so your workload runs without sandbox-specific code. The following features are available in a Nitro Sandbox:

Block storage
Attach block devices (virtio-blk) backed by local instance store or Amazon EBS. You can resize a block device while the Nitro Sandbox is running. A block device attaches to only one Nitro Sandbox at a time.

Networking
Attach network interfaces (virtio-net) for VPC connectivity, and reach instance metadata through the instance metadata service. Each Nitro Sandbox has its own isolated network stack and can't share the parent instance's network namespace.

Host communication
Use a vsock channel (virtio-vsock) between the Nitro Sandbox and the parent, for example to relay attestation traffic.

Entropy
Attach an entropy device (virtio-rng) in direct mode. Confidential mode doesn't support the entropy device. The guest uses its own entropy sources instead.

Device hot plug
Add block and network virtio devices to a running Nitro Sandbox when you enable hot plug. The devices that you hot plug count toward the instance's device limit. You can't hot-unplug a device.

## When to use Nitro Sandboxes
<a name="nitro-sandboxes-when-to-use"></a>

Use a Nitro Sandbox when you need a boundary as strong as a virtual machine around a container-scale workload, but you don't want the cost of a separate Amazon EC2 instance for each workload or the overhead of nested virtualization. Common use cases include:
+ **Enhanced container isolation** – Make each pod or task a hard security boundary in multi-tenant clusters, while still packing many workloads onto each instance.
+ **Attested containers** – Let regulated workloads or third-party models prove their isolation and integrity before they receive secrets.
+ **Attested virtual machine workloads** – Use a Nitro Sandbox as an alternative to nested virtualization for lightweight virtual machines. It is available on all instance types that support Nitro Sandboxes and provides higher performance together with hardware-backed attestation.
+ **Isolation from your own operators** – Run a workload so that neither the parent instance nor your own operators can read its memory or data.
+ **Secret isolation** – Isolate secrets and sensitive logic from a larger application, so that a compromise of the application doesn't expose them.
+ **Agentic workloads** – Sandbox AI agents that generate and run untrusted code, giving each agent session a hardware-isolated boundary.

**Note**
You can use Nitro Sandboxes directly on Amazon EC2, or through a managed container service. If you run containers on Amazon EKS or Amazon ECS, then Amazon EKS and Amazon ECS provisions and attests a Nitro Sandbox for each pod or task for you. For more information, see [Sandboxing](https://docs.aws.amazon.com/eks/latest/userguide/sandboxing.html) in the *Amazon EKS User Guide* and [Isolated and confidential tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/isolated-confidential-tasks.html) in the *Amazon ECS Developer Guide*. The rest of this topic describes the self-managed experience, in which your own orchestrator drives Nitro Sandboxes directly on Amazon EC2.

## Run a Nitro Sandbox on an Amazon EC2 instance
<a name="nitro-sandboxes-run-on-ec2"></a>

You can use Nitro Sandboxes as a building block for Amazon EC2 workloads. The managed container integrations for Amazon EKS and Amazon ECS are layers built on top of this primitive. If you run your own orchestrator, it performs the same role that a managed service otherwise would: On each instance it launches Nitro Sandboxes, connects their I/O, accounts for the resources they consume, and relays attestation. The self-managed workflow has the following main steps.

**To run a workload in a self-managed Nitro Sandbox**

1. **Launch a supported instance and enable the feature.** Launch an instance type that supports AWS Nitro Enclaves, and enable it with the same instance option that enables Nitro Enclaves. For the instance launch parameters, see the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command.

1. **Build a guest image for your workload.** The image declares the capabilities it requires, such as the devices to attach and whether Nitro Sandboxes share CPU. These settings are part of the signed image and must match what you request at launch, which is what keeps attestation meaningful.

1. **Launch the Nitro Sandbox with a VMM.** On the instance, use a standard VMM (we recommend Firecracker) to launch the Nitro Sandbox from your image, specifying the vCPU count, memory, and devices. Confidential mode is the default. You can instead select direct mode for higher throughput without attestation.

1. **Attest the Nitro Sandbox before you release secrets.** At launch, the Nitro Sandbox measures its contents into the NSM. Your workload retrieves the attestation, and an external verifier (commonly AWS KMS, through a condition in a key policy) releases secrets only when the measurement matches. The parent instance can't forge the measurement.

When you run your own orchestrator, you are the parent operator. You are responsible for the following tasks:
+ Building guest images with the correct settings.
+ Running the device backends, and treating all data from a Nitro Sandbox as untrusted input.
+ Accounting for the memory and CPU you contribute, and zeroing memory before you contribute it.
+ Terminating Nitro Sandboxes for an orderly shutdown.
+ Relaying attestation traffic between the Nitro Sandbox and the external verifier.

## Launch, resize, and attach storage to a Nitro Sandbox
<a name="nitro-sandboxes-launch-size-storage"></a>

When you run your own orchestrator, you use standard Amazon EC2 and VMM commands to launch a Nitro Sandbox, set its size, and attach storage. The examples in this section use Firecracker, the recommended VMM. For other VMMs, such as QEMU, you need to add Nitro Sandbox compatibility before you can use attestation or run a Nitro Sandbox in confidential mode.

### How Firecracker works
<a name="nitro-sandboxes-firecracker"></a>

Firecracker can launch and manage Nitro Sandboxes as an alternative to KVM microVMs. Instead of creating a microVM through KVM, Firecracker uses the Nitro Enclaves driver on the parent instance to create, configure, and boot a Nitro Sandbox with a standard virtio-pci device model. Firecracker acts as the Nitro Sandbox's frontend: it owns the API socket, the device backends, and the Nitro Sandbox lifecycle. To launch a Nitro Sandbox, Firecracker does the following:

1. Creates the Nitro Sandbox and checks the capabilities that the platform supports.

1. Adds vCPUs, either as dedicated cores from the parent's CPU pool, as explicit CPU IDs, or as vCPUs that share the parent's remaining cores when you enable CPU overcommit.

1. Allocates contiguous memory, writes the guest image into it, and donates the memory to the Nitro Sandbox.

1. Registers each configured virtio device, such as block, network, vsock, and entropy devices.

1. Starts the Nitro Sandbox. The Nitro System boots the image through UEFI firmware and presents a full PCIe topology to the guest.

After the guest starts, the device backends in Firecracker serve I/O through shared queues: guest memory in direct mode, or dedicated device memory buffers in confidential mode. The guest sees ordinary virtio-pci devices and needs no sandbox-specific code. Nitro Sandbox memory isn't overcommitted: the parent donates the full memory size when the Nitro Sandbox starts, and that memory returns to the parent only when the Nitro Sandbox terminates.

**Note**
Because Nitro Sandboxes build on Nitro Enclaves, the Firecracker API uses the term *enclave* for the Nitro Sandbox configuration endpoint. Confidential mode is the default; direct mode is opt-in.

### Launch a Nitro Sandbox
<a name="nitro-sandboxes-launch"></a>

First, launch an instance type that supports AWS Nitro Enclaves, and enable it with the `--enclave-options Enabled=true` parameter, the same option that enables Nitro Enclaves.

```
aws ec2 run-instances \
--image-id {{ami-id}} \
--instance-type {{instance-type}} \
--enclave-options Enabled=true
```

After the instance is running, use Firecracker, the recommended VMM, on the instance to launch the Nitro Sandbox from your guest image, specifying the vCPU count, memory, and devices. Firecracker drives a Nitro Sandbox through its API socket or a `--config-file` JSON file rather than through command-line machine flags. Confidential mode is the default, and we recommend it for any workload that processes secrets. Because confidential mode is the default, the empty `"enclave": {}` object is enough to mark the virtual machine as a Nitro Sandbox; you don't set a separate confidential flag.

```
{
    "boot-source": {
        "kernel_image_path": "sandbox-image"
    },
    "machine-config": {
        "vcpu_count": 2,
        "mem_size_mib": 2048
    },
    "drives": [
        {
            "drive_id": "rootfs",
            "path_on_host": "rootfs.ext4",
            "is_root_device": true,
            "is_read_only": false
        }
    ],
    "network-interfaces": [
        {
            "iface_id": "eth0",
            "host_dev_name": "tap0"
        }
    ],
    "enclave": {}
}
```

Launch the Nitro Sandbox by passing the configuration file to Firecracker.

```
firecracker --config-file sandbox.json
```

To use direct mode instead (which shares memory with the parent, provides no attestation, and offers higher I/O throughput), set `direct_mode` to true in the enclave configuration. The parent keeps access to the Nitro Sandbox's memory.

```
"enclave": {
    "direct_mode": true
}
```

### Size and resize a Nitro Sandbox
<a name="nitro-sandboxes-resize"></a>

You set the size of a Nitro Sandbox at launch with the VMM. In the `machine-config` object, `vcpu_count` sets the number of vCPUs and `mem_size_mib` sets the memory in MiB (a multiple of 2).

```
"machine-config": {
    "vcpu_count": 4,
    "mem_size_mib": 2048
}
```

By default, each vCPU consumes a dedicated physical core from the Nitro Enclaves CPU pool, and Nitro allocates cores whole (both SMT siblings together). To let vCPUs float over the parent's remaining CPUs instead of dedicating whole cores, set `cpu_overcommit` to true in the Nitro Sandbox (enclave) configuration when you launch it. Before you launch Nitro Sandboxes, provision the parent-side resource pools that back their size: a CPU pool for pinned vCPUs, a memory pool for the memory you contribute, and a device-slot budget large enough for the number of Nitro Sandboxes you plan to run.

You can't change a Nitro Sandbox's vCPU and memory allocation during the life of the Nitro Sandbox. To change either value, terminate the Nitro Sandbox and re-create it at the new size. If the guest image enables PCIe hot plug, you can add devices to a running Nitro Sandbox; otherwise, attach all devices before you launch it. To run more or larger Nitro Sandboxes than the parent currently has capacity for, increase the parent-side CPU pool, memory pool, and device-slot budget before you launch them.

### Attach storage to a Nitro Sandbox
<a name="nitro-sandboxes-attach-storage"></a>

A Nitro Sandbox reaches storage the same way an ordinary Amazon EC2 guest does, through the devices that the parent presents to it. You can attach the following types of storage:

Local instance store
Ephemeral NVMe storage on the parent host, which the parent presents to the Nitro Sandbox as a `virtio-blk` device. It is fast and included in the instance price, but you lose its contents when the instance stops or terminates. Use it for scratch space and caches.

Amazon EBS
Persistent, network-attached block volumes. The parent presents a volume to the Nitro Sandbox as a `virtio-blk` device. A block device attaches to only one Nitro Sandbox at a time. Don't mount the same volume from two Nitro Sandboxes at the same time, which corrupts the file system. Encrypt volumes with an AWS KMS key.

Amazon S3 and other network storage
Object and file storage that the Nitro Sandbox reaches over the network. The Nitro Sandbox needs network connectivity and an AWS identity. Amazon S3, Amazon EFS, and similar services are inherently shareable across many Nitro Sandboxes and ordinary instances. You control access with IAM and encrypt data with `SSE-KMS`.

Storage isolation is independent of compute isolation. To keep data confidential from the parent operator, encrypt the volume or objects with an AWS KMS key whose policy releases the data key only to a Nitro Sandbox whose attestation matches the values you expect.

## Considerations and limitations
<a name="nitro-sandboxes-considerations"></a>

Keep the following considerations in mind when you use Nitro Sandboxes:

Supported instance types
Nitro Sandboxes are available only on instance types that support AWS Nitro Enclaves. If an instance type can't run Nitro Enclaves, it can't run Nitro Sandboxes. The following instance types support Nitro Sandboxes:

**General purpose instances that support Nitro Sandboxes**

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>M5</td><td>All instance types, <b>except</b>: <code>m5.large</code> | <code>m5.metal</code></td></tr>
  <tr><td>M5a</td><td>All instance types, <b>except</b>: <code>m5a.large</code></td></tr>
  <tr><td>M5ad</td><td>All instance types, <b>except</b>: <code>m5ad.large</code></td></tr>
  <tr><td>M5d</td><td>All instance types, <b>except</b>: <code>m5d.large</code> | <code>m5d.metal</code></td></tr>
  <tr><td>M5dn</td><td>All instance types, <b>except</b>: <code>m5dn.large</code> | <code>m5dn.metal</code></td></tr>
  <tr><td>M5n</td><td>All instance types, <b>except</b>: <code>m5n.large</code> | <code>m5n.metal</code></td></tr>
  <tr><td>M5zn</td><td>All instance types, <b>except</b>: <code>m5zn.large</code> | <code>m5zn.metal</code></td></tr>
  <tr><td>M6a</td><td>All instance types, <b>except</b>: <code>m6a.large</code> | <code>m6a.metal</code></td></tr>
  <tr><td>M6g</td><td>All instance types, <b>except</b>: <code>m6g.medium</code> | <code>m6g.metal</code></td></tr>
  <tr><td>M6gd</td><td>All instance types, <b>except</b>: <code>m6gd.medium</code> | <code>m6gd.metal</code></td></tr>
  <tr><td>M6i</td><td>All instance types, <b>except</b>: <code>m6i.large</code> | <code>m6i.metal</code></td></tr>
  <tr><td>M6id</td><td>All instance types, <b>except</b>: <code>m6id.large</code> | <code>m6id.metal</code></td></tr>
  <tr><td>M6idn</td><td>All instance types, <b>except</b>: <code>m6idn.large</code> | <code>m6idn.metal</code></td></tr>
  <tr><td>M6in</td><td>All instance types, <b>except</b>: <code>m6in.large</code> | <code>m6in.metal</code></td></tr>
  <tr><td>M7a</td><td>All instance types, <b>except</b>: <code>m7a.medium</code> | <code>m7a.large</code> | <code>m7a.metal-48xl</code></td></tr>
  <tr><td>M7g</td><td>All instance types, <b>except</b>: <code>m7g.medium</code> | <code>m7g.metal</code></td></tr>
  <tr><td>M7gd</td><td>All instance types, <b>except</b>: <code>m7gd.medium</code> | <code>m7gd.metal</code></td></tr>
  <tr><td>M7i</td><td>All instance types, <b>except</b>: <code>m7i.large</code> | <code>m7i.metal-24xl</code> | <code>m7i.metal-48xl</code></td></tr>
  <tr><td>M8a</td><td>All instance types, <b>except</b>: <code>m8a.medium</code> | <code>m8a.metal-24xl</code> | <code>m8a.metal-48xl</code></td></tr>
  <tr><td>M8azn</td><td>All instance types, <b>except</b>: <code>m8azn.medium</code> | <code>m8azn.metal-12xl</code> | <code>m8azn.metal-24xl</code></td></tr>
  <tr><td>M8g</td><td>All instance types, <b>except</b>: <code>m8g.medium</code> | <code>m8g.metal-24xl</code> | <code>m8g.metal-48xl</code></td></tr>
  <tr><td>M8gb</td><td>All instance types, <b>except</b>: <code>m8gb.medium</code> | <code>m8gb.metal-24xl</code> | <code>m8gb.metal-48xl</code></td></tr>
  <tr><td>M8gd</td><td>All instance types, <b>except</b>: <code>m8gd.medium</code> | <code>m8gd.metal-24xl</code> | <code>m8gd.metal-48xl</code></td></tr>
  <tr><td>M8gn</td><td>All instance types, <b>except</b>: <code>m8gn.medium</code> | <code>m8gn.metal-24xl</code> | <code>m8gn.metal-48xl</code></td></tr>
  <tr><td>M8i</td><td>All instance types, <b>except</b>: <code>m8i.large</code> | <code>m8i.metal-48xl</code> | <code>m8i.metal-96xl</code></td></tr>
  <tr><td>M8id</td><td>All instance types, <b>except</b>: <code>m8id.large</code> | <code>m8id.metal-48xl</code> | <code>m8id.metal-96xl</code></td></tr>
  <tr><td>M8in</td><td>All instance types, <b>except</b>: <code>m8in.large</code> | <code>m8in.metal-48xl</code> | <code>m8in.metal-96xl</code></td></tr>
  <tr><td>M8idn</td><td>All instance types, <b>except</b>: <code>m8idn.large</code> | <code>m8idn.metal-48xl</code> | <code>m8idn.metal-96xl</code></td></tr>
  <tr><td>M8ine</td><td>All instance types, <b>except</b>: <code>m8ine.large</code></td></tr>
  <tr><td>M8ib</td><td>All instance types, <b>except</b>: <code>m8ib.large</code> | <code>m8ib.metal-48xl</code> | <code>m8ib.metal-96xl</code></td></tr>
  <tr><td>M8idb</td><td>All instance types, <b>except</b>: <code>m8idb.large</code> | <code>m8idb.metal-48xl</code> | <code>m8idb.metal-96xl</code></td></tr>
  <tr><td>M9g</td><td>All instance types, <b>except</b>: <code>m9g.medium</code> | <code>m9g.metal-48xl</code></td></tr>
  <tr><td>M9gd</td><td>All instance types, <b>except</b>: <code>m9gd.medium</code> | <code>m9gd.metal-48xl</code></td></tr>
</tbody>
</table>

**Compute optimized instances that support Nitro Sandboxes**

<table>
<thead>
  <tr><th>Instance family</th><th>Exceptions</th></tr>
</thead>
<tbody>
  <tr><td>C5</td><td>All instance types, <b>except</b>: <code>c5.large</code> | <code>c5.metal</code></td></tr>
  <tr><td>C5a</td><td>All instance types, <b>except</b>: <code>c5a.large</code></td></tr>
  <tr><td>C5ad</td><td>All instance types, <b>except</b>: <code>c5ad.large</code></td></tr>
  <tr><td>C5d</td><td>All instance types, <b>except</b>: <code>c5d.large</code> | <code>c5d.metal</code></td></tr>
  <tr><td>C5n</td><td>All instance types, <b>except</b>: <code>c5n.large</code> | <code>c5n.metal</code></td></tr>
  <tr><td>C6a</td><td>All instance types, <b>except</b>: <code>c6a.large</code> | <code>c6a.metal</code></td></tr>
  <tr><td>C6g</td><td>All instance types, <b>except</b>: <code>c6g.medium</code> | <code>c6g.metal</code></td></tr>
  <tr><td>C6gd</td><td>All instance types, <b>except</b>: <code>c6gd.medium</code> | <code>c6gd.metal</code></td></tr>
  <tr><td>C6gn</td><td>All instance types, <b>except</b>: <code>c6gn.medium</code></td></tr>
  <tr><td>C6i</td><td>All instance types, <b>except</b>: <code>c6i.large</code> | <code>c6i.metal</code></td></tr>
  <tr><td>C6id</td><td>All instance types, <b>except</b>: <code>c6id.large</code> | <code>c6id.metal</code></td></tr>
  <tr><td>C6in</td><td>All instance types, <b>except</b>: <code>c6in.large</code> | <code>c6in.metal</code></td></tr>
  <tr><td>C7a</td><td>All instance types, <b>except</b>: <code>c7a.medium</code> | <code>c7a.large</code> | <code>c7a.metal-48xl</code></td></tr>
  <tr><td>C7g</td><td>All instance types, <b>except</b>: <code>c7g.medium</code> | <code>c7g.metal</code></td></tr>
  <tr><td>C7gd</td><td>All instance types, <b>except</b>: <code>c7gd.medium</code> | <code>c7gd.metal</code></td></tr>
  <tr><td>C7i</td><td>All instance types, <b>except</b>: <code>c7i.large</code> | <code>c7i.metal-24xl</code> | <code>c7i.metal-48xl</code></td></tr>
  <tr><td>C8a</td><td>All instance types, <b>except</b>: <code>c8a.medium</code> | <code>c8a.metal-24xl</code> | <code>c8a.metal-48xl</code></td></tr>
  <tr><td>C8g</td><td>All instance types, <b>except</b>: <code>c8g.medium</code> | <code>c8g.metal-24xl</code> | <code>c8g.metal-48xl</code></td></tr>
  <tr><td>C8gb</td><td>All instance types, <b>except</b>: <code>c8gb.medium</code> | <code>c8gb.metal-24xl</code> | <code>c8gb.metal-48xl</code></td></tr>
  <tr><td>C8gd</td><td>All instance types, <b>except</b>: <code>c8gd.medium</code> | <code>c8gd.metal-24xl</code> | <code>c8gd.metal-48xl</code></td></tr>
  <tr><td>C8gn</td><td>All instance types, <b>except</b>: <code>c8gn.medium</code> | <code>c8gn.metal-24xl</code> | <code>c8gn.metal-48xl</code></td></tr>
  <tr><td>C8i</td><td>All instance types, <b>except</b>: <code>c8i.large</code> | <code>c8i.metal-48xl</code> | <code>c8i.metal-96xl</code></td></tr>
  <tr><td>C8id</td><td>All instance types, <b>except</b>: <code>c8id.large</code> | <code>c8id.metal-48xl</code> | <code>c8id.metal-96xl</code></td></tr>
  <tr><td>C8in</td><td>All instance types, <b>except</b>: <code>c8in.large</code> | <code>c8in.metal-48xl</code> | <code>c8in.metal-96xl</code></td></tr>
  <tr><td>C8ine</td><td>All instance types, <b>except</b>: <code>c8ine.large</code></td></tr>
  <tr><td>C8ib</td><td>All instance types, <b>except</b>: <code>c8ib.large</code> | <code>c8ib.metal-48xl</code> | <code>c8ib.metal-96xl</code></td></tr>
  <tr><td>C9g</td><td>All instance types, <b>except</b>: <code>c9g.medium</code> | <code>c9g.metal-48xl</code></td></tr>
  <tr><td>C9gd</td><td>All instance types, <b>except</b>: <code>c9gd.medium</code> | <code>c9gd.metal-48xl</code></td></tr>
</tbody>
</table>

**Memory optimized instances that support Nitro Sandboxes**

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>R5</td><td>All instance types, <b>except</b>: <code>r5.large</code> | <code>r5.metal</code></td></tr>
  <tr><td>R5a</td><td>All instance types, <b>except</b>: <code>r5a.large</code></td></tr>
  <tr><td>R5ad</td><td>All instance types, <b>except</b>: <code>r5ad.large</code></td></tr>
  <tr><td>R5b</td><td>All instance types, <b>except</b>: <code>r5b.large</code> | <code>r5b.metal</code></td></tr>
  <tr><td>R5d</td><td>All instance types, <b>except</b>: <code>r5d.large</code> | <code>r5d.metal</code></td></tr>
  <tr><td>R5dn</td><td>All instance types, <b>except</b>: <code>r5dn.large</code> | <code>r5dn.metal</code></td></tr>
  <tr><td>R5n</td><td>All instance types, <b>except</b>: <code>r5n.large</code> | <code>r5n.metal</code></td></tr>
  <tr><td>R6a</td><td>All instance types, <b>except</b>: <code>r6a.large</code> | <code>r6a.metal</code></td></tr>
  <tr><td>R6g</td><td>All instance types, <b>except</b>: <code>r6g.medium</code> | <code>r6g.metal</code></td></tr>
  <tr><td>R6gd</td><td>All instance types, <b>except</b>: <code>r6gd.medium</code> | <code>r6gd.metal</code></td></tr>
  <tr><td>R6i</td><td>All instance types, <b>except</b>: <code>r6i.large</code> | <code>r6i.metal</code></td></tr>
  <tr><td>R6id</td><td>All instance types, <b>except</b>: <code>r6id.large</code> | <code>r6id.metal</code></td></tr>
  <tr><td>R6idn</td><td>All instance types, <b>except</b>: <code>r6idn.large</code> | <code>r6idn.metal</code></td></tr>
  <tr><td>R6in</td><td>All instance types, <b>except</b>: <code>r6in.large</code> | <code>r6in.metal</code></td></tr>
  <tr><td>R7a</td><td>All instance types, <b>except</b>: <code>r7a.medium</code> | <code>r7a.large</code> | <code>r7a.metal-48xl</code></td></tr>
  <tr><td>R7g</td><td>All instance types, <b>except</b>: <code>r7g.medium</code> | <code>r7g.metal</code></td></tr>
  <tr><td>R7gd</td><td>All instance types, <b>except</b>: <code>r7gd.medium</code> | <code>r7gd.metal</code></td></tr>
  <tr><td>R7i</td><td>All instance types, <b>except</b>: <code>r7i.large</code> | <code>r7i.metal-24xl</code> | <code>r7i.metal-48xl</code></td></tr>
  <tr><td>R7iz</td><td>All instance types, <b>except</b>: <code>r7iz.large</code> | <code>r7iz.metal-16xl</code> | <code>r7iz.metal-32xl</code></td></tr>
  <tr><td>R8a</td><td>All instance types, <b>except</b>: <code>r8a.medium</code> | <code>r8a.metal-24xl</code> | <code>r8a.metal-48xl</code></td></tr>
  <tr><td>R8g</td><td>All instance types, <b>except</b>: <code>r8g.medium</code> | <code>r8g.metal-24xl</code> | <code>r8g.metal-48xl</code></td></tr>
  <tr><td>R8gb</td><td>All instance types, <b>except</b>: <code>r8gb.medium</code> | <code>r8gb.metal-24xl</code> | <code>r8gb.metal-48xl</code></td></tr>
  <tr><td>R8gd</td><td>All instance types, <b>except</b>: <code>r8gd.medium</code> | <code>r8gd.metal-24xl</code> | <code>r8gd.metal-48xl</code></td></tr>
  <tr><td>R8gn</td><td>All instance types, <b>except</b>: <code>r8gn.medium</code> | <code>r8gn.metal-24xl</code> | <code>r8gn.metal-48xl</code></td></tr>
  <tr><td>R8i</td><td>All instance types, <b>except</b>: <code>r8i.large</code> | <code>r8i.metal-48xl</code> | <code>r8i.metal-96xl</code></td></tr>
  <tr><td>R8id</td><td>All instance types, <b>except</b>: <code>r8id.large</code> | <code>r8id.metal-48xl</code> | <code>r8id.metal-96xl</code></td></tr>
  <tr><td>R8in</td><td>All instance types, <b>except</b>: <code>r8in.large</code> | <code>r8in.metal-48xl</code> | <code>r8in.metal-96xl</code></td></tr>
  <tr><td>R8idn</td><td>All instance types, <b>except</b>: <code>r8idn.large</code> | <code>r8idn.metal-48xl</code> | <code>r8idn.metal-96xl</code></td></tr>
  <tr><td>R8ib</td><td>All instance types, <b>except</b>: <code>r8ib.large</code> | <code>r8ib.metal-48xl</code> | <code>r8ib.metal-96xl</code></td></tr>
  <tr><td>R8idb</td><td>All instance types, <b>except</b>: <code>r8idb.large</code> | <code>r8idb.metal-48xl</code> | <code>r8idb.metal-96xl</code></td></tr>
  <tr><td>R9g</td><td>All instance types, <b>except</b>: <code>r9g.medium</code> | <code>r9g.metal-48xl</code></td></tr>
  <tr><td>R9gd</td><td>All instance types, <b>except</b>: <code>r9gd.medium</code> | <code>r9gd.metal-48xl</code></td></tr>
  <tr><td>X2gd</td><td>All instance types, <b>except</b>: <code>x2gd.medium</code> | <code>x2gd.metal</code></td></tr>
  <tr><td>X2idn</td><td>All instance types, <b>except</b>: <code>x2idn.metal</code></td></tr>
  <tr><td>X2iedn</td><td>All instance types, <b>except</b>: <code>x2iedn.metal</code></td></tr>
  <tr><td>X2iezn</td><td>All instance types, <b>except</b>: <code>x2iezn.metal</code></td></tr>
  <tr><td>X8g</td><td>All instance types, <b>except</b>: <code>x8g.medium</code> | <code>x8g.metal-24xl</code> | <code>x8g.metal-48xl</code></td></tr>
  <tr><td>X8aedz</td><td>All instance types, <b>except</b>: <code>x8aedz.metal-12xl</code> | <code>x8aedz.metal-24xl</code></td></tr>
  <tr><td>X8i</td><td>All instance types, <b>except</b>: <code>x8i.large</code> | <code>x8i.metal-48xl</code> | <code>x8i.metal-96xl</code></td></tr>
  <tr><td>z1d</td><td>All instance types, <b>except</b>: <code>z1d.large</code> | <code>z1d.metal</code></td></tr>
</tbody>
</table>

**Storage optimized instances that support Nitro Sandboxes**

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>D3</td><td>All instance types.</td></tr>
  <tr><td>D3en</td><td>All instance types.</td></tr>
  <tr><td>I3en</td><td>All instance types, <b>except</b>: <code>i3en.large</code> | <code>i3en.metal</code></td></tr>
  <tr><td>I4g</td><td>All instance types.</td></tr>
  <tr><td>I4i</td><td>All instance types, <b>except</b>: <code>i4i.large</code> | <code>i4i.metal</code></td></tr>
  <tr><td>I7i</td><td>All instance types, <b>except</b>: <code>i7i.large</code> | <code>i7i.metal-24xl</code> | <code>i7i.metal-48xl</code></td></tr>
  <tr><td>I7ie</td><td>All instance types, <b>except</b>: <code>i7ie.large</code> | <code>i7ie.metal-24xl</code> | <code>i7ie.metal-48xl</code></td></tr>
  <tr><td>I8g</td><td>All instance types, <b>except</b>: <code>i8g.metal-24xl</code> | <code>i8g.metal-48xl</code></td></tr>
  <tr><td>I8ge</td><td>All instance types, <b>except</b>: <code>i8ge.metal-24xl</code> | <code>i8ge.metal-48xl</code></td></tr>
</tbody>
</table>

**Accelerated computing instances that support Nitro Sandboxes**

<table>
<thead>
  <tr><th>Instance family</th><th>Instance types</th></tr>
</thead>
<tbody>
  <tr><td>G6</td><td><code>g6.xlarge</code>, <code>g6.2xlarge</code>, <code>g6.4xlarge</code>, <code>g6.8xlarge</code>, <code>g6.12xlarge</code>, <code>g6.16xlarge</code>, <code>g6.24xlarge</code>, <code>g6.48xlarge</code></td></tr>
  <tr><td>Gr6</td><td><code>gr6.4xlarge</code>, <code>gr6.8xlarge</code></td></tr>
  <tr><td>G6e</td><td><code>g6e.xlarge</code>, <code>g6e.2xlarge</code>, <code>g6e.4xlarge</code>, <code>g6e.8xlarge</code>, <code>g6e.12xlarge</code>, <code>g6e.16xlarge</code>, <code>g6e.24xlarge</code>, <code>g6e.48xlarge</code></td></tr>
  <tr><td>G7</td><td><code>g7.2xlarge</code>, <code>g7.4xlarge</code>, <code>g7.8xlarge</code>, <code>g7.12xlarge</code>, <code>g7.24xlarge</code>, <code>g7.48xlarge</code></td></tr>
  <tr><td>G7e</td><td><code>g7e.2xlarge</code>, <code>g7e.4xlarge</code>, <code>g7e.8xlarge</code>, <code>g7e.12xlarge</code>, <code>g7e.24xlarge</code>, <code>g7e.48xlarge</code></td></tr>
  <tr><td>edg-8ad</td><td><code>edg-8ad.xlarge</code>, <code>edg-8ad.2xlarge</code>, <code>edg-8ad.4xlarge</code>, <code>edg-8ad.8xlarge</code>, <code>edg-8ad.16xlarge</code>, <code>edg-8ad.32xlarge</code></td></tr>
  <tr><td>P3dn</td><td><code>p3dn.24xlarge</code></td></tr>
  <tr><td>G5</td><td><code>g5.xlarge</code>, <code>g5.2xlarge</code>, <code>g5.4xlarge</code>, <code>g5.8xlarge</code>, <code>g5.12xlarge</code>, <code>g5.16xlarge</code>, <code>g5.24xlarge</code>, <code>g5.48xlarge</code></td></tr>
  <tr><td>G5g</td><td><code>g5g.xlarge</code>, <code>g5g.2xlarge</code>, <code>g5g.4xlarge</code>, <code>g5g.8xlarge</code>, <code>g5g.16xlarge</code></td></tr>
</tbody>
</table>

Maximum Nitro Sandboxes per instance
To maintain near-native Amazon EC2 performance, the total vCPUs allocated across all Nitro Sandboxes on an instance can't exceed 5 times the instance's vCPU count. This is a limit on total vCPU allocation, not on the number of Nitro Sandboxes: You can run up to 5 Nitro Sandboxes per vCPU only when each Nitro Sandbox uses a single vCPU. For example, on a 4-vCPU instance the budget is 20 vCPUs.
The instance's available memory also limits how many Nitro Sandboxes you can run, because the memory of each Nitro Sandbox is dedicated and isn't overcommitted. The number of Nitro Sandboxes on an instance can't exceed whichever of these limits you reach first:
+ 5 times the instance's vCPU count
+ The amount of memory available on the instance

**Example: Nitro Sandbox budget on a 4-vCPU instance (20 vCPU total)**
<a name="nitro-sandboxes-budget-example"></a>
<table>
<thead>
  <tr><th>vCPUs per Nitro Sandbox</th><th>Maximum Nitro Sandboxes</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>20</td></tr>
  <tr><td>2</td><td>10</td></tr>
  <tr><td>4</td><td>5</td></tr>
</tbody>
</table>

Larger Nitro Sandboxes reduce the number that you can run on the instance.

Device limits
The instance, not the Nitro Sandbox, determines the number of devices you can attach to a Nitro Sandbox. The instance type sets the maximum number of attached devices, including any devices that you hot plug. For the device limits of each instance type, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md).
When you run more than one Nitro Sandbox on the same instance, the Nitro Sandboxes share the instance's overall device limit.

Memory
The parent donates a Nitro Sandbox's full memory when the Nitro Sandbox starts, and that memory stays reserved until the Nitro Sandbox terminates. Nitro Sandbox memory isn't overcommitted.

Storage
A Nitro Sandbox reaches storage through the devices that the parent presents to it. You can use local instance store for ephemeral scratch space, Amazon EBS for persistent block storage, and Amazon S3, Amazon EFS, or other network storage for shared access. To keep data confidential from the parent operator, encrypt the volume with an attestation-gated AWS KMS key.

Shared parent-instance resources
The Nitro System isolates the compute and memory of each Nitro Sandbox, but the parent instance's network stack is a shared, per-instance resource. A single Nitro Sandbox can exhaust parent-side resources, such as the connection-tracking (conntrack) table or the DNS resolver budget, and deny network access to other Nitro Sandboxes on the same instance. As the parent operator, cap or rate-limit these resources for each Nitro Sandbox.

GPU passthrough
GPU passthrough into a Nitro Sandbox is currently unavailable.

Resizing
You can't change a Nitro Sandbox's vCPU and memory allocation during the life of the Nitro Sandbox. To change either, terminate and re-create the Nitro Sandbox at the new size.
