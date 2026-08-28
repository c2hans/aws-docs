---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/networking-service.html
---

# Networking service
<a name="networking-service"></a>

The open-source project `systemd-networkd` is widely available in modern Linux distributions. The project uses a declarative configuration language that's similar to the rest of the `systemd` framework. Its primary configuration file types are `.network` and `.link` files.

The `amazon-ec2-net-utils` package generates interface-specific configurations in the `/run/systemd/network` directory. These configurations enable both IPv4 and IPv6 networking on interfaces when they're attached to an instance. These configurations also install policy routing rules that help ensure that locally sourced traffic is routed to the network through the corresponding instance's network interface. These rules ensure that the right traffic is routed through the Elastic Network Interface (ENI) from the associated addresses or prefixes. For more information about using ENI, see [Using ENI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide*.

You can customize this networking behavior by placing a custom configuration file in the `/etc/systemd/network` directory to override the default configuration settings contained in `/run/systemd/network`.

**Important**
If you supply a drop-in configuration file, ensure that `amazon-ec2-net-utils` has finished generating the base `70-ens{{N}}.network` file in `/run/systemd/network` and allow time for the default configuration to be fully applied before the drop-in takes effect. If the drop-in is applied at approximately the same time as the base configuration, the rapid succession of configuration changes can cause the interface link to go down. To avoid this race condition, make sure to allow enough time for the default configuration to take place before applying the custom configuration.

The [systemd.network](https://www.freedesktop.org/software/systemd/man/systemd.network.html) documentation describes how the `systemd-networkd` service determines the configuration that applies to a specific interface. It also generates alternative names, known as altnames, for the ENI-backed interfaces to reflect the properties of various AWS resources. These ENI-backed interface properties are the `ENI ID` and the `DeviceIndex` field of the ENI attachment. You can refer to these interfaces using their properties when using various tools, such as the `ip` command.

AL2023 instance interface names are generated using the `systemd` slot naming scheme. For more information, see [systemd.net naming scheme](https://www.freedesktop.org/software/systemd/man/systemd.net-naming-scheme.html).

Additionally, AL2023 uses the `fq_codel` active queue management network transmission scheduling algorithm by default. For more information, see [CoDel overview](https://www.bufferbloat.net/projects/codel/wiki/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
