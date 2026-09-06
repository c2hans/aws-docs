---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/introduction.html
---

# Robust network design with AWS Control Tower
<a name="introduction"></a>

*T.V.R.L.Phani Kumar Dadi, Chintamani Aphale, JAGDISH KOMAKULA, Pratap Kumar Nanda, Pradip kumar Pandey, Aarti Rajput, and Mayuri Shinde, Amazon Web Services*

Security plays a crucial role for any organization. One of the key factors of application security is networking. A loophole in networking can open various options for cybercriminals to compromise applications and take control over systems. This guide defines some of the best practices when using AWS Control Tower to design a network at the AWS Organizations level. The goal of the network design is to provide easier management, improved security, and protection for the applications hosted on the AWS Cloud. To help meet this goal, the network design includes inspecting, filtering, and logging the traffic that comes in and goes out to internet from a single centralized network account in AWS.

The approach covered uses a centralized network account with three virtual private clouds (VPCs). Inbound and outbound traffic from spoke VPCs and the internet is filtered by AWS WAF and AWS Network Firewall. AWS Transit Gateway and VPC endpoints help route the traffic.

## Prerequisites
<a name="prerequisites"></a>
+ An active [AWS account](https://aws.amazon.com/resources/create-account/)
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) set up
+ Knowledge of [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/extend-tgw.html)
+ Knowledge of networking and network security

## Centralized network account
<a name="network-account"></a>

When managing an organization's entire network, we recommend having a separate account that is dedicated for managing networking components or services. First, the networking team requests the creation of an account (network) for managing networking services. After you create the new account, note the account number. Next, change [Amazon Virtual Private Cloud (Amazon VPC) IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) control from the AWS Control Tower management account to the network account by providing the account details in IPAM.

The newly created account will be your centralized network account, which will manage the following network services:
+ IPAM
+ VPC configuration
+ Network access control list (ACL)
+ Centralized network firewall
+ AWS Transit Gateway
+ VPC endpoint configuration
+ Centralized DNS management
+ Centralized inbound traffic
+ AWS WAF
