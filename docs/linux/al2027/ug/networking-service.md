---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/networking-service.html
---

# Networking service
<a name="networking-service"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The open-source project `systemd-networkd` is widely available in modern Linux distributions. The project uses a declarative configuration language that's similar to the rest of the `systemd` framework. Its primary configuration file types are `.network` and `.link` files.

The `amazon-ec2-net-utils` package configures each interface in the `/run/systemd/network` directory. For each Elastic Network Interface (ENI) that's attached to an instance, the package creates a per-interface configuration named `70-{{interface_name}}.network` that enables both IPv4 and IPv6 networking through DHCP.

Interface-specific settings are written to a drop-in directory named `70-{{interface_name}}.network.d` that's associated with the per-interface configuration. The `policy-routes@{{interface_name}}.service` unit generates an `eni.conf` drop-in in this directory. The drop-in installs policy routing rules that help ensure that locally sourced traffic is routed to the network through the corresponding instance's network interface. These rules ensure that the right traffic is routed through the ENI from the associated addresses or prefixes. For more information about using ENI, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide*.

You can customize this networking behavior by placing a custom configuration file in the `/etc/systemd/network` directory to override the default configuration settings contained in `/run/systemd/network`.

**Important**
If you supply a drop-in configuration file, ensure that `amazon-ec2-net-utils` has finished generating the base `70-{{interface_name}}.network` configuration and its associated `eni.conf` drop-in in `/run/systemd/network` and allow time for the default configuration to be fully applied before the drop-in takes effect. If the drop-in is applied at approximately the same time as the base configuration, the rapid succession of configuration changes can cause the interface link to go down. To avoid this race condition, make sure to allow enough time for the default configuration to take place before applying the custom configuration.

The [systemd.network](https://www.freedesktop.org/software/systemd/man/systemd.network.html) documentation on the freedesktop.org website describes how the `systemd-networkd` service determines the configuration that applies to a specific interface. It also generates alternative names, known as altnames, for the ENI-backed interfaces to reflect the properties of various AWS resources. These ENI-backed interface properties are the `ENI ID` and the `DeviceIndex` field of the ENI attachment. You can refer to these interfaces using their properties when using various tools, such as the `ip` command.

AL2027 instance interface names are generated using the `systemd` slot naming scheme. AL2027 ships with `systemd` version 260 and uses the `v260` net naming scheme by default. For more information, see [systemd.net naming scheme](https://www.freedesktop.org/software/systemd/man/systemd.net-naming-scheme.html) on the freedesktop.org website.

Additionally, AL2027 uses the `fq_codel` active queue management network transmission scheduling algorithm by default. For more information, see [CoDel overview](https://www.bufferbloat.net/projects/codel/wiki/) on the Bufferbloat website.
