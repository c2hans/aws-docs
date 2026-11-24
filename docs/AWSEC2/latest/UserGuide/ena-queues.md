---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-queues.html
---

# ENA queues

Elastic Network Adapter (ENA) queues handle packet processing for your Amazon EC2 network interfaces. Each network card has a pool of ENA queues that is shared by the network interfaces attached to it. On instance types with multiple network cards, each network card has a separate pool, and network interfaces on different network cards don't share queues. By default, each network interface gets a fixed number of queues, based on the instance type and size.

On [supported instance types](#supported-instances), you can choose how many queues each network interface gets. Each network interface is limited to the maximum ENA queues per interface for the instance type, and all network interfaces on a network card together are limited to that card's pool. For example, assign more queues to a network interface with high packets-per-second traffic across many flows, so that processing spreads across more vCPUs. Assign fewer queues to a low-traffic interface, such as a management interface, to leave queues for other network interfaces.

**Topics**
+ [ENA queue specifications for EC2 instance types](#supported-instances)
+ [Network interface limits and ENA queues](#ena-queues-network-interface-limits)
+ [Configure ENA queue allocation](#modify)

## ENA queue specifications for EC2 instance types
<a name="supported-instances"></a>

The following tables list instance types that support configurable ENA queue allocation, along with their default and maximum queue values.

**Note**
For ENA queue values for all instance types, including types that do not support configurable ENA queue allocation, see the [Network specifications tables](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-type-specifications.html) in the *Amazon EC2 Instance Types* guide.

------
#### [ General purpose ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| m6i.large | 1 | 3 | 2 | 2 | 6 |
| m6i.xlarge | 1 | 4 | 4 | 4 | 16 |
| m6i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m6i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m6i.8xlarge | 1 | 8 | 8 | 32 | 64 |
| m6i.12xlarge | 1 | 8 | 8 | 32 | 64 |
| m6i.16xlarge | 1 | 15 | 8 | 32 | 120 |
| m6i.24xlarge | 1 | 15 | 8 | 32 | 120 |
| m6i.32xlarge | 1 | 15 | 8 | 32 | 120 |
| m6id.large | 1 | 3 | 2 | 2 | 6 |
| m6id.xlarge | 1 | 4 | 4 | 4 | 16 |
| m6id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m6id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m6id.8xlarge | 1 | 8 | 8 | 32 | 64 |
| m6id.12xlarge | 1 | 8 | 8 | 32 | 64 |
| m6id.16xlarge | 1 | 15 | 8 | 32 | 120 |
| m6id.24xlarge | 1 | 15 | 8 | 32 | 120 |
| m6id.32xlarge | 1 | 15 | 8 | 32 | 120 |
| m6idn.large | 1 | 3 | 2 | 2 | 6 |
| m6idn.xlarge | 1 | 4 | 4 | 4 | 16 |
| m6idn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m6idn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m6idn.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m6idn.12xlarge | 1 | 8 | 16 | 32 | 128 |
| m6idn.16xlarge | 1 | 15 | 16 | 32 | 240 |
| m6idn.24xlarge | 1 | 15 | 32 | 32 | 480 |
| m6idn.32xlarge | 2 | 8 | 32 | 32 | 256 |
| m6in.large | 1 | 3 | 2 | 2 | 6 |
| m6in.xlarge | 1 | 4 | 4 | 4 | 16 |
| m6in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m6in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m6in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m6in.12xlarge | 1 | 8 | 16 | 32 | 128 |
| m6in.16xlarge | 1 | 15 | 16 | 32 | 240 |
| m6in.24xlarge | 1 | 15 | 32 | 32 | 480 |
| m6in.32xlarge | 2 | 8 | 32 | 32 | 256 |
| m8a.medium | 1 | 2 | 1 | 1 | 3 |
| m8a.large | 1 | 3 | 2 | 2 | 6 |
| m8a.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8a.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8a.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8a.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m8a.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8a.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8a.24xlarge | 1 | 16 | 16 | 128 | 384 |
| m8a.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8a.metal-24xl | 1 | 16 | 16 | 128 | 384 |
| m8a.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8azn.medium | 1 | 3 | 1 | 1 | 3 |
| m8azn.large | 1 | 4 | 2 | 2 | 8 |
| m8azn.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8azn.3xlarge | 1 | 8 | 4 | 16 | 48 |
| m8azn.6xlarge | 1 | 8 | 8 | 32 | 96 |
| m8azn.12xlarge | 1 | 16 | 8 | 64 | 192 |
| m8azn.24xlarge | 1 | 16 | 16 | 128 | 384 |
| m8azn.metal-12xl | 1 | 16 | 8 | 64 | 192 |
| m8azn.metal-24xl | 1 | 16 | 16 | 128 | 384 |
| m8gb.medium | 1 | 2 | 1 | 1 | 2 |
| m8gb.large | 1 | 3 | 2 | 2 | 6 |
| m8gb.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8gb.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8gb.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8gb.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m8gb.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8gb.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8gb.24xlarge | 1 | 24 | 16 | 128 | 384 |
| m8gb.48xlarge | 2 | 12 | 32 | 128 | 384 |
| m8gb.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| m8gb.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| m8gn.medium | 1 | 2 | 1 | 1 | 2 |
| m8gn.large | 1 | 3 | 2 | 2 | 6 |
| m8gn.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8gn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8gn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8gn.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m8gn.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8gn.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8gn.24xlarge | 1 | 24 | 16 | 128 | 384 |
| m8gn.48xlarge | 2 | 12 | 32 | 128 | 384 |
| m8gn.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| m8gn.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| m8i.large | 1 | 3 | 2 | 2 | 6 |
| m8i.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8i.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m8i.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8i.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8i.24xlarge | 1 | 16 | 16 | 128 | 384 |
| m8i.32xlarge | 1 | 24 | 16 | 128 | 512 |
| m8i.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8i.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| m8i.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8i.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| m8id.large | 1 | 3 | 2 | 2 | 6 |
| m8id.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8id.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m8id.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8id.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8id.24xlarge | 1 | 16 | 16 | 128 | 384 |
| m8id.32xlarge | 1 | 24 | 16 | 128 | 512 |
| m8id.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8id.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| m8id.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8id.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| m8i-flex.large | 1 | 3 | 1 | 1 | 3 |
| m8i-flex.xlarge | 1 | 4 | 2 | 2 | 8 |
| m8i-flex.2xlarge | 1 | 4 | 4 | 4 | 16 |
| m8i-flex.4xlarge | 1 | 8 | 4 | 8 | 32 |
| m8i-flex.8xlarge | 1 | 10 | 4 | 16 | 64 |
| m8i-flex.12xlarge | 1 | 12 | 8 | 32 | 96 |
| m8i-flex.16xlarge | 1 | 16 | 8 | 32 | 128 |
| m8in.large | 1 | 4 | 2 | 2 | 8 |
| m8in.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m8in.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8in.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8in.24xlarge | 1 | 16 | 16 | 128 | 256 |
| m8in.32xlarge | 1 | 16 | 32 | 128 | 512 |
| m8in.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8in.96xlarge | 2 | 12 | 32 | 128 | 768 |
| m8in.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8in.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| m8idn.large | 1 | 4 | 2 | 2 | 8 |
| m8idn.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8idn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8idn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8idn.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m8idn.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8idn.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8idn.24xlarge | 1 | 16 | 16 | 128 | 256 |
| m8idn.32xlarge | 1 | 16 | 32 | 128 | 512 |
| m8idn.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8idn.96xlarge | 2 | 12 | 32 | 128 | 768 |
| m8idn.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8idn.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| m8ine.large | 1 | 4 | 2 | 2 | 8 |
| m8ine.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8ine.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8ine.4xlarge | 1 | 8 | 16 | 16 | 128 |
| m8ine.8xlarge | 1 | 8 | 32 | 32 | 256 |
| m8ine.12xlarge | 1 | 12 | 32 | 64 | 384 |
| m8ib.large | 1 | 4 | 2 | 2 | 8 |
| m8ib.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8ib.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8ib.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8ib.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m8ib.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8ib.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8ib.24xlarge | 1 | 16 | 16 | 128 | 256 |
| m8ib.32xlarge | 1 | 16 | 32 | 128 | 512 |
| m8ib.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8ib.96xlarge | 2 | 12 | 32 | 128 | 768 |
| m8ib.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8ib.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| m8idb.large | 1 | 4 | 2 | 2 | 8 |
| m8idb.xlarge | 1 | 4 | 4 | 4 | 16 |
| m8idb.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m8idb.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m8idb.8xlarge | 1 | 8 | 16 | 32 | 128 |
| m8idb.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m8idb.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m8idb.24xlarge | 1 | 16 | 16 | 128 | 256 |
| m8idb.32xlarge | 1 | 16 | 32 | 128 | 512 |
| m8idb.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m8idb.96xlarge | 2 | 12 | 32 | 128 | 768 |
| m8idb.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m8idb.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| m9g.medium | 1 | 2 | 1 | 1 | 2 |
| m9g.large | 1 | 3 | 2 | 2 | 6 |
| m9g.xlarge | 1 | 4 | 4 | 4 | 16 |
| m9g.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m9g.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m9g.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m9g.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m9g.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m9g.24xlarge | 1 | 24 | 16 | 128 | 384 |
| m9g.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m9g.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| m9gd.medium | 1 | 2 | 1 | 1 | 2 |
| m9gd.large | 1 | 3 | 2 | 2 | 6 |
| m9gd.xlarge | 1 | 4 | 4 | 4 | 16 |
| m9gd.2xlarge | 1 | 4 | 8 | 8 | 32 |
| m9gd.4xlarge | 1 | 8 | 8 | 16 | 64 |
| m9gd.8xlarge | 1 | 10 | 8 | 32 | 128 |
| m9gd.12xlarge | 1 | 12 | 16 | 64 | 192 |
| m9gd.16xlarge | 1 | 16 | 16 | 64 | 256 |
| m9gd.24xlarge | 1 | 24 | 16 | 128 | 384 |
| m9gd.48xlarge | 1 | 24 | 32 | 128 | 768 |
| m9gd.metal-48xl | 1 | 24 | 32 | 128 | 768 |

------
#### [ Compute optimized ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| c6i.large | 1 | 3 | 2 | 2 | 6 |
| c6i.xlarge | 1 | 4 | 4 | 4 | 16 |
| c6i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c6i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c6i.8xlarge | 1 | 8 | 8 | 32 | 64 |
| c6i.12xlarge | 1 | 8 | 8 | 32 | 64 |
| c6i.16xlarge | 1 | 15 | 8 | 32 | 120 |
| c6i.24xlarge | 1 | 15 | 8 | 32 | 120 |
| c6i.32xlarge | 1 | 15 | 8 | 32 | 120 |
| c6id.large | 1 | 3 | 2 | 2 | 6 |
| c6id.xlarge | 1 | 4 | 4 | 4 | 16 |
| c6id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c6id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c6id.8xlarge | 1 | 8 | 8 | 32 | 64 |
| c6id.12xlarge | 1 | 8 | 8 | 32 | 64 |
| c6id.16xlarge | 1 | 15 | 8 | 32 | 120 |
| c6id.24xlarge | 1 | 15 | 8 | 32 | 120 |
| c6id.32xlarge | 1 | 15 | 8 | 32 | 120 |
| c6in.large | 1 | 3 | 2 | 2 | 6 |
| c6in.xlarge | 1 | 4 | 4 | 4 | 16 |
| c6in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c6in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c6in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| c6in.12xlarge | 1 | 8 | 16 | 32 | 128 |
| c6in.16xlarge | 1 | 15 | 16 | 32 | 240 |
| c6in.24xlarge | 1 | 15 | 32 | 32 | 480 |
| c6in.32xlarge | 2 | 8 | 32 | 32 | 256 |
| c8a.medium | 1 | 2 | 1 | 1 | 3 |
| c8a.large | 1 | 3 | 2 | 2 | 6 |
| c8a.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8a.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8a.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8a.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c8a.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8a.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8a.24xlarge | 1 | 16 | 16 | 128 | 384 |
| c8a.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c8a.metal-24xl | 1 | 16 | 16 | 128 | 384 |
| c8a.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c8gb.medium | 1 | 2 | 1 | 1 | 2 |
| c8gb.large | 1 | 3 | 2 | 2 | 6 |
| c8gb.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8gb.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8gb.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8gb.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c8gb.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8gb.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8gb.24xlarge | 1 | 24 | 16 | 128 | 384 |
| c8gb.48xlarge | 2 | 12 | 32 | 128 | 384 |
| c8gb.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| c8gb.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| c8gn.medium | 1 | 2 | 1 | 1 | 2 |
| c8gn.large | 1 | 3 | 2 | 2 | 6 |
| c8gn.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8gn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8gn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8gn.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c8gn.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8gn.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8gn.24xlarge | 1 | 24 | 16 | 128 | 384 |
| c8gn.48xlarge | 2 | 12 | 32 | 128 | 384 |
| c8gn.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| c8gn.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| c8i.large | 1 | 3 | 2 | 2 | 6 |
| c8i.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8i.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c8i.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8i.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8i.24xlarge | 1 | 16 | 16 | 128 | 384 |
| c8i.32xlarge | 1 | 24 | 16 | 128 | 512 |
| c8i.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c8i.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| c8i.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c8i.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| c8id.large | 1 | 3 | 2 | 2 | 6 |
| c8id.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8id.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c8id.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8id.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8id.24xlarge | 1 | 16 | 16 | 128 | 384 |
| c8id.32xlarge | 1 | 24 | 16 | 128 | 512 |
| c8id.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c8id.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| c8id.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c8id.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| c8i-flex.large | 1 | 3 | 1 | 1 | 3 |
| c8i-flex.xlarge | 1 | 4 | 2 | 2 | 8 |
| c8i-flex.2xlarge | 1 | 4 | 4 | 4 | 16 |
| c8i-flex.4xlarge | 1 | 8 | 4 | 8 | 32 |
| c8i-flex.8xlarge | 1 | 10 | 4 | 16 | 64 |
| c8i-flex.12xlarge | 1 | 12 | 8 | 32 | 96 |
| c8i-flex.16xlarge | 1 | 16 | 8 | 32 | 128 |
| c8in.large | 1 | 4 | 2 | 2 | 8 |
| c8in.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| c8in.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8in.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8in.24xlarge | 1 | 16 | 16 | 128 | 256 |
| c8in.32xlarge | 1 | 16 | 32 | 128 | 512 |
| c8in.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c8in.96xlarge | 2 | 12 | 32 | 128 | 768 |
| c8in.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c8in.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| c8ine.large | 1 | 4 | 2 | 2 | 8 |
| c8ine.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8ine.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8ine.4xlarge | 1 | 8 | 16 | 16 | 128 |
| c8ine.8xlarge | 1 | 8 | 32 | 32 | 256 |
| c8ine.12xlarge | 1 | 12 | 32 | 64 | 384 |
| c8ib.large | 1 | 4 | 2 | 2 | 8 |
| c8ib.xlarge | 1 | 4 | 4 | 4 | 16 |
| c8ib.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c8ib.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c8ib.8xlarge | 1 | 8 | 16 | 32 | 128 |
| c8ib.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c8ib.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c8ib.24xlarge | 1 | 16 | 16 | 128 | 256 |
| c8ib.32xlarge | 1 | 16 | 32 | 128 | 512 |
| c8ib.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c8ib.96xlarge | 2 | 12 | 32 | 128 | 768 |
| c8ib.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c8ib.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| c9g.medium | 1 | 2 | 1 | 1 | 2 |
| c9g.large | 1 | 3 | 2 | 2 | 6 |
| c9g.xlarge | 1 | 4 | 4 | 4 | 16 |
| c9g.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c9g.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c9g.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c9g.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c9g.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c9g.24xlarge | 1 | 24 | 16 | 128 | 384 |
| c9g.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c9g.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| c9gd.medium | 1 | 2 | 1 | 1 | 2 |
| c9gd.large | 1 | 3 | 2 | 2 | 6 |
| c9gd.xlarge | 1 | 4 | 4 | 4 | 16 |
| c9gd.2xlarge | 1 | 4 | 8 | 8 | 32 |
| c9gd.4xlarge | 1 | 8 | 8 | 16 | 64 |
| c9gd.8xlarge | 1 | 10 | 8 | 32 | 128 |
| c9gd.12xlarge | 1 | 12 | 16 | 64 | 192 |
| c9gd.16xlarge | 1 | 16 | 16 | 64 | 256 |
| c9gd.24xlarge | 1 | 24 | 16 | 128 | 384 |
| c9gd.48xlarge | 1 | 24 | 32 | 128 | 768 |
| c9gd.metal-48xl | 1 | 24 | 32 | 128 | 768 |

------
#### [ Memory optimized ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| r6i.large | 1 | 3 | 2 | 2 | 6 |
| r6i.xlarge | 1 | 4 | 4 | 4 | 16 |
| r6i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r6i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r6i.8xlarge | 1 | 8 | 8 | 32 | 64 |
| r6i.12xlarge | 1 | 8 | 8 | 32 | 64 |
| r6i.16xlarge | 1 | 15 | 8 | 32 | 120 |
| r6i.24xlarge | 1 | 15 | 8 | 32 | 120 |
| r6i.32xlarge | 1 | 15 | 8 | 32 | 120 |
| r6id.large | 1 | 3 | 2 | 2 | 6 |
| r6id.xlarge | 1 | 4 | 4 | 4 | 16 |
| r6id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r6id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r6id.8xlarge | 1 | 8 | 8 | 32 | 64 |
| r6id.12xlarge | 1 | 8 | 8 | 32 | 64 |
| r6id.16xlarge | 1 | 15 | 8 | 32 | 120 |
| r6id.24xlarge | 1 | 15 | 8 | 32 | 120 |
| r6id.32xlarge | 1 | 15 | 8 | 32 | 120 |
| r6idn.large | 1 | 3 | 2 | 2 | 6 |
| r6idn.xlarge | 1 | 4 | 4 | 4 | 16 |
| r6idn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r6idn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r6idn.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r6idn.12xlarge | 1 | 8 | 16 | 32 | 128 |
| r6idn.16xlarge | 1 | 15 | 16 | 32 | 240 |
| r6idn.24xlarge | 1 | 15 | 32 | 32 | 480 |
| r6idn.32xlarge | 2 | 8 | 32 | 32 | 256 |
| r6in.large | 1 | 3 | 2 | 2 | 6 |
| r6in.xlarge | 1 | 4 | 4 | 4 | 16 |
| r6in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r6in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r6in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r6in.12xlarge | 1 | 8 | 16 | 32 | 128 |
| r6in.16xlarge | 1 | 15 | 16 | 32 | 240 |
| r6in.24xlarge | 1 | 15 | 32 | 32 | 480 |
| r6in.32xlarge | 2 | 8 | 32 | 32 | 256 |
| r8a.medium | 1 | 2 | 1 | 1 | 3 |
| r8a.large | 1 | 3 | 2 | 2 | 6 |
| r8a.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8a.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8a.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8a.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r8a.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8a.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8a.24xlarge | 1 | 16 | 16 | 128 | 384 |
| r8a.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8a.metal-24xl | 1 | 16 | 16 | 128 | 384 |
| r8a.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8gb.medium | 1 | 2 | 1 | 1 | 2 |
| r8gb.large | 1 | 3 | 2 | 2 | 6 |
| r8gb.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8gb.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8gb.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8gb.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r8gb.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8gb.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8gb.24xlarge | 1 | 24 | 16 | 128 | 384 |
| r8gb.48xlarge | 2 | 12 | 32 | 128 | 384 |
| r8gb.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| r8gb.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| r8gn.medium | 1 | 2 | 1 | 1 | 2 |
| r8gn.large | 1 | 3 | 2 | 2 | 6 |
| r8gn.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8gn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8gn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8gn.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r8gn.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8gn.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8gn.24xlarge | 1 | 24 | 16 | 128 | 384 |
| r8gn.48xlarge | 2 | 12 | 32 | 128 | 384 |
| r8gn.metal-24xl | 1 | 24 | 32 | 128 | 768 |
| r8gn.metal-48xl | 2 | 12 | 32 | 128 | 384 |
| r8i.large | 1 | 3 | 2 | 2 | 6 |
| r8i.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8i.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r8i.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8i.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8i.24xlarge | 1 | 16 | 16 | 128 | 384 |
| r8i.32xlarge | 1 | 24 | 16 | 128 | 512 |
| r8i.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8i.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| r8i.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8i.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| r8id.large | 1 | 3 | 2 | 2 | 6 |
| r8id.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8id.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8id.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8id.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r8id.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8id.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8id.24xlarge | 1 | 16 | 16 | 128 | 384 |
| r8id.32xlarge | 1 | 24 | 16 | 128 | 512 |
| r8id.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8id.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| r8id.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8id.metal-96xl | 1 | 24 | 32 | 128 | 1536 |
| r8i-flex.large | 1 | 3 | 1 | 1 | 3 |
| r8i-flex.xlarge | 1 | 4 | 2 | 2 | 8 |
| r8i-flex.2xlarge | 1 | 4 | 4 | 4 | 16 |
| r8i-flex.4xlarge | 1 | 8 | 4 | 8 | 32 |
| r8i-flex.8xlarge | 1 | 10 | 4 | 16 | 64 |
| r8i-flex.12xlarge | 1 | 12 | 8 | 32 | 96 |
| r8i-flex.16xlarge | 1 | 16 | 8 | 32 | 128 |
| r8in.large | 1 | 4 | 2 | 2 | 8 |
| r8in.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8in.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8in.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8in.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r8in.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8in.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8in.24xlarge | 1 | 16 | 16 | 128 | 256 |
| r8in.32xlarge | 1 | 16 | 32 | 128 | 512 |
| r8in.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8in.96xlarge | 2 | 12 | 32 | 128 | 768 |
| r8in.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8in.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| r8idn.large | 1 | 4 | 2 | 2 | 8 |
| r8idn.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8idn.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8idn.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8idn.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r8idn.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8idn.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8idn.24xlarge | 1 | 16 | 16 | 128 | 256 |
| r8idn.32xlarge | 1 | 16 | 32 | 128 | 512 |
| r8idn.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8idn.96xlarge | 2 | 12 | 32 | 128 | 768 |
| r8idn.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8idn.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| r8ib.large | 1 | 4 | 2 | 2 | 8 |
| r8ib.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8ib.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8ib.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8ib.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r8ib.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8ib.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8ib.24xlarge | 1 | 16 | 16 | 128 | 256 |
| r8ib.32xlarge | 1 | 16 | 32 | 128 | 512 |
| r8ib.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8ib.96xlarge | 2 | 12 | 32 | 128 | 768 |
| r8ib.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8ib.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| r8idb.large | 1 | 4 | 2 | 2 | 8 |
| r8idb.xlarge | 1 | 4 | 4 | 4 | 16 |
| r8idb.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r8idb.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r8idb.8xlarge | 1 | 8 | 16 | 32 | 128 |
| r8idb.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r8idb.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r8idb.24xlarge | 1 | 16 | 16 | 128 | 256 |
| r8idb.32xlarge | 1 | 16 | 32 | 128 | 512 |
| r8idb.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r8idb.96xlarge | 2 | 12 | 32 | 128 | 768 |
| r8idb.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r8idb.metal-96xl | 2 | 12 | 32 | 128 | 768 |
| r9g.medium | 1 | 2 | 1 | 1 | 2 |
| r9g.large | 1 | 3 | 2 | 2 | 6 |
| r9g.xlarge | 1 | 4 | 4 | 4 | 16 |
| r9g.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r9g.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r9g.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r9g.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r9g.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r9g.24xlarge | 1 | 24 | 16 | 128 | 384 |
| r9g.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r9g.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| r9gd.medium | 1 | 2 | 1 | 1 | 2 |
| r9gd.large | 1 | 3 | 2 | 2 | 6 |
| r9gd.xlarge | 1 | 4 | 4 | 4 | 16 |
| r9gd.2xlarge | 1 | 4 | 8 | 8 | 32 |
| r9gd.4xlarge | 1 | 8 | 8 | 16 | 64 |
| r9gd.8xlarge | 1 | 10 | 8 | 32 | 128 |
| r9gd.12xlarge | 1 | 12 | 16 | 64 | 192 |
| r9gd.16xlarge | 1 | 16 | 16 | 64 | 256 |
| r9gd.24xlarge | 1 | 24 | 16 | 128 | 384 |
| r9gd.48xlarge | 1 | 24 | 32 | 128 | 768 |
| r9gd.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| x8aedz.large | 1 | 4 | 2 | 2 | 8 |
| x8aedz.xlarge | 1 | 4 | 4 | 4 | 16 |
| x8aedz.3xlarge | 1 | 8 | 4 | 16 | 48 |
| x8aedz.6xlarge | 1 | 8 | 8 | 32 | 96 |
| x8aedz.12xlarge | 1 | 16 | 8 | 64 | 192 |
| x8aedz.24xlarge | 1 | 16 | 16 | 128 | 384 |
| x8aedz.metal-12xl | 1 | 16 | 8 | 64 | 192 |
| x8aedz.metal-24xl | 1 | 16 | 16 | 128 | 384 |
| x8i.large | 1 | 3 | 2 | 2 | 6 |
| x8i.xlarge | 1 | 4 | 4 | 4 | 16 |
| x8i.2xlarge | 1 | 4 | 8 | 8 | 32 |
| x8i.4xlarge | 1 | 8 | 8 | 16 | 64 |
| x8i.8xlarge | 1 | 10 | 8 | 32 | 128 |
| x8i.12xlarge | 1 | 12 | 16 | 64 | 192 |
| x8i.16xlarge | 1 | 16 | 16 | 64 | 256 |
| x8i.24xlarge | 1 | 16 | 16 | 128 | 384 |
| x8i.32xlarge | 1 | 24 | 16 | 128 | 512 |
| x8i.48xlarge | 1 | 24 | 32 | 128 | 768 |
| x8i.64xlarge | 1 | 24 | 32 | 128 | 1024 |
| x8i.96xlarge | 1 | 24 | 32 | 128 | 1536 |
| x8i.metal-48xl | 1 | 24 | 32 | 128 | 768 |
| x8i.metal-96xl | 1 | 24 | 32 | 128 | 1536 |

------
#### [ Storage optimized ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| i8ge.large | 1 | 3 | 2 | 2 | 6 |
| i8ge.xlarge | 1 | 4 | 4 | 4 | 16 |
| i8ge.2xlarge | 1 | 4 | 8 | 8 | 32 |
| i8ge.3xlarge | 1 | 6 | 8 | 16 | 48 |
| i8ge.6xlarge | 1 | 10 | 8 | 32 | 96 |
| i8ge.12xlarge | 1 | 12 | 16 | 64 | 192 |
| i8ge.18xlarge | 1 | 16 | 16 | 128 | 288 |
| i8ge.24xlarge | 1 | 16 | 16 | 128 | 384 |
| i8ge.48xlarge | 2 | 12 | 32 | 128 | 768 |

------
#### [ Accelerated computing ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| g7.2xlarge | 1 | 4 | 8 | 8 | 32 |
| g7.4xlarge | 1 | 8 | 8 | 16 | 64 |
| g7.8xlarge | 1 | 10 | 8 | 32 | 80 |
| g7.12xlarge | 1 | 12 | 16 | 64 | 192 |
| g7.24xlarge | 1 | 24 | 16 | 128 | 384 |
| g7.48xlarge | 2 | 12 | 32 | 128 | 384 |

------
#### [ High performance computing ]

| Instance type | Network cards | Maximum network interfaces per network card | Default ENA queues per interface | Maximum ENA queues per interface | ENA queue pool per network card |
| --- | --- | --- | --- | --- | --- |
| hpc8a.96xlarge | 2 | 2 | 32 | 128 | 256 |

------

**Note**
The ENA queue pool and the number of network interfaces are per network card. On instance types with multiple network cards, each card has its own pool. For the number of network cards, see [Network cards](using-eni.md#network-cards).

## Network interface limits and ENA queues
<a name="ena-queues-network-interface-limits"></a>

On instance types that support configurable ENA queue allocation, two limits determine how many network interfaces you can attach: the maximum number of network interfaces for the instance type, and the ENA queues that remain available in the pool of each network card. If the queue count that you request for a network interface (or the default, if you don't specify one) is more than the queues that remain in the pool for its network card, the attachment fails, even if the instance hasn't reached its maximum number of network interfaces.

Starting with 8th generation instance types, the maximum number of network interfaces for each network card is fixed. Configuring fewer ENA queues per interface lets you attach more network interfaces, up to that maximum, but doesn't raise the maximum.

C6in, M6in, and R6in instance types work differently. On these instance types, you can attach additional network interfaces beyond the maximum if you configure fewer ENA queues per interface. The specification tables on this page don't include these additional network interfaces. To find the number for an instance type, check `AdditionalFlexibleNetworkInterfaces` in the output of the [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command.

To check whether your network interfaces fit with the default queue count, multiply the default ENA queues per interface by the number of network interfaces on the card, and compare the result to the card's pool. To choose a smaller count, divide the pool by the number of network interfaces that you want on the card, and then use the largest power of 2 that is no more than that result and no more than the maximum ENA queues per interface.

For example, consider an instance type with a pool of 128 ENA queues on its network card, a default of 16 ENA queues per interface, and a maximum of 32 queues per interface.
+ With the default queue count, 10 network interfaces need 10 × 16 = 160 queues. That is more than the pool of 128, so only 8 network interfaces fit with the default (8 × 16 = 128).
+ To attach all 10 network interfaces, divide the pool by the number of interfaces: 128 ÷ 10 = 12.8. The largest power of 2 that is no more than 12.8 is 8, and 8 is within the per-interface maximum of 32. With 8 queues each, 10 network interfaces need 10 × 8 = 80 queues, which fits within the pool of 128. To attach all 10 network interfaces, specify `--ena-queue-count 8` for each one.

If the queue counts for the network interfaces on a network card exceed the pool for that card, the attachment fails with an error such as `The sum of ENA queue counts for all interfaces on network card 0 exceeds the maximum allowed value of 128`.

## Configure ENA queue allocation
<a name="modify"></a>

On supported instance types, you can configure the ENA queue count for each network interface. Use the AWS Management Console, AWS CLI, or PowerShell. In the AWS Management Console, this setting appears under each **Network interface**.

**Note**
Before you configure ENA queues, note the following requirements:
You can set the number of ENA queues when you launch an instance or attach a network interface, including to a running instance. To change the number of ENA queues for a network interface that is already attached, you must stop the instance first.
The value must be a power of 2, such as 1, 2, 4, 8, 16, or 32, and can't be more than the maximum ENA queues per interface for the instance type.
The total number of ENA queues for all network interfaces on a network card can't exceed the ENA queue pool for that network card.

Before you change the queue count, check your current count with the following command.

------
#### [ AWS CLI ]

```json
aws ec2 describe-instances --instance-id {{i-1234567890abcdef0}}
```

------
#### [ PowerShell ]

```powershell
(Get-EC2Instance -InstanceId i-{{1234567890abcdef0}}).Instances.NetworkInterfaces |
  Select-Object NetworkInterfaceId,
    @{N='DeviceIndex';E={$_.Attachment.DeviceIndex}},
    @{N='AttachmentId';E={$_.Attachment.AttachmentId}},
    @{N='EnaQueueCount';E={$_.Attachment.EnaQueueCount}}
```

------

If EnaQueueCount isn't returned for a network interface, the network interface uses the default number of ENA queues for the instance type.

To view only the ENA queue count for each network interface, use one of the following commands.

------
#### [ AWS CLI ]

```json
aws ec2 describe-instances \
  --instance-ids {{i-1234567890abcdef0}} \
  --query 'Reservations[].Instances[].NetworkInterfaces[].{Device: Attachment.DeviceIndex, Card: Attachment.NetworkCardIndex, Queues: Attachment.EnaQueueCount}' \
  --output table
```

------
#### [ PowerShell ]

```powershell
(Get-EC2Instance -InstanceId {{i-1234567890abcdef0}}).Instances.NetworkInterfaces |
  Select-Object @{N='Device';E={$_.Attachment.DeviceIndex}},
    @{N='Card';E={$_.Attachment.NetworkCardIndex}},
    @{N='Queues';E={$_.Attachment.EnaQueueCount}} |
  Format-Table
```

------

### Attach a network interface with ENA queues
<a name="modify-attach"></a>

In the following example, 16 ENA queues are configured on a network interface.

------
#### [ AWS CLI ]

**To attach a network interface with ENA queues**
Use the [attach-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-network-interface.html) command.

```json
aws ec2 attach-network-interface \
  --network-interface-id eni-{{abcdef01234567890}} \
  --instance-id {{i-1234567890abcdef0}} \
  --device-index 1 \
  --ena-queue-count 16
```

------
#### [ PowerShell ]

**To attach a network interface with ENA queues**
Use the [Add-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2NetworkInterface.html) cmdlet.

```powershell
Add-EC2NetworkInterface `
  -NetworkInterfaceId eni-{{abcdef01234567890}} `
  -InstanceId {{i-1234567890abcdef0}} `
  -DeviceIndex 1 `
  -EnaQueueCount 16
```

------

### Launch an instance with ENA queues
<a name="modify-run"></a>

In the following example, 16 ENA queues each are configured on 3 network interfaces.

------
#### [ AWS CLI ]

**To launch an instance with ENA queues**
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command.

```json
aws ec2 run-instances \
  --image-id ami-{{1234567890abcdef0}} \
  --instance-type c8i.4xlarge \
  --network-interfaces \
    "[{\"DeviceIndex\":0,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":1,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16},
      {\"DeviceIndex\":2,\"SubnetId\":\"subnet-{{abcdef01234567890}}\",\"EnaQueueCount\":16}]"
```

------
#### [ PowerShell ]

**To launch an instance with ENA queues**
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet.

```powershell
New-EC2Instance `
  -ImageId ami-{{1234567890abcdef0}} `
  -InstanceType c8i.4xlarge `
  -NetworkInterface @(
    @{DeviceIndex=0; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16},
    @{DeviceIndex=1; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16},
    @{DeviceIndex=2; SubnetId="subnet-{{abcdef01234567890}}"; EnaQueueCount=16}
  )
```

------

### Modify ENA queues on an existing network interface
<a name="modify-eni-attribute"></a>

In the following example, 16 ENA queues are configured on a network interface.

------
#### [ AWS CLI ]

**To modify ENA queues on a network interface**
Use the [modify-network-interface-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-network-interface-attribute.html) command.

```json
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-{{1234567890abcdef0}} \
  --attachment AttachmentId=eni-attach-{{1234567890abcdef0}},EnaQueueCount=16
```

------
#### [ PowerShell ]

**To modify ENA queues on a network interface**
Use the [Edit-EC2NetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2NetworkInterfaceAttribute.html) cmdlet.

```powershell
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-{{1234567890abcdef0}} `
  -Attachment_AttachmentId eni-attach-{{1234567890abcdef0}} `
  -Attachment_EnaQueueCount 16
```

------

In the following example, the ENA count is reset to the default value.

------
#### [ AWS CLI ]

```json
aws ec2 modify-network-interface-attribute \
  --network-interface-id eni-{{1234567890abcdef0}} \
  --attachment AttachmentId=eni-attach-{{1234567890abcdef0}},DefaultEnaQueueCount=true
```

------
#### [ PowerShell ]

```powershell
Edit-EC2NetworkInterfaceAttribute `
  -NetworkInterfaceId eni-{{1234567890abcdef0}} `
  -Attachment_AttachmentId eni-attach-{{1234567890abcdef0}} `
  -Attachment_DefaultEnaQueueCount $true
```

------
