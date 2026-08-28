---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/data-management-and-transfer.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data management and transfer
<a name="data-management-and-transfer"></a>

 Although HPC systems in financial services are typically loosely coupled, with limited need for *East-West* communication between compute instances, there are still significant demands for *North-South* communication bandwidth between layers in the stack. A key consideration for networking is where in the stack any separation between on-premises systems and cloud-based systems occurs. This is because communication within the AWS network is typically of higher bandwidth and lower cost than communication to external networks. As a result, any architecture that causes hundreds or thousands of compute instances to connect to an external network—particularly if they’re requesting the same binaries or task data—would create a bottleneck.

 Ideally, the *fanout* point (the point in the architecture at which large numbers of instances are introduced) is in the cloud. This means that the larger volumes of communication stay in the AWS network with relatively few connections to on-premises systems.

 AWS offers networking services that complement the financial services HPC systems. A common starting point is to deploy [AWS Direct Connect](https://aws.amazon.com/directconnect/) connections between customer data centers and an AWS Region through a third-party point of presence (PoP) provider. A Direct Connect link offers a consistent and predictable experience with speeds of up to 100Gbps. You can employ multiple diverse Direct Connect links to provide highly resilient, high-bandwidth connectivity.

 Though most HPC applications within financial services are loosely coupled, this isn’t universal and there are times when network bandwidth is a significant component of overall performance. The current AWS Nitro–based instances offer various levels of network bandwidth with the largest compute instance types such as the c6in.32xlarge or c7gn.16xlarge instances, which offer up to 200Gbps (in the case of c6i.32xlarge, two network interfaces must be attached to get a maximum of 200Gbps) and GPU enabled p5 instances offering up to 3,200 Gbps. Additionally, a cluster [placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node-to-node communication that is typical of some HPC applications.

 The [Elastic Fabric Adaptor](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html) service (EFA) enhances the Elastic Network Adaptor (ENA), and is specifically engineered to support tightly-coupled HPC workloads which require low latency communication between instances. An EFA is a virtual network device which can be attached to an Amazon EC2 instance. EFA is suited to workloads using the [Message Passing Interface](https://en.wikipedia.org/wiki/Message_Passing_Interface) (MPI). EFA may be worthy of consideration for some financial services workloads, such as weather predictions, as part of an insurance industry catastrophic event model.

 EFA traffic that bypasses the operating system (OS-bypass) is not routable, so it’s limited to a single subnet. As a result, any peers in this network must be in the same subnet and Availability Zone, which could alter resiliency strategies. The OS-bypass capabilities of EFA are also not supported on Windows.

 Some Amazon EC2 instance types support *jumbo frames* where the Network Maximum Transmission Unit (the number of bytes per packet) is increased. AWS supports MTUs of up to 9001 bytes. By using fewer packets to send the same amount of data, end-to-end network performance is improved.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
