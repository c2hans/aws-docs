---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-lattice.html
---

# Amazon VPC Lattice
<a name="vpc-lattice"></a>

 Amazon VPC Lattice is a fully managed application networking service that is used to connect, monitor, and secure services across various accounts and virtual private clouds. VPC Lattice helps to interconnect services within a logical boundary, so that you can manage and discover them efficiently.

 VPC Lattice components consists of:
+  **Service** - This is a unit of application running on an instance, a container, or a Lambda function and consists of listeners, rules and target groups.
+  **Service network** - This is the logical boundary that is used to automatically implement service discovery and connectivity and apply common access and observability policies to a collection of services.
+  **Auth policies** - IAM resource policies that can be associated with a service network or individual services to support request-level authentication and context-specific authorization.
+  **Service Directory** - A centralized view of the services that you own or that have been shared with you through the AWS Resource Access Manager.

 VPC Lattice usage steps:

1.  Create the service network. The service network usually resides on a network account where a network administrator has full access. The service network can be shared across multiple accounts within an organization. Sharing can be performed on individual services or the entire service account.

1.  Attach VPCs to the service network to enable application networking for each VPC, so that different services can start consuming other services that are registered within the network. Security groups are applied to control traffic.

1.  Developers define the services, which are populated in the service directory and registered into the service network. VPC Lattice contains the address book of all services configured. Developers can also define routing polices to use blue/green deployments. Security is managed at the service network level where authentication and authorization policies are defined and at the service level where access policies with IAM are implemented.

![A diagram depicting VPC Lattice communication flows](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/vpc-lattice.png)

 More details can be found in the [VPC Lattice user guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html ).
